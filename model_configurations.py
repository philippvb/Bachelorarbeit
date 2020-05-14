EXP_GROUPS = {
        "mnist1":{"dataset":"mnist",
            "model":"mlp",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":40},

        "cifar10_1":{"dataset":"cifar10",
            "model":"resnet34",
            "loss_func": {"name":"softmax_loss", "distance":True, "factor":1, "width":1e-3, "step": 60},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-2, "regularization":0.001, "scheduler": True},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":380},

        "mobileNetV2":{"dataset":"cifar10",
            "model":"mobileNetV2",
            "loss_func": {"name":"softmax_loss", "distance":False, "factor":1, "width":1e-3},
            "optimizer":{"name":"sgd_momentum_wdecay", "lr":1e-1, "regularization":0.001, "scheduler": True, "step": 50},
            "acc_func":{"name":"softmax_accuracy"},
            "batch_size":128,
            "max_epochs":200}
            
}
