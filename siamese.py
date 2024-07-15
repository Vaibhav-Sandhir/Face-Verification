from torch.utils.data import Dataset, DataLoader
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch import nn
import torch
from torch import optim
import torch.nn.functional as F
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
from online_triplet_loss.losses import *
from Mining import *
import os
CWD = os.getcwd()
PATH_TO_TRAINING_IMAGES = '/home/vaibhav/Desktop/photos/train'

class SiameseNetwork(nn.Module):
    def __init__(self, resnet):
        super(SiameseNetwork, self).__init__()
        self.resnet = resnet
        self.fc1 = nn.Sequential(
            nn.Linear(in_features=512, out_features=256),
            nn.PReLU(),
            nn.Linear(in_features=256, out_features=128),
        )

    def forward_one_image(self, x):
        output = self.resnet(x)
        output = self.fc1(output)
        return output
    
    def forward(self, x):
        return self.forward_one_image(x)

if __name__ == "__main__":
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    dataset = ImageFolder(root = PATH_TO_TRAINING_IMAGES, transform=transform)
    margin = 2.0
    resnet = InceptionResnetV1(pretrained='vggface2').to("cuda")
    for param in list(resnet.parameters())[:-18]:
        param.requires_grad = False
    model = SiameseNetwork(resnet).to("cuda")
    train_dataloader = DataLoader(dataset, shuffle = True, batch_size = 64)

    optimizer = optim.Adam(model.parameters(), lr=0.0001)

    costs = []
    epochs = 90
    for epoch in range(epochs):
        cost = 0.0
        total_accuracy = 0.0
        for imgs, labels in train_dataloader:
            imgs = imgs.to("cuda")
            labels = labels.to("cuda")
            model.train()
            optimizer.zero_grad()
            embeddings = model(imgs)
            
            loss, pos_mask, neg_mask = online_mine_hard(labels, embeddings, margin, squared = True, device = "cuda")
            cost += loss.item()
            loss.backward()
            optimizer.step()

        costs.append(cost)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {cost}")

    plt.figure()
    plt.plot(range(1, epochs + 1), costs)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Epochs')
    plt.savefig('loss.png')
    torch.save(model, CWD + '/siamese_model.pt')
