from src.pipeline.song_predictor import recommender
from src.pipeline.predict_pipeline import camera
from src.utils import emotion_average
from src.exception import CustomException
import sys
def Execute():
    try:    
        camera()
        return recommender(emotion_average("src\pipeline\Registered_emotions.txt"))
    except Exception as E:
        raise CustomException(E,sys)
if __name__=="__main__":
    Execute()