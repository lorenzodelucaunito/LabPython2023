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

import matplotlib.pyplot as plt


plt.bar(tweet_medi['domain'], tweet_medi['tweet_medi_per_utente'])
plt.xticks(rotation=90) 
plt.xlabel('Domini',color="red",fontsize=16)
plt.ylabel('Media numeri di tweet per utente', color="red", fontsize=14)
plt.title('Media numeri di tweet degli utenti per dominio',color="red", fontweight="bold")
plt.show()
