from flask import Flask, request, render_template, Response,redirect,url_for
from src.pipeline.predict_pipeline import CameraModule
from src.pipeline.song_predictor import recommender 
from src.utils import emotion_average
from src.exception import CustomException
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="12496220faa84eb39d6fdd22d53f3599",
                                                                client_secret="bc1f341b8551410c98f12d749c49fd33")) 

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
    songs=sp.track(recommender(emotion))
    return render_template('suggestion.html', track=songs)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
