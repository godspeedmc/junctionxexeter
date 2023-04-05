# Prototype 1 

import csv
from datetime import datetime
from textblob import TextBlob
from flask import Flask, render_template, request

app = Flask('Wellbeing')

# Load the CSV file
csv_file = 'twitter_data.csv'
data = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

def analyze_sentiment(username):
    sentiment_sum = 0
    tweet_count = 0
    for row in data:
        if row['user_scr_name'] == username:
            text = row['twit_text']
            blob = TextBlob(text)
            sentiment_sum += blob.sentiment.polarity
            tweet_count += 1
    if tweet_count == 0:
        return None
    return sentiment_sum / tweet_count

def analyze_sentiment(username):
    latest_tweet = None
    latest_datetime = None
    for row in data:
        if row['user_scr_name'] == username:
            current_datetime = datetime.strptime(row['twit_created_datetime'], '%Y-%m-%d %H:%M:%S%z')
            if latest_datetime is None or current_datetime > latest_datetime:
                latest_datetime = current_datetime
                latest_tweet = row['twit_text']

    if latest_tweet is None:
        return None

    sentiment = TextBlob(latest_tweet).sentiment.polarity
    return sentiment

def get_mood_category(score):
    if -1.0 <= score < -0.6:
        return "You are likely to be depressed, please seek help from a nearby therapist"
    elif -0.6 <= score < -0.2:
        return "You are likely anxious, please breathe in and out for 1 minute with 10 second intervals"
    elif -0.2 <= score < 0:
        return "You are likely to be upset, please meditate for 5 minutes"
    elif score == 0:
        return "Nice, your mood is Neutral"
    elif 0 < score <= 0.2:
        return "Yay! it appears you are content...keep it up"
    elif 0.2 < score <= 0.6:
        return "Happy, happy, happy..."
    else:
        return "Lovely, you appear to be elated"
    

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    username = request.form["username"]
    sentiment = analyze_sentiment(username)
    if sentiment is None:
        sentiment = "No tweets found for the given username."
    else:
        mood = get_mood_category(sentiment)
        sentiment = f"Overall sentiment for {username}: {sentiment:.2f}"
    return render_template("index.html", sentiment=sentiment, mood=mood)

if 'Wellbeing' == "main":
    app.run(debug=True)



# Prototype 2

# from flask import Flask, render_template, request
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# from nltk.corpus import stopwords
# from instagramy import InstagramUser

# # Download required NLTK resoursces
# nltk.download("vader_lexicon")
# nltk.download("stopwords")

# # Define the stop words to remove from the text
# stop_words = set(stopwords.words("english"))

# # Define the sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# app = Flask('Depression')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     username = request.form['username']
#     results = analyze_user(username)
#     return render_template('index.html', results=results, username=username)

# # Define a function to analyze the sentiment of a text
# def analyze_sentiment(text):
#     # Remove stop words from the text
#     filtered_text = " ".join([word for word in text.split() if word not in stop_words])
    
#     # Analyze the sentiment of the filtered text
#     sentiment = sia.polarity_scores(filtered_text)
    
#     # Return the sentiment score
#     return sentiment["compound"]
    
# # Define a function to detect signs of depression in a social media post
# def detect_depression(post):
#     # Analyze the sentiment of the post caption
#     caption_sentiment = analyze_sentiment(post.caption)
    
#     # Analyze the sentiment of the post comments
#     comment_sentiments = [analyze_sentiment(comment.text) for comment in post.comments]
    
#     # Calculate the average sentiment score
#     avg_sentiment = (caption_sentiment + sum(comment_sentiments)) / (len(comment_sentiments) + 1)
    
#     # Check if the sentiment score is below a certain threshold
#     if avg_sentiment < -0.5:
#         return True
#     else:
#         return False

# # Define the analyze_user function to analyze a user's profile and calculate the depression score
# def analyze_user(username):
#     # Get the user's profile information using the Instagram API
#     user = InstagramUser(username)
#     media_items = user.posts
    
#     # Calculate the depression score by analyzing the sentiment of the captions and comments of the user's recent media items
#     depression_score = 0
#     for media_item in media_items:
#         if media_item.caption is not None:
#             caption_sentiment = analyze_sentiment(media_item.caption)
#             if detect_depression(media_item):
#                 depression_score += abs(caption_sentiment)
#             else:
#                 depression_score -= caption_sentiment
                
#         if media_item.comments is not None:
#             for comment in media_item.comments:
#                 comment_sentiment = analyze_sentiment(comment.text)
#                 if detect_depression(media_item):
#                     depression_score += abs(comment_sentiment)
#                 else:
#                     depression_score -= comment_sentiment
                    
#     # Determine if the user is depressed based on the depression score
#     is_depressed = False
#     if depression_score > 0.5:
#         is_depressed = True
    
#     # Return the depression score and whether the user is depressed
#     return {'depression_score': depression_score, 'is_depressed': is_depressed}

# app.run(debug=True)
