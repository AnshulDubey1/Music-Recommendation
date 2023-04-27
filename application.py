from flask import Flask, request, render_template, Response,redirect,url_for
from src.pipeline.predict_pipeline import CameraModule
from src.pipeline.song_predictor import recommender 
from src.utils import emotion_average
from src.exception import CustomException

app = Flask(__name__)

def gen(camera):
    while True:
        frame, success = camera.generate_frames()
        if not success:
            break
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cam')
def execute_camera():
    return Response(gen(CameraModule()), mimetype='multipart/x-mixed-replace;boundary=frame')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/close_cam')
def close_camera():
    emotion=emotion_average("artifacts\Registered_emotions.txt")
    return render_template('suggestion.html', songs=str(recommender(emotion)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
