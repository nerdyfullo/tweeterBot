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
status = input()

# @Username - username of who's tweet you're replying to
username = input()

# tweetID - ID of the tweet you're replying to
tweetId = input("Insert tweet id:")

api.update_status(status, '@'username, tweetId)
