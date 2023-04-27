from flask import Flask, request, render_template, Response,redirect,url_for
import numpy as np
import pandas as pd
import os
from src.pipeline.integration import Execute as integration_Execute
from sklearn.preprocessing import StandardScaler
from src.pipeline.song_predictor import recommender 
from src.utils import emotion_average
from src.exception import CustomException
import sys
import cv2
from keras.models import load_model
from keras.utils import load_img, img_to_array 
import time

app = Flask(__name__)
model = load_model('src/pipeline/best_model.h5')
camera = cv2.VideoCapture(0)
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
transfer = []

def generate_frames():
    start_time = time.time()
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
            for (x, y, w, h) in faces_detected:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
                roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
                roi_gray = cv2.resize(roi_gray, (224, 224))
                img_pixels = img_to_array(roi_gray)
                img_pixels = np.expand_dims(img_pixels, axis=0)
                img_pixels /= 255
                predictions = model.predict(img_pixels)

                    # find max indexed array
                max_index = np.argmax(predictions[0])

                predicted_emotion = emotions[max_index]

                transfer.append(str(max_index))

                cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                resized_img = cv2.resize(frame, (1000, 700))
                cv2.imshow('Facial emotion analysis ', resized_img)
                with open('artifacts/Registered_emotions.txt', 'w') as f:
                    f.write('\n'.join(transfer))
            ref,buffer=cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
   

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/cam')
def execute_camera():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/close_cam')
def close_camera():
    emotion=emotion_average("artifacts\Registered_emotions.txt")
    return render_template('suggestion.html', songs=str(recommender(emotion)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
