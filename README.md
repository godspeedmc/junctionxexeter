# junctionxexeter
Junction Hackathon 

use index.html and app.py for both demo

Prototype 1: Twitter Sentiment Analysis 

Dataset:
https://drive.google.com/file/d/1O2zefrFPhbmNI7OGRjvo12IDzJ4HWEnh/view?usp=sharing


A Flask web application that performs sentiment analysis on a user's tweets and categorizes their mood based on the sentiment score. The sentiment analysis is done using TextBlob, a Python library for processing textual data.

Dependencies
To run the application, you need to have the following dependencies installed:

-Python 3.x
-Flask
-TextBlob

You can install Flask and TextBlob by running the following commands in your terminal:

pip install Flask
pip install textblob

Build Instructions
To run the application, follow these steps:

1.Clone the repository to your local machine.
2.Navigate to the root directory of the project in your terminal.
3.Run the following command to start the Flask server:

python app.py

4.Open your web browser and go to http://localhost:5000/ to access the web application

How to Use

Enter a Twitter username in the input field and click the "Analyze" button.
The application will perform sentiment analysis on the user's tweets and display the overall sentiment score.
The mood category will also be displayed based on the sentiment score.

Future Work

Improve the accuracy of sentiment analysis by using more advanced techniques such as deep learning.
Expand the application to work with multiple social media platforms.
Add more features such as data visualization and user authentication.

##
Prototype 2: Depression Detector

This is a prototype for a Depression Detector application that analyzes an Instagram user's recent media items and comments to determine if they might be depressed.

Dependencies

This application requires the following dependencies to be installed:

Flask
nltk
Instagramy

You can install these dependencies by running the following command:

pip install flask nltk instagramy

Build Instructions

To run this application, follow these steps:
1. Clone the repository
2. Navigate to the project directory
3. Start the Flask server:(python app.py)
4. Open your web browser and go to http://localhost:5000.
5. Enter an Instagram username in the form and click the "Analyze" button to see the depression score and whether the user might be depressed.

Note: You will need to obtain an Instagram API access token and add it to the app.py file to use this application. Instructions for obtaining an access token can be found on the Instagram Developer website.










