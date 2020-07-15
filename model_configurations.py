EXP_GROUPS = {
        "mobileNetV2_baseline":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_baseline_distance":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline_distance":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},


    # -----------------------width---------------------------------------------
    
        "mobileNetV2_width_e1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-1, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

        "mobileNetV2_width_e2":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-2, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

        "mobileNetV2_width_e4":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-4, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

        "ResNet32_width_e1":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-1, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

        "ResNet32_width_e2":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-2, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

        "ResNet32_width_e4":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-4, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":400},

    # -----------------------strength------------------------------------------

        "mobileNetV2_strength_e1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":0.1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_strength_e2":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_strength_e3":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_strength_e1":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":0.1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_strength_e2":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_strength_e3":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

    # -----------------------lr variations------------------------------------

        "mobileNetV2_baseline_distance_lr3":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_baseline_lr3":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_baseline_distance_lr1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "mobileNetV2_baseline_lr1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline_lr3":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline_distance_lr3":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-3, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline_lr1":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},

        "ResNet32_baseline_distance_lr1":{"dataset":"cifar10",
            "model":"resnet32",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 100, "multiple": False},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200},


    # -----------------------new stuff-----------------------------------------

        "mobileNetV2_distance_as_cosine_f1":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_distance_as_cosine_f10":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":10, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900},

        "mobileNetV2_distance_as_cosine_f100":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":100, "width":1e-3, "step": 150, "multiple": True},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": "None", "step": 50, "cycle":150},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":900}
}




# TODO: Run baseline 400 epochs for width


