import os, sys
from django.db import models
from random import choice
from django.conf import settings
import tweepy
from project.settings_local import auth_settings

# Create your models here.


class FridayTweet(models.Model):
    tweet = models.CharField(max_length=140)
    tweet_created = models.DateTimeField(auto_now_add=True)
    tweet_length = models.IntegerField()

    def __unicode__(self):
        return self.tweet

    @staticmethod
    def random_line():
        with open('main/friday.txt', 'r') as friday:
            line = choice(friday.readlines())

            return line

    @staticmethod
    def bye_felicia():
        auth = tweepy.OAuthHandler(auth_settings['consumer_key'], auth_settings['consumer_secret'])
        auth.set_access_token(auth_settings['access_token_key'], auth_settings['access_token_secret'])
        api = tweepy.API(auth)

        high_today = FridayTweet.random_line()

        # tweet_different = FridayTweet.objects.filter(tweet=high_today).exists()

        tweet = FridayTweet()
        tweet.tweet = high_today
        tweet.tweet_length = len(tweet.tweet)
        tweet.save()

        api.update_status(status=high_today)
        print high_today
        print "\n\tThis tweet was %d characters long\n" % len(high_today)
