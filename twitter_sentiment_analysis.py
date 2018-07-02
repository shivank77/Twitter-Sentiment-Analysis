import tweepy
from textblob import TextBlob

# step 1 - Authenticate

consumer_key = '4ambeecTTMwHJu3JrTiWMzuId'
consumer_secret = 'YTtC9UL7emmdlAXPfCncgEnNTrY6ghIueYSHMJp7B0oewkB28T'

access_token = '795625002691391488-JgNFl4tYSDMFhDPLlNAgRI9pz2OqUZs'
access_token_secret = 'JaL6fePHPQt0fqTIx7OP7Envr92ZWFGNLuBt1yaQY7awH'

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