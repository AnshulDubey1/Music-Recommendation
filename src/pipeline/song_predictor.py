from src.pipeline.predict_pipeline import camera
from src.utils import emotion_average
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from src.utils import normalize
from src.utils import string
from src.exception import CustomException
import sys
import pandas as pd
def recommender(emotion):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="12496220faa84eb39d6fdd22d53f3599",
                                                                client_secret="bc1f341b8551410c98f12d749c49fd33"))
        playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        results = sp.playlist(playlist_URI, fields='tracks,next')
        tracks=results['tracks']
        audio_features_list = []
        while tracks:
            for item in tracks['items']:
                track = item['track']
                
                # Get the audio features for the track
                audio_features = sp.audio_features(track['id'])[0]
                
                # Add the audio features to the list
                audio_features_list.append(audio_features)
            
            # Get the next page of tracks (if there is one)
            tracks = sp.next(tracks)

        # Convert the list of audio features to a Pandas DataFrame
        b = pd.DataFrame(audio_features_list)
        # Iterate over each dictionary in the list and append it to a
        b['valence']=normalize(b['valence'])
        b['energy']=normalize(b['energy'])
        b['tempo']=normalize(b['tempo'])
        b['emotional_state']=(b['tempo']+b['valence'])/2
        emotions=[]
        for val in b['emotional_state']:
            if val>0:
                emotions.append(1)
            else:
                emotions.append(0)
        b['emotion']=emotions
        extract1=b[b['emotion']==1]
        extract2=b[b['emotion']==0]
        random_row1 = extract1.sample(n=1)
        random_row2 = extract2.sample(n=1)
        track1 = sp.track(string(random_row1))
        track2 = sp.track(string(random_row2))
        if emotion==1:
            print("The recommended track name:",track1['name'],"and the artist name:",track1['artists'][0]['name'])
        else :
            print("The recommended track name:",track2['name'],"and the artist name:",track2['artists'][0]['name'])
    except Exception as e:
        raise CustomException(e,sys)
camera()
recommender(emotion_average("src\pipeline\Registered_emotions.txt"))
