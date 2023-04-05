import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

# Download required NLTK resources
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Define the stop words to remove from the text
stop_words = set(stopwords.words("english"))

# Define the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a function to analyze the sentiment of a text
def analyze_sentiment(text):
    # Remove stop words from the text
    filtered_text = " ".join([word for word in text.split() if word not in stop_words])
    
    # Analyze the sentiment of the filtered text
    sentiment = sia.polarity_scores(filtered_text)
    
    # Return the sentiment score
    return sentiment["compound"]
    
# Define a function to detect signs of depression in a social media post
def detect_depression(post):
    # Analyze the sentiment of the post caption
    caption_sentiment = analyze_sentiment(post["caption"])
    
    # Analyze the sentiment of the post comments
    comment_sentiments = [analyze_sentiment(comment["text"]) for comment in post["comments"]]
    
    # Calculate the average sentiment score
    avg_sentiment = (caption_sentiment + sum(comment_sentiments)) / (len(comment_sentiments) + 1)
    
    # Check if the sentiment score is below a certain threshold
    if avg_sentiment < -0.5:
        return True
    else:
        return False