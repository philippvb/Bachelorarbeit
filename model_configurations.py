EXP_GROUPS = {
        "MNIST":{"dataset":"mnist",
            "model":"mlp",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 60, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": True, "step": 20, "cycle": 60},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":800},
            
        "resnet32_lr1_cosine":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True, "merge": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle": 150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_ensemble":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "step", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_ensemble_distance_f2":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "step", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_ensemble_distance_f2_w4":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-4, "step": 150},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "step", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},


        "mobileNetV2_lr1_distance":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_lr1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_lr0001_distance":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

            "mobileNetV2_lr0001":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "cosine", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900}
}

# rename step to cycle in loss_func

