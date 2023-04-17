#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:27:32 2023

@author: jimmywhite

Esercizio 08

La funzione get_mentions_number (pagina precedente) calcolare quali sono i 100 
utenti che fanno più mentions. 
C’è correlazione fra il loro numero di mentions e il loro numero di tweet scritti?

"""

import pandas as pd
import re
import matplotlib.pyplot as plt

# Definisco la funzione get_mention_number
def get_mention_number(text):
    return len(re.findall('@[0-9]+', text))

# Importo i file .csv
tweets = pd.read_csv('tweets.csv')
domains = pd.read_csv('domains.csv')

# Faccio il merge delle due tabelle
merged_df = pd.merge(tweets, domains, on='domain')

# Calcolo del numero di mentions per ogni tweet
merged_df['mentions'] = merged_df['text'].apply(get_mention_number)


# Raggruppamento dei tweet per user_id e calcolo del numero di tweet e di mentions per ogni utente
groupped_df = merged_df.groupby('user_id').agg({'mentions': 'sum', 'text': 'count'})

# Selezione dei primi 100 utenti per numero di mentions
sorted_df = groupped_df.sort_values(by ='mentions', ascending = False)
top_users_df = sorted_df.head(100)


# Plot del numero di mentions rispetto al numero di tweet scritti per ogni utente
cmp = plt.get_cmap('viridis')
plt.scatter(top_users_df['text'], top_users_df['mentions'], c=top_users_df['mentions'], cmap=cmp)
plt.xlabel('Numero di tweet')
plt.ylabel('Numero di mentions')
plt.show()


# Tramite la funzione 'corr' di Pandas, calcoliamo il coefficiente di correlazione di Pearson tra le due variabili.
# Il coefficiente di correlazione varia tra -1 e 1, dove 
# -1 indica una forte correlazione negativa,
# 0 indica una mancanza di correlazione, 
# e 1 indica una forte correlazione positiva.
corr = top_users_df['mentions'].corr(top_users_df['text'])
print('Il coefficiente di correlazione tra mentions e text è:', round(corr, 2))
print("Ovvero gli utenti che scrivono piu tweets tendono anche a fare piu mentions")


# =============================================================================
# La funzione get_mention_number utilizza la libreria re di Python per 
# cercare tutte le mentions presenti nel testo, utilizzando una espressione regolare. 
# In particolare, la funzione cerca tutte le stringhe che iniziano con il simbolo @, 
# seguito da uno o più numeri, utilizzando la seguente espressione regolare: @[0-9]+.
# =============================================================================
