EXP_GROUPS = {
        "mobileNetV2_multiple":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":100},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_multiple_f100_noreg":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0., "scheduler": "None", "step": 50, "cycle":100},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},
        
        "ResNet32_scheduler_step":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "step", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_cosine_lr0":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_cosine_lr0_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_scheduler_cosine_lr0":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_scheduler_cosine_distance_lr0":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_baseline":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        


# ------------------------ensemble---------------------------------------------


        "mobileNetV2_ensemble_baseline":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "mobileNetV2_ensemble_baseline_cosine":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "mobileNetV2_ensemble_distance":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "mobileNetV2_ensemble_distance_f10":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

            # *---------------------------------------------------------

        "mobileNetV2_ensemble_distance_f100":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "mobileNetV2_ensemble_distance_f100_w4":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-4, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "mobileNetV2_ensemble_distance_f1000":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1000, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},


        "mobileNetV2_scheduler_cosine_distance_lr1_f10":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_scheduler_cosine_distance_lr1_f100":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},





        #-----------------------------------------------------------
        
        "ResNet32_ensemble_baseline":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "ResNet32_ensemble_baseline_cosine":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "ResNet32_ensemble_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750},

        "ResNet32_ensemble_distance_f10":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":750}


        
}

# [TODO: stronger factors for cosine scheduler distance]
# baseline lr1 600 epochs for both with and wothout distance
# multiple again for more constant epoch time ----



# cosine scheduler wrong lr other factors like smaller and larger lr (especially larger)-----
# resnet scheduler step ----
# does distance come back after kernel is away again??
# multiple without regularization -----
# baseline see gradient-----


# ensemble distance f100
# ensemble distance f100 w4
# ensemble distance f1000
# scheduler distance wrong lr other factors

