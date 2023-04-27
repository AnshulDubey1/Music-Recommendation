import os
import cv2
import numpy as np
from PIL import Image
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from keras.utils import load_img, img_to_array 
from keras.models import  load_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.exception import CustomException
import sys
from src.utils import write

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
model = load_model('src/pipeline/best_model.h5')
emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
transfer = []
camera = cv2.VideoCapture(0)

# load model
class CameraModule(object):
       
    def generate_frames(self):
        success, frame = camera.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
        for (x, y, w, h) in faces_detected:

            # Drawing rectangle on detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)

            # Cropping face area from  image
            roi_gray = gray_img[y:y + w, x:x + h]  
            roi_gray = cv2.resize(roi_gray, (224, 224))
            img_pixels = img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255

            # Predicting expression using cropped image
            predictions = model.predict(img_pixels)

            # Finding max indexed array
            max_index = np.argmax(predictions[0])
            predicted_emotion = emotions[max_index]
            transfer.append(str(max_index))

            # Putting text on displayed rectangles
            cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
            resized_img = cv2.resize(frame, (1000, 700))
            cv2.imshow('Facial emotion analysis ', resized_img)
            write('artifacts\Registered_emotions.txt', transfer)

        # Creating copy frames
        global last_frame1
        last_frame1 = frame.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)     
        img = Image.fromarray(last_frame1)
        img = np.array(img)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes(), success
           
   
