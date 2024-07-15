from pymongo.mongo_client import MongoClient
import base64
import os
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('MONGO_URI')
cluster = MongoClient(uri)
db = cluster["project"]
collection = db["users"]

if __name__ == "__main__":
    images = {}
    directory = os.getcwd() + '/photos'
    for photo in os.listdir(directory):
        name, _ = photo.split('.')
        img_path = directory + '/' + photo
        with open(img_path, 'rb') as image_file:
            images[name] = base64.b64encode(image_file.read())
    time = datetime.now()

    document1 = {
        "name" : "Vaibhav", 
        "age" : 21, 
        "email" : "vaibhav.sandhir@learner.manipal.edu",
        "reg_number" : 210905152,
        "image" : images["Vaibhav"],
        "isAdmin" : True,
        "last_login" : time
    }
    document2 = {
        "name" : "Komal",
        "age" : 10,
        "email" : "komal.choudhry@learner.manipal.edu",
        "reg_number" : 210905356,
        "image" : images["Komal"],
        "isAdmin" : False,
        "last_login" : time
    }
    document3 = {
        "name" : "Ayush",
        "age" : 21,
        "email" : "ayush.prakash@learner.manipal.edu",
        "reg_number" : 210909230,
        "image" : images["Ayush"],
        "isAdmin" : False,
        "last_login" : time
    }
    document4 = {
        "name" : "Singhvi",
        "age" : 21,
        "email" : "aditya.singhvi@learner.manipal.edu",
        "reg_number" : 210905216,
        "image" : images["Singhvi"],
        "isAdmin" : False,
        "last_login" : time
    }
    document5 = {
        "name" : "Vikrant",
        "age" : 21,
        "email" : "vikrant.vhatkar@learner.manipal.edu",
        "reg_number" : 210909168,
        "image" : images["Vikrant"],
        "isAdmin" : False,
        "last_login" : time
    }
    document6 = {
        "name" : "Shreyansh",
        "age" : 22,
        "email" : "shreyansh.sankrit@learner.manipal.edu",
        "reg_number" : 210953352,
        "image" : images["Shreyansh"],
        "isAdmin" : False,
        "last_login" : time
    }
    document7 = {
        "name" : "Aditya",
        "age" : 21,
        "email" : "aditya.singh35@learner.manipal.edu",
        "reg_number" : 210962214,
        "image" : images["Aditya"],
        "isAdmin" : False,
        "last_login" : time
    }
    document8 = {
        "name" : "Daddyji",
        "age" : 54,
        "email" : "drsandhir@yahoo.co.in",
        "reg_number" : 164434,
        "image" : images["Daddyji"],
        "isAdmin" : False,
        "last_login" : time
    }
    document9 = {
        "name" : "Mummyji",
        "age" : 51,
        "email" : "monasandhir19@gmail.com",
        "reg_number" : 164435,
        "image" : images["Mummyji"],
        "isAdmin" : False,
        "last_login" : time
    }
    document10 = {
        "name" : "Prashar",
        "age" : 21,
        "email" : "samarth.parashar@learner.manipal.edu",
        "reg_number" : 210905206,
        "image" : images["Prashar"],
        "isAdmin" : False,
        "last_login" : time
    }

    collection.insert_many(documents = [document1, document2, document3, document4, document5, document6, document7, document8, document9, document10])