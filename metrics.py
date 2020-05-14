import torch 
# import tqdm
from torch.utils.data import DataLoader

def get_metric(metric_dict, eval_flag=False):
    loss_function = None
    name = metric_dict.get("name")
    distance = metric_dict.get("distance", False)
    distance_factor = metric_dict.get("factor", 1)
    distance_width = metric_dict.get("width", 0.01)


    if name == "softmax_accuracy":
        loss_function =  softmax_accuracy

    elif name == "softmax_loss":
        loss_function =  softmax_loss

    if distance and not eval_flag:
        print("used distance function")
        return distance_wrapper(loss_function, distance_factor, distance_width)
    else:
        return loss_function

    



@torch.no_grad()
def compute_metric_on_dataset(model, dataset, metric_dict, cuda):
    metric_function = get_metric(metric_dict, True)
    metric_name = metric_dict.get("name")
    
    model.eval()

    loader = DataLoader(dataset, drop_last=False, batch_size=1024)
    print("> Computing %s..." % (metric_name))

    score_sum = 0.
    for images, labels in loader: # tqdm.tqdm(loader):
        if cuda:
            images, labels = images.cuda(), labels.cuda()

        score_sum += metric_function(model, images, labels).item() * images.shape[0] 
            
    score = float(score_sum / len(loader.dataset))

    print('The current %s value is %f' %(metric_name, score))

    return score



def softmax_loss(model, images, labels):
    logits = model(images)
    criterion = torch.nn.CrossEntropyLoss(reduction="mean")
    loss = criterion(logits, labels.view(-1))
    return loss



def computedistance(minimum, model):
    distance = 0
    for minparam, param in zip(minimum, model.parameters()):
        dif = torch.add(-param, minparam)
        distance += torch.sum(torch.mul(dif, dif))
    return distance


def softmax_accuracy(model, images, labels):
    logits = model(images)
    pred_labels = logits.argmax(dim=1)
    acc = (pred_labels == labels).float().mean()

    return acc



def distance_wrapper(loss_function, distance_factor, distance_width):

    def loss_distance(model, images, labels, minimum_list):
        loss = 0
        classify_loss = loss_function(model, images, labels)
        loss += classify_loss
        for minimum in minimum_list:
            loss += distance_factor/len(minimum_list) * torch.exp(-1* distance_width * computedistance(minimum, model)) # divided by length to be the same as before

        return loss

    return loss_distance
