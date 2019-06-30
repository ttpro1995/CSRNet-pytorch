import torch
import dataset
from torchvision import datasets, transforms
from create_train_dataset import create_training_image_list, DATA_PATH

"""
This help me understand data loader

"""

if __name__ == "__main__":
    train_list = create_training_image_list(DATA_PATH)

    train_loader = torch.utils.data.DataLoader(
        dataset.listDataset(train_list,
                       shuffle=True,
                       transform=transforms.Compose([
                       transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225]),
                   ]),
                       train=True,
                       batch_size=1,
                       num_workers=1),
        batch_size=1)  # if you have different image size, then batch_size must be 1

    print(type(train_loader))

    for batch_ndx, sample in enumerate(train_loader):
        img = sample[0]
        density = sample[1]
        print("img shape ", img.shape)
        print("density shape", density.shape)