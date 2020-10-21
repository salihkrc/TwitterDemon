import tweepy
import random
from time import sleep

print('############################ BEFORE WE START PLEASE GIVE ME SOME DETAILS #####################\n')
print('\n')
sleep(3)
# CONSUMER_KEY = input('Please give your CONSUMER_KEY: ')
# CONSUMER_SECRET = input('Please give your CONSUMER_SECRET: ')
# ACCESS_KEY = input('Please give your ACCESS_KEY: ')
# ACCESS_SECRET = input('Please give your ACCESS_SECRET: ')
n_ = int

n_ = input('How many tweets you want to scan per account ? : ')
num_likes = input('How much likes must have a tweet (min) to send a DM to user ? : ')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''
print('Initializing the connection...')
sleep(5)


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


def my_brain():
    print('1')
    n = n_
    num_of_likes = num_likes
    num_lines = len(account_names.readlines())
    print(num_lines)
    for i in range(2):
        print('2')
        user_name = get_user_name(i)    # get one by one account names from account.txt
        tweets_from_user = api.user_timeline(screen_name=user_name, count=50,  # scans maximum 50 tweets from an account
                                             tweet_mode='extended')
        for current_tweet in tweets_from_user[:10]:  # n will be asked from console to user
            tweet_id = current_tweet.id
            if current_tweet.favorite_count >= 10 :  # num_of_likes to be asked from console
                print('3')
                c_user = current_tweet.user
                c_user_id = c_user.id
                msg_file = open('message.txt', mode='r')  # TODO create message.txt
                message = msg_file.read()
                msg_file.close()
                direct_msg = api.send_direct_message(c_user_id, message)



my_brain()











#def main():

   # name = get_user_name()
  #  print(name)


# main()
