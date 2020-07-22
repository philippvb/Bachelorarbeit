EXP_GROUPS = {

        "mobileNetV2_baseline":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "mobileNetV2_baseline_distance":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_baseline":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_baseline_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
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

        "ResNet32_scheduler_cosine":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_step_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "step", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_cosine_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_cosine_lr1":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_scheduler_cosine_lr1_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

#---------------------------------------------------------------------------

         "ResNet32_multiple":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":100},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_multiple_f10":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_multiple_f100":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":600},

        "ResNet32_multiple_merge":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True, "merge":True},
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
# cosine scheduler wrong lr other factors like smaller and larger lr (especially larger)
