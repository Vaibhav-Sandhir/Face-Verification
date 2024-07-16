# Face Verification Project

## Introduction

This project implements a face verification system using a Siamese neural network architecture. The Siamese network is particularly well-suited for face verification tasks as it can learn to distinguish between pairs of faces, determining whether they belong to the same person or different individuals.

## Technologies Used

### Siamese Neural Network

The core of my face verification system is built upon a Siamese neural network. This architecture consists of two identical subnetworks that process two input images simultaneously. The network learns to generate embeddings for each input face, allowing for efficient comparison and verification.

### MongoDB Database

To store and manage user data efficiently, I've integrated MongoDB as my database solution. MongoDB's flexible document model allows me to store complex user information, including facial features and metadata, in a scalable and easily queryable format.

### Streamlit User Interface

For a seamless user experience, I've developed a user interface using Streamlit. This powerful Python library enables me to create an interactive and responsive web application for my face verification system. Users can easily upload images, perform verifications, and view results through this intuitive interface.

## Project Structure
The face verification pipeline in this project is divided into two main parts:

### 1. Image Capture and Face Recognition

- **Image Capture**: The process begins with capturing an image through the webcam.
- **Face Recognition**: The captured image is then passed to a pre-trained MTCNN model, which is fine-tuned for face recognition. The model identifies and extracts the face from the image, isolating it for further processing.

### 2. Face Verification

- **Siamese Neural Network**: A pre-trained ResNet18 model was used as a backbone for the Siamese Neural Network. The extracted face image is input into a Siamese neural network developed in PyTorch. The network generates embeddings for the face and compares these embeddings with those stored in the database.
- **Verification Process**: The network determines whether the face matches any registered individuals in the database, verifying the identity of the person.

### Data Storage and Retrieval

- **MongoDB**: MongoDB is used to store data about all registered individuals, including their facial embeddings and metadata. If an image is verified, the relevant data is retrieved from the database to confirm the identity of the person.

## Future Improvements

Implement Liveliness Detection to ensure security
