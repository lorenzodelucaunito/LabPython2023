#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:42:59 2023

@author: jimmywhite

Esercizio 07 

A che ore vengono pubblicate più news, senza contare i minuti? E le fake news?

"""

import pandas as pd
import matplotlib.pyplot as plt

# Carica i dataset
tweets = pd.read_csv("tweets.csv")
domains = pd.read_csv("domains.csv")

# Effettua il merge delle due tabelle
merged_table = pd.merge(domains, tweets, on = "domain")

# Assegna ad una nuova colonna 'hour' il valore dell'ora presente in 
# 'date', rappresentata dallo slice nelle posizioni 11 e 13
merged_table['hour'] = merged_table['date'].str.slice(11, 13)

# Tramite il broadcasting assegna una nuova colonna che contiene il valore "1".
# Questa colonna verrà usata come contatore.
merged_table['my_variable_for_counter'] = 1

# Raggruppa i dati in base all'ora del giorno e al tipo di sito (news o fake news)
my_counter = merged_table[['domain_type', 'hour', 'my_variable_for_counter']].groupby(['domain_type', 'hour']).count().reset_index()

# Estrae i conteggi relativi alle news e alle fake news
news_counts = my_counter[my_counter['domain_type'] == 'news']
fake_news_counts = my_counter[my_counter['domain_type'] == 'fake news']

# Trova l'ora con il conteggio più alto per le news e per le fake news
max_news_hour = news_counts.loc[news_counts['my_variable_for_counter'].idxmax()]['hour']
max_fake_hour = fake_news_counts.loc[fake_news_counts['my_variable_for_counter'].idxmax()]['hour']
print("L'ora in cui vengono pubblicate più news è:", max_news_hour)
print("L'ora in cui vengono pubblicate più fake news è:", max_fake_hour)

# Stampo il numero piu piccolo dei due dataset per poi impostare la scale del grafico:
# print(news_counts.min())
# print(fake_news_counts.min())


# Crea un dataframe con i conteggi delle news e delle fake news in base all'ora del giorno
df = my_counter.pivot(index='hour', columns='domain_type', values='my_variable_for_counter') 

#1

# Rimuovi la riga corrispondente a "fact checking" dal dataframe df
# df = df.drop(index='fact checking')
del df['fact checking']

# Crea un grafico a barre che mostri i conteggi per ogni ora del giorno
ax = df.plot.bar()

#2

# Imposta il titolo del grafico
plt.title("Tweets per ora")

# Imposta le etichette degli assi
plt.xlabel("Ora")
plt.ylabel("Numero di Tweets")

# Mostra il grafico
plt.show()
