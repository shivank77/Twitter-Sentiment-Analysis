import tweepy
from textblob import TextBlob

# step 1 - Authenticate

consumer_key = '*************************'
consumer_secret = '***********************************************'

access_token = '*****************************************************'
access_token_secret = '***************************************************'

# step 2 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csv_file = open('tweet_sentiments.csv', 'w')

# Step 3 - Retrieve Tweets
public_tweets = api.search('Game of thrones')

for tweet in public_tweets:
    csv_file.write(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    result = analysis.sentiment
    result_str = '\n\n polarity ='+str(result[0])+ ' subjectivity = '+str(result[1])
    #print(result_str)
    csv_file.write(result_str)
    csv_file.write('\n\n')
