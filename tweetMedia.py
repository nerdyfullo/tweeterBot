"""
Name: tweeterBot
Author: Zaharadeen Fakka
Date: May, 2020
Description: This program uses the Twitter API to post tweets along side media and other datas.
written in python.

NOTE: THIS IS THE FIRST WRITTEN CODE, MORE FEATURES WILL BE ADDED!.

"""

import sys, os, time
import tweepy
import requests

# Authentication with Twitter
# Provide Your App's Consumer API keys
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
# Provide Your App's Access Token & Access Token Secret
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create the API object
api = tweepy.API(auth)

# Create a new tweet
status = input()

# Select the images to be uploaded with your tweet
# in my case it's 1.png & 2.png
# feel free to rename
# NOTE: IMAGES NEED TO BE IN THE SAME FOLDER AS THE PROGRAM
filenames = ['1.jpg', '2.jpg']
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

# Send the tweet, along side the images
api.update_status(status, media_ids=media_ids)


print("Your tweet with media has been sent. check the dev in here:\nhttps://instagram.com/nerdyfullo")
input("Press any key to continue")
