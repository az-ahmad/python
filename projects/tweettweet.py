import tweepy
import time
import json

auth = tweepy.OAuthHandler('xxxxx', 'xxxxx')
auth.set_access_token('xxxx-xxxx', 'xxxxxx')

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        stuff = api.user_timeline(id = tweet.user.id, count = 100, include_rts = False)
        timeHour = 0
        timeMinute = 0
        timeSecond = 0
        tweetCount = 0
        for status in stuff:
            # print(status.text)
            date = str(status.created_at)[-8:]
            # print(date)
            tweetCount += 1
            timeHour += int(date[:2])
            timeMinute += int(date[3:5])
            timeSecond += int(date[6:])
        hour = int(timeHour/tweetCount)
        minute = int(timeMinute/tweetCount)
        second = int(timeSecond/tweetCount)
        avgTweetTime = f'{hour}:{minute}:{second}'

        
            

        tweet.favorite()
        api.update_status(f'@{tweet.user.screen_name} Thank you for tweeting me.\nYour average time of tweeting your last 20 tweets is {avgTweetTime}.\nI am an automated bot built by Aziz.', tweet.id)

    def on_error(self, status):
        print("Error detected")



api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
user = api.me()
public_tweets = api.home_timeline()

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["@aziz_bot_"], languages=["en"])

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)







# for tweet in tweepy.Cursor(api.search, q='brackets', count=5, result_type="recent", include_entities=True, lang="en").items(1):
#     try:
#         print(tweet.user.screen_name)
#         print(tweet.text)
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break




# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Sixth Form':
#         follower.follow()
#         break