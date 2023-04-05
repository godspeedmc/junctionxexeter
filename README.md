# junctionxexeter
Junction Hackathon 

######################################
Prototype 1: Twitter Sentiment Analysis 
######################################

A Flask web application that performs sentiment analysis on a user's tweets and categorizes their mood based on the sentiment score. The sentiment analysis is done using TextBlob, a Python library for processing textual data.

Dependencies
To run the application, you need to have the following dependencies installed:

Python 3.x
Flask
TextBlob

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

###############################
Prototype 2: Depression Detector
###############################

A prototype application that analyzes a user's social media activity to detect signs of depression. The application uses the Instagram API to gather the user's recent media items, and then analyzes the sentiment of the captions and comments of those items to calculate a depression score. If the depression score is above a certain threshold, the application determines that the user might be depressed.

Build Instructions
To build and run the Depression Detector application, you will need to follow these steps:

1.Clone the repository to your local machine.
2.Install the required dependencies by running the following command in your terminal:

pip install -r requirements.txt

3.Obtain an access token from the Instagram API. You can do this by following the steps outlined in the Instagram API documentation.
4.Replace the ACCESS_TOKEN variable in app.py with your access token.
5.Run the application by executing the following command in your terminal:

python app.py

6. Open your web browser and navigate to http://localhost:5000/ to use the Depression Detector application.

Dependencies

The following dependencies are required to run the Depression Detector application:

Flask==2.1.2
instagramy==4.4.2
nltk==3.6.3

The required dependencies can be installed by running the following command in your terminal

pip install -r requirements.txt

Please note that this application was last tested with Python 3.9.6.




