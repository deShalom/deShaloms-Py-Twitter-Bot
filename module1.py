import tweepy
import time
import schedule
from module2 import collectTweet

print("Debug - Launched")

#----Jays Keys!
#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#ACCESS_KEY = ''
#ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#----Collects the last thirty @'s from the users timeline.
mentions = api.mentions_timeline()

#----Collects all dm's.
#dms = api.list_direct_messages()
#print(dms[0].__dict__.keys())
#----Returns content of the DM.
#print(dms[0].message_create['message_data']['text'])

#Testing Schedual library
def job():
    print(collectTweet())
    api.update_status(collectTweet())
    print("Debug - Tweeted")
    
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("05:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
