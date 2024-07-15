import torch
from PIL import Image, ImageDraw
from facenet_pytorch import MTCNN, extract_face
import os
CWD = os.getcwd()

def face(path = CWD + '/hello.jpg'):
    image = Image.open(path)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(
        image_size=224, margin=100, min_face_size=20,
        thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
        device=device
    )
    boxes, probs, points = mtcnn.detect(image, landmarks = True)
    img_draw = image.copy()
    draw = ImageDraw.Draw(img_draw)
    for i, (box, point) in enumerate(zip(boxes, points)):
        draw.rectangle(box.tolist(), width=5)
        for p in point:
            draw.rectangle((p - 10).tolist() + (p + 10).tolist(), width=30)
        extract_face(image, box, save_path='detected_face_{}.png'.format(i))

    if os.path.exists(path):
        os.remove(path)

    del mtcnn
    