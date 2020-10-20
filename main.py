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

account_lines = account_names.readline()

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


def main():

    for x in range(5):

        name = get_user_name(x)
        print(name)

# TODO ACCOUNT NAMES TO THE LIST
# READ BY LIST
