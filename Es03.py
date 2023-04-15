# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:06:43 2023

@author: simone
"""
import pandas as pd


tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")

tweet_medi=tweet[['domain', 'text', 'user_id']].groupby(['domain','user_id']).count().reset_index()
tweet_medi=tweet_medi[['domain', 'text']].groupby(['domain']).mean().reset_index()

tweet_medi = tweet_medi.rename({'text': 'tweet_medi_per_utente'}, axis=1)

display(tweet_medi)