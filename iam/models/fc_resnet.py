import torch.nn as nn


class FC_ResNet(nn.Module):

    def __init__(self, model, num_classes):
        super(FC_ResNet, self).__init__()

        # feature encoding
        self.features = nn.Sequential(
            model.conv1,
            model.bn1,
            model.relu,
            model.maxpool,
            model.layer1,
            model.layer2,
            model.layer3,
            model.layer4)

        # classifier
        self.num_features = model.layer4[1].conv1.in_channels
        self.classifier = nn.Sequential(
            nn.Conv2d(self.num_features, num_classes, kernel_size=1, bias=True))

    def get_feature_map_channel(self):
        return self.num_features

    def forward(self, x):
        x = self.features(x)
        y = x
        x = self.classifier(x)
        return x, y
