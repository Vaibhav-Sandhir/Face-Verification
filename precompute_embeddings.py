import os
from torchvision.transforms import transforms
from PIL import Image
from siamese import SiameseNetwork
import torch
import json
CWD = os.getcwd()

transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
])

if __name__ == "__main__":
    model = torch.load(CWD + '/siamese_model.pt').to("cuda")
    directory = CWD + '/photos'
    people_embeddings = {}
    model.eval()

    with torch.inference_mode():
        for photo in os.listdir(directory):
            name, _ = photo.split('.')
            img_path = directory + '/' + photo
            img = Image.open(img_path)
            img = img.convert("RGB")
            img = transform(img)
            img = torch.unsqueeze(img, dim = 0)
            img = img.to("cuda")
            embedding = model(img)
            people_embeddings[name] = embedding.cpu().numpy().tolist()
    
    with open(CWD + '/people_embeddings.json', 'w') as f:
        json.dump(people_embeddings, f)

    del model