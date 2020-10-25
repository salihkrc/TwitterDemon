import tweepy
import random
import time
from time import sleep
import datetime


print('        ############       ###\n'
      '             ##            ##  ##\n'
      '             ##            ##    ##\n'
      '             ##            ##    ##\n'
      '             ##            ##  ## \n'
      '             ##            ###\n')



CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

account_names = open('accounts.txt')

account_lines = account_names.readlines()

def get_user_name(n):
    user_name = account_lines[n]
    return user_name



def scan_rt():
    print('MODE 1 is activated!\n')
    n_ = input('How many tweets you want to scan per account ? : ')
    num_likes = input('How much likes must have a tweet (min) to send a DM to user ? : ')
    n = int(n_)
    num_of_likes = int(num_likes)
    num_lines = open("accounts.txt").read().count('\n')

    print(num_lines)

    for i in range(num_lines):
        print('Now scanning tweets of the user : ')

        user_name = get_user_name(i)    # get one by one account names from account.txt
        print(user_name)
        tweets_from_user = api.user_timeline(screen_name=user_name, count=50, exclude_replies=True, include_rts=True,  # scans maximum 50 tweets from an account
                                             tweet_mode='extended')
        for current_tweet in tweets_from_user[:n]:  # n will be asked from console to user
            tweet_id = current_tweet.id
            fav_num = 0
            creation_t = 0
            try:
                fav_num = current_tweet.retweeted_status.favorite_count
                creation_t = current_tweet.retweeted_status.created_at
            except:
                print('Found Tweet Which Is Not a RT!')
                print('Skipping....')


            if fav_num >= num_of_likes and ((datetime.datetime.now() - creation_t).days <= 2)  :  # num_of_likes to be asked from console
                print('-----------------------------------------------------------------')
                print('%%%%% Tweet With Criteria FOUND! %%%%%\n')
                print('ID OF TWEET: ')
                print(current_tweet.retweeted_status.id)
                print("Tweet's Content : ")
                print(current_tweet.retweeted_status.full_text)
                print('Number of Favs: ')
                print(current_tweet.retweeted_status.favorite_count)
                try:
                    api.create_favorite(current_tweet.retweeted_status.id) # likes the tweet
                except:
                    print("Already Favorited this tweet")
                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                c_user = current_tweet.retweeted_status.user
                c_user_id = c_user.id
                msg_file = open('message.txt', mode='r')  # TODO create message.txt
                message = msg_file.read()
                msg_file.close()


                try:

                    direct_msg = api.send_direct_message(c_user_id, message)
                    print('Message Sent to the user!')
                    print(c_user_id)
                    print('-----------------------------------------------------------------')
                    sleep(300)
                except:
                    print('This User did not accept DMs!')
                    print('-----------------------------------------------------------------')


def get_top():
    print('MODE 2 is activated!\n')
    keyword = input('Please type the keyword to search for : ')
    t_tweets = api.search(q=keyword, result_type='popular', tweet_mode='extended')
    t_user = t_tweets[0].user
    print(t_user.screen_name)
    print(len(t_tweets))









while True:
    print('############################ BEFORE WE START PLEASE GIVE ME SOME DETAILS #####################\n')
    mode_select = input('Please SELECT the Mode of Program :\n '
                        '1. Scan for RT from accounts\n'
                        '2. Get top trending Tweet\ns'
                        'Please Type 1 or 2 : ')
    sleep(3)
    print('Initializing the connection...')
    sleep(5)

    print('*** TwitterDemon is Starting *** ')

    if mode_select == '1':

         scan_rt()
    elif mode_select == '2':

        get_top()
    else:
        print('Wrong Selection')

