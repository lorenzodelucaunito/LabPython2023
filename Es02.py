# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:41:33 2023

@author: simone
"""
import pandas as pd


tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")

unione = tweet.merge(domini, left_on = 'domain', right_on='domain')

utenti_unici= unione[['domain', 'user_id']].groupby(['domain']).nunique()

tweet_dominio= unione[['domain', 'text']].groupby(['domain']).count().reset_index()

merged= utenti_unici.merge(tweet_dominio, left_on = 'domain', right_on='domain')

merged = merged.rename({'user_id': 'utenti_unici'}, axis=1)
merged = merged.rename({'text': 'tweetXdominio'}, axis=1)


display(merged)   





