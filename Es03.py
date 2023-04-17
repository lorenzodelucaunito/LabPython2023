# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:06:43 2023

@author: simone
"""
import pandas as pd
import matplotlib.pyplot as plt


tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")

tweet_medi=tweet[['domain', 'text', 'user_id']].groupby(['domain','user_id']).count().reset_index()
tweet_medi=tweet_medi[['domain', 'text']].groupby(['domain']).mean().reset_index()

tweet_medi = tweet_medi.rename({'text': 'tweet_medi_per_utente'}, axis=1)

tweet_medi = tweet_medi.sort_values('tweet_medi_per_utente', ascending=True)

print(tweet_medi)

# =============================================================================
#   Creazione del grafico
# =============================================================================




fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(tweet_medi['domain'], tweet_medi['tweet_medi_per_utente'])
ax.set_xlabel('Media tweet per utente')
ax.set_ylabel('Dominio')
ax.set_title('Media tweet per utente per dominio')
plt.xticks(rotation=0)

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_03.png")

plt.show()