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


config_file = open('config.txt')
configs = config_file.readlines()



CONSUMER_KEY = configs[0].rstrip()
CONSUMER_SECRET = configs[1].rstrip()

ACCESS_KEY = configs[2].rstrip()
ACCESS_SECRET = configs[3].rstrip()


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
    num_likes = input('How many likes must have a tweet (min) to send a DM to user ? : ')
    n = int(n_)
    num_of_likes = int(num_likes)
    num_lines = open("accounts.txt").read().count('\n')

    #print(num_lines)

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
                print('\n')
                print('%%%%% Tweet With Criteria FOUND! %%%%%\n')
                print('ID OF TWEET: ')
                print(current_tweet.retweeted_status.id)
                print("Tweet's Content : ")
                print(current_tweet.retweeted_status.full_text)
                print('Number of Favs: ')
                print(current_tweet.retweeted_status.favorite_count)

                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                c_user = current_tweet.retweeted_status.user
                c_user_name = c_user.screen_name
                c_user_id = c_user.id
                msg_file = open('message.txt', mode='r')  # TODO create message.txt
                message = msg_file.read()
                msg_file.close()
                try:
                    api.send_direct_message(c_user_id, message)
                    print('Message Sent to the user!')
                    print(c_user_name)
                    try:
                        api.create_favorite(current_tweet.retweeted_status.id)  # likes the tweet
                    except:
                        print("Already Favorited this tweet")
                    print('-----------------------------------------------------------------')
                    sleep(300)
                except:
                    print('This User did not accept DMs!')
                    print('-----------------------------------------------------------------')


def get_top():
    print('MODE 2 is activated!\n')
    keyw = input('Please give a keyword : ')
    topn = input('Please Declare Top N tweets, N = ? : ')
    topn = int(topn)
    num_likes = input('How many likes must have a tweet (min) to send a DM to user ? : ')
    num_of_likes = int(num_likes)

    for tweet in tweepy.Cursor(api.search, q=keyw, result_type='popular').items(topn):
        fav_num = 0
        creation_t = 0
        try:
            fav_num = tweet.favorite_count
            creation_t = tweet.created_at
        except:
            print('Found Tweet Which Is Not a RT!')
            print('Skipping....')

        if fav_num >= num_of_likes and (
                (datetime.datetime.now() - creation_t).days <= 2):  # num_of_likes to be asked from console
            print('\n')
            print('%%%%% Tweet With Criteria FOUND! %%%%%\n')
            print('ID OF TWEET: ')
            print(tweet.id)
            #print("Tweet's Content : ")
            #print(tweet.full_text)
            print('Number of Favs: ')
            print(tweet.favorite_count)

            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            c_user = tweet.user
            c_user_name = c_user.screen_name
            c_user_id = c_user.id
            msg_file = open('message.txt', mode='r')
            message = msg_file.read()
            msg_file.close()
            try:
                api.send_direct_message(c_user_id, message)
                print('Message Sent to the user!')
                print(c_user_name)
                try:
                    api.create_favorite(tweet.id)  # likes the tweet
                except:
                    print("Already Favorited this tweet")
                print('-----------------------------------------------------------------')
                sleep(300)
            except:
                print('This User did not accept DMs!')
                print('-----------------------------------------------------------------')














while True:
    print('############################ BEFORE WE START PLEASE GIVE ME SOME DETAILS #####################\n')
    mode_select = input('Please SELECT the Mode of Program :\n '
                        '1. Scan for RT from accounts\n'
                        '2. Get top trending Tweets\n'
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



