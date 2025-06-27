import torch.nn as nn
import torchvision.models as models

def get_model(num_classes=38):
    model = models.resnet18(weights=None)

    # Change input layer to accept grayscale (1-channel) instead of RGB (3-channel)
    model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

    # Change final layer to match the number of output classes
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)

    return model
