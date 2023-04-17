#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:58:00 2023

@author: jimmywhite

Esercizio 09

La funzione extract_hashtags estrae tutti gli hashtags contenuti in un testo. 
Quali sono i 10 hashtag più frequenti nelle news, fake news e fact checking?

"""

import pandas as pd
import re
import matplotlib.pyplot as plt

# Definisco la funzione extract_hashtags
def extract_hashtags(text):
    return re.findall("#[a-zA-Z0-9]+", text)

# Importo i file csv
tweets = pd.read_csv('tweets.csv')
domains = pd.read_csv('domains.csv')

# Unisco i due dataset tramite un merge
tweets = tweets.merge(domains[['domain', 'domain_type']], on='domain', how='left')

# Estrae gli hashtag dal testo di ogni tweet
tweets['hashtags'] = tweets['text'].apply(lambda x: extract_hashtags(x))

# =============================================================================
# Provo a stampare il dataset dopo aver richiamato la funzione che estrae gli hashtag
# print(tweets.columns)
# print(tweets.head(20))
# print("")
# print("")
# print("")
# =============================================================================

# Raggruppo i tweet per tipo di sito e conta gli hashtag
hashtags_by_type = {}
colors = ['green', 'red', 'blue']  # colori per le tre barre
for i, domain_type in enumerate(['news', 'fake news', 'fact checking']):
    tweets_of_type = tweets[tweets['domain_type'] == domain_type]
    hashtags_of_type = tweets_of_type['hashtags'].explode().dropna().tolist()
    hashtag_counts = pd.Series(hashtags_of_type).value_counts().head(10)
    hashtags_by_type[domain_type] = hashtag_counts

# Crea un grafico a barre dei 10 hashtag più frequenti per ogni tipo di sito
fig, axs = plt.subplots(1, 3, figsize=(15,5))
for i, (domain_type, hashtags) in enumerate(hashtags_by_type.items()):
    axs[i].bar(hashtags.index, hashtags.values, color=colors[i])  # coloro le barre in base all'indice
    axs[i].set_title(domain_type)
    axs[i].set_xlabel('Hashtag')
    axs[i].set_ylabel('Frequenza')
    axs[i].tick_params(axis='x', labelrotation=90)

#plt.tight_layout()
plt.savefig("Esercizio_09_01.png")
plt.show()

