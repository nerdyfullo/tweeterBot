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

# Create a new reply
status = input("Type Your Reply:")

# @Username - username of who's tweet you're replying to
username = input("Type Username of who you replying to (including @ sign):")

# tweetID - ID of the tweet you're replying to
tweetId = input("Insert tweet id:")

reply = status + " " + username

api.update_status(reply, tweetId)

print("Your reply has been sent. check the dev in here:\nhttps://instagram.com/nerdyfullo")
input("Press any key to continue")
