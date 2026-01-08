import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download lexicon
nltk.download('vader_lexicon')

# Load data
df = pd.read_csv(
    r"D:\code alpha sentiment analysis task 4\data\amazon_reviews.csv"
)

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Sentiment function
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply classification
df['Sentiment'] = df['review'].apply(get_sentiment)

# Display classification output
pd.set_option('display.max_colwidth', 60)
df[['review', 'Sentiment']].head()
