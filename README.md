# G-Minor: A music recommendation system

Music is a part of the daily lives of the current generation. But sometimes, it becomes difficult to calm the mind and think of that one song that can help the most on times of need. With G-Minor, we aim to eliminate that doubt. G-minor uses the fundamentals of image processing and computer vision to capture frames from a user’s video input, analyze their facial expression and suggest a song based on the same from Spotify’s top playlists. This is an end to end project which uses an industrial level documentation format and covers many aspects from the making to the deployment of a website.


# Features: 

* `Data preprocessing` : The project preprocesses data from the Million Song Dataset, which is a large, freely-available dataset of audio features and metadata for a million songs.
* `Feature engineering` : The project extracts audio features from the dataset such as tempo, key, and mode, and creates a feature vector for each song.
* `Content-based filtering`: The project also uses content-based filtering techniques to recommend songs based on audio features.
* `User interface`: The project has a web-based user interface that allows users to input their preferences and receive music recommendations.
* `Technology stack`: The project is written in Python and uses various libraries such as NumPy, Pandas, Flask, and Scikit-learn.


# Webpage components:

* `Home page`: This page represents us and our role in the making of this project.
* `Side navbar`: This page enables the user to navigate to different sectionns of the website.
* `Emotion analysis page` : This page prompts the user's camera and captures their live video feed. It has a predict button which redirects you to the following page.
* `Suggestions page`: This page suggests a song based on the detected mood.
* `Error page` : This page is designed for handling unexpected errors. It gives an error message and image and redirects the user back to the home page.


# Screenshot of UI

<img src="screenshots\1.png" alt="Homepage"/>
<img src="screenshots\2.jpg" alt="Navbar"/>
<img src="screenshots\3.jpg" alt="Camera"/>
<img src="screenshots\4.jpg" alt="Suggestions"/>
<img src="screenshots\5.jpg" alt="Error"/>


# Approach for the data analysis 

1. Importing Pre-Requisite Modules:
    * The first step is to import all the necessary modules and libraries required for the project. This includes data analysis and visualization tools like Pandas, NumPy, Matplotlib, and Seaborn. Additionally, we also import the Spotipy library, which allows us to connect to the Spotify API and extract data from the platform.

2. Reading the Data:
    * The next step is to read the data from the dataset. We have used Pandas to read the CSV files. We need to ensure that the data is loaded correctly, and there are no issues with data types or formatting.

3. Data Cleaning:
    * Data cleaning is a critical step in any data science project. In this step, we identify the features that are relevant to our analysis and remove any missing or null values. We also need to split the data into numerical and categorical values to perform appropriate transformations. Additionally, we also perform data visualization to find correlations between features and to identify any outliers in the data.

4. Data Transformation:
    * The next step is data transformation, where we perform normalization of data to ensure that all features have the same scale. This step is crucial when we are working with machine learning models as it can affect the performance of the model.

5. Prediction:
    * Once the data is cleaned and transformed, we can then proceed with building machine learning models to make predictions. In this project, we use random sampling to generate recommendations for Spotify users based on their listening history.
    * In this step, we use the Spotipy library to connect to the Spotify API and extract data from the platform. This allows us to access user data and perform data analysis to generate recommendations.


# Exploratory Data Analysis 

Link : [EDA Notebook](notebook\suggestion.ipynb)


# Dependencies

* Python 3.8 or higher
* Scikit-learn
* Pandas 
* Numpy
* Tensorflow
* Seaborn
* Matplotlib
* Dill
* Pymongo
* Ipykernel
* Spotipy
* Opencv-python
* Flask
* Pillow

Please make sure to install these dependencies using pip or any other package manager before running the project.


# Usage

Install the required dependencies using "pip install requirements.txt".
Clone the repository using git clone https://github.com/AnshulDubey1/Music-Recommendation.git
Navigate to the project directory using cd <Music-Recommendation>.
Run the application.py script using "python application.py"
Open your web browser and input your local host adress with a /8000.
This would take you to the home page. 
Click on the "Music Recommendation System" bar on the top OR click on the side navbar menu and click on "Camera".
You will be redirected to the Emotion recognition page.
Wait for the emotions to register and then click on "Predict"
You will be redirected to the suggestion page which suggests a song to you.


# Conclusion

The Music Recommendation project aims to provide users with personalized music recommendations based on their mood and expression. The system would be be able to handle a large number of concurrent users, provide recommendations in real-time and have a user-friendly interface. This project can be used by the general public to enhance their listening experience by enabling them to discover new songs that match their mood.