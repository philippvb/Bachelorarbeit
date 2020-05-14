import os
import json
import pickle


import numpy as np
import time
import argparse
import torch
from torch.utils.tensorboard import SummaryWriter
import uuid

import pprint
import pandas as pd
import sys


import datasets
import optimizers, model_configurations
import models
import metrics








def train(experiment_dictionary, save_directory_base, data_directory, name=None, new_name=None):

    gpu_exists = torch.cuda.is_available()
    name = name if name else str(uuid.uuid1())
    save_directory = os.path.join(save_directory_base, name)
    base_model_directory = None
    continue_Training = False


    # look if dir alraedy exists, if so, create new based on newName
    if os.path.exists(save_directory) and new_name:
        base_model_directory = os.path.join(save_directory_base, name)
        save_directory = os.path.join(save_directory_base, name, new_name)
        continue_Training = True

    os.makedirs(save_directory, exist_ok=False)

    # init Tensorboard 
    writer = SummaryWriter(save_directory)


    # save configuration
    with open(os.path.join(save_directory, 'exp_dict.json'), 'w') as outfile:
        json.dump(experiment_dictionary, outfile)
    pprint.pprint(experiment_dictionary)
    print('Experiment saved in %s' % save_directory)


    # set seeds
    seed = 1234
    np.random.seed(seed)
    torch.manual_seed(seed)

    # load datasets
    train_set = datasets.getDataSet(experiment_dictionary['dataset'], data_directory, train_flag=True)

    train_loader = torch.utils.data.DataLoader(train_set, drop_last=True, shuffle=True, batch_size=experiment_dictionary['batch_size'])

    val_set = datasets.getDataSet(experiment_dictionary['dataset'], data_directory, train_flag=False)


    # load model and optimizer
    model = models.get_Model(experiment_dictionary['model'], experiment_dictionary['dataset'])
    if gpu_exists:
        model.cuda()

    opt = optimizers.get_optimizer(experiment_dictionary['optimizer'], model.parameters())

    if experiment_dictionary['optimizer'].get("scheduler"):
        scheduler = torch.optim.lr_scheduler.StepLR(opt, experiment_dictionary["optimizer"].get("step"), 0.1)

    loss_function = metrics.get_metric(experiment_dictionary['loss_func'])



    # create checkpoint
    model_path = os.path.join(save_directory, 'model.pth')
    opt_path = os.path.join(save_directory, 'opt_state_dict.pth')
    score_list_path = os.path.join(save_directory, 'score_list.pkl')

    if continue_Training:
        model.load_state_dict(torch.load(os.path.join(base_model_directory, 'model.pth')))
        opt.load_state_dict(torch.load(os.path.join(base_model_directory, 'opt_state_dict.pth'), map_location=torch.device('cpu'))) #, map_location=torch.device('cpu') if cpu
        for param_group in opt.param_groups:
            param_group['lr'] = experiment_dictionary['optimizer'].get("lr") # if new learn rate is wished for example in step decay but momentum should be kept

        score_list = pickle.load(open(os.path.join(base_model_directory, 'score_list.pkl'), 'rb'))
        next_epoch = score_list[-1]['epoch'] + 1
    else:
        score_list = []
        initial_loss = metrics.compute_metric_on_dataset(model, train_set,
                                                metric_dict=experiment_dictionary["loss_func"], cuda=gpu_exists)

        initial_accuracy = metrics.compute_metric_on_dataset(model, val_set,
                                                        metric_dict=experiment_dictionary["acc_func"], cuda=gpu_exists)
        writer.add_scalar('Train_loss', initial_loss, 0)
        writer.add_scalar('Validation_accuracy', initial_accuracy, 0)
        writer.flush()

        score_dict = {"epoch": 0}
        score_dict["train_loss"] = initial_loss
        score_dict["val_acc"] = initial_accuracy
        score_dict["batch_size"] =  train_loader.batch_size
        score_list += [score_dict]
        next_epoch = 1


    # save current state as minimum
    minimum = []
    for param in model.parameters():
        newparams = param.clone().detach().to(device='cuda') #use clone to clone and detach to clear gradient
        minimum.append(newparams)


    print('Starting experiment at epoch %d/%d' % (next_epoch, experiment_dictionary['max_epochs']))

    for epoch in range(next_epoch, experiment_dictionary['max_epochs'] + 1):

        print('\n\n Starting epoch %d' %epoch)

        # start training
        model.train()
        print("Epoch %d - Training model with %s..." % (epoch, experiment_dictionary["loss_func"].get("name")))

        start_time = time.time()
        for images,labels in train_loader:#tqdm.tqdm(train_loader):
            if gpu_exists:
                images, labels = images.cuda(), labels.cuda()
            
            opt.zero_grad()

            if experiment_dictionary["loss_func"].get("distance"):
                loss = loss_function(model, images, labels, minimum)
            else:
                loss = loss_function(model, images, labels)
                
            loss.backward()
            opt.step()

        end_time = time.time()

        scheduler.step()

        # evaluate model
        
        train_loss = metrics.compute_metric_on_dataset(model, train_set,
                                                metric_dict=experiment_dictionary["loss_func"], cuda=gpu_exists)

        val_acc = metrics.compute_metric_on_dataset(model, val_set,
                                                        metric_dict=experiment_dictionary["acc_func"], cuda=gpu_exists)

        with torch.no_grad():
            distance = metrics.computedistance(minimum, model).data
            print('Current distance to last minimum checkpoint: %f' % distance)

        writer.add_scalar('Train_loss', train_loss, epoch)
        writer.add_scalar('Validation_accuracy', val_acc, epoch)
        writer.add_scalar('distance', distance, epoch)
        writer.add_scalar('similarity', torch.exp(-1* experiment_dictionary["loss_func"].get("width") * distance), epoch)
        writer.add_scalar('lr', get_lr(opt), epoch)
        writer.flush()

        print(get_lr(opt))

        score_dict = {"epoch": epoch}
        score_dict["train_loss"] = train_loss
        score_dict["val_acc"] = val_acc
        score_dict["batch_size"] =  train_loader.batch_size
        score_dict["train_epoch_time"] = end_time - start_time
        score_dict["distance"] = distance
        score_list += [score_dict]

        with open(score_list_path, 'wb') as outfile:
            pickle.dump(score_list, outfile)
        torch.save(model.state_dict(), model_path)
        torch.save(opt.state_dict(), opt_path)


        

        # flush printer
        sys.stdout.flush()
        

    print('Experiment completed')
    print('Printing summary')
    print(pd.DataFrame(score_list))



def get_lr(optimizer):
    for param_group in optimizer.param_groups:
        return param_group['lr']


if __name__ == '__main__':
        parser = argparse.ArgumentParser()

        parser.add_argument('-n', '--name')
        parser.add_argument('-nn', '--newname')
        parser.add_argument('-sb', '--savedir_base', default='./results')
        parser.add_argument('-d', '--datadir', default='./data')
        parser.add_argument('-en', '--experiment_name', required=True, nargs='+')

        args = parser.parse_args()

        for experiment in args.experiment_name:
            train(model_configurations.EXP_GROUPS[experiment], 
            args.savedir_base, 
            args.datadir,
            args.name,
            args.newname)