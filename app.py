import streamlit as st
from verify import verify
from siamese import SiameseNetwork
from pymongo.mongo_client import MongoClient
import base64
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('MONGO_URI')
cluster = MongoClient(uri)
db = cluster["project"]
collection = db["users"]

if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'person'not in st.session_state:
    st.session_state.person = ''
if 'metadata' not in st.session_state:
    st.session_state.metadata = None

def display():
    st.header("Welcome " + st.session_state.person + "!")
    col1, col2 = st.columns(2)
    image = st.session_state.metadata["image"]
    image = base64.b64decode(image)
    col2.image(image, caption = st.session_state.person, use_column_width = True)
    for key in st.session_state.metadata.keys():
        if key == "image" or key == "_id":
            continue
        else:
            col1.markdown(f"### {key} :")
            col1.write(st.session_state.metadata[key])

def main():

    if st.session_state.page == "login":
        picture = st.camera_input("Take a picture")
        if picture:
            with open("hello.jpg", 'wb') as f:
                f.write(picture.getbuffer())
            person = verify()
            st.session_state.person = person
            st.session_state.page = "logged_in"
            st.rerun()

    elif st.session_state.page == "logged_in":
        if st.session_state.person == "None":
            st.subheader("Verification Failed")
            if st.button("Try Again", "primary"):
                st.session_state.page = "login"
                st.rerun()
        else:
            st.session_state.metadata = collection.find_one({"name" : st.session_state.person})
            if st.session_state.metadata["isAdmin"]:
                st.session_state.page = "admin"
                st.rerun()
            else:
                st.session_state.page = "user"
                st.rerun()
    
    elif st.session_state.page == "user":
        display()

    
    elif st.session_state.page == "admin":
        display()

if __name__ == "__main__":
    main()
