#Tutorial from https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html :)
from cgi import test
from numpy import dtype
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor


#Downloading trainings data from dataset MNIST
trainig_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)
#Downloading test data from dataset MNIST
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

batch_size=64

#Creating data loaders
##Wraps dataset in iterable(i) for use
train_datloader= DataLoader(trainig_data, batch_size=batch_size)
test_dataloader =DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print(f"Shape of X [N, C,H,W]:{X.shape}")
    print(f"Shape of y: {y.shape}{y.dtype}")
    break