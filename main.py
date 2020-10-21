import tweepy
import random
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''

print('*** TwitterDemon is Starting *** ')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

account_names = open('accounts.txt')

account_lines = account_names.readlines()

FILE_NAME = 'last_seen_id.txt'


def retrive_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def get_user_name(n):
    user_name = account_lines[n]
    return user_name



def mybrain():
    num_lines = sum(1 for line in account_names)
    for i in num_lines:
        user_name = get_user_name(i)    # get one by one account names from account.txt
        tweets_from_user = api.user_timeline(screen_name=user_name, count=50, # scans maximum 50 tweets from an account
                                             include_rts=True,
                                             tweet_mode='extended')
        for current_tweet in tweets_from_user[:n]:  # n will be asked from console to user
            tweet_id = current_tweet.id
            if current_tweet.favorite_count > num_o_likes: # num_of_likes to be asked from console
                
                # TODO MESSAGING ALGORITHM















#def main():

   # name = get_user_name()
  #  print(name)


# main()
