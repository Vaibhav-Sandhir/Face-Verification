import torch
from PIL import Image
from torchvision.transforms import transforms
import torch.nn.functional as F
import os
from extract_face import face
import json
CWD = os.getcwd()

transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
])

def verify():
    face()
    img = Image.open(CWD + '/detected_face_0.png') 
    img = transform(img)
    img = img.unsqueeze(0).to("cuda")   

    with open('people_embeddings.json', 'r') as f:
        people = json.load(f)

    for person in people.keys():
        people[person] = torch.tensor(people[person]).to("cuda")
    
    model = torch.load(CWD + '/siamese_model.pt')
    model = model.to("cuda")
    model.eval()

    min_dist = 10000000000
    correct_person = "None"
    with torch.inference_mode():
        o1 = model.forward_one_image(img)
        for person in people.keys():
            o2 = (people[person])
            distance = F.pairwise_distance(o1, o2, keepdim = True)
            if distance < min_dist and distance <= 1.0:
                min_dist = distance
                correct_person = person
    
    for i in range(0, 5):
        if os.path.exists(CWD + f'/detected_face_{i}.png'):
            os.remove(CWD + f'/detected_face_{i}.png')

    del model
    return correct_person