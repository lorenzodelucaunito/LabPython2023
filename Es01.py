# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:19:09 2023

@author: simone
"""
import pandas as pd


tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")

tweet_dominio= tweet[['domain', 'text']].groupby(['domain']).count().reset_index()
display(tweet_dominio)

unione = tweet.merge(domini, left_on = 'domain', right_on='domain')


tweet_dominio= unione[['domain', 'text', 'domain_type']].groupby(['domain', 'domain_type']).count().reset_index()
display(tweet_dominio)

