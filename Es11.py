#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import delle librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# lettura dei dati dai file csv
tweets = pd.read_csv("tweets.csv")
domains = pd.read_csv("domains.csv")

# creazione della colonna 'giorno' contenente il giorno del mese a cui si riferisce il tweet
tweets['giorno'] = pd.to_datetime(tweets['date']).dt.day

# creazione della lista dei giorni della settimana
settimana = ["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"]

# definizione della data di riferimento per il calcolo del giorno della settimana
riferimento = datetime.date(2019, 8, 1)

# funzione che restituisce il giorno della settimana a partire dal numero del giorno del mese
def giorno_settimana(giorno):
    delta = datetime.timedelta(days=giorno-1)
    data = riferimento + delta
    return settimana[data.weekday()]

# creazione della colonna 'giorno_settimana' contenente il giorno della settimana a cui si riferisce il tweet
tweets['giorno_settimana'] = tweets['giorno'].apply(lambda x: giorno_settimana(x))

# unione dei dataframe 'tweets' e 'domains' in base alla colonna 'domain'
merged = pd.merge(tweets, domains, left_on='domain', right_on='domain')

# raggruppamento dei tweet per giorno della settimana e tipo di dominio, e conteggio dei tweet per ogni gruppo
grouped = merged.groupby(['giorno_settimana', 'domain_type'])['giorno_settimana'].count().unstack('domain_type')

# definizione dei colori per i tipi di dominio
colors = {'fact checking': 'blue', 'fake news': 'red', 'news': 'green'}

# creazione della figura con 3 subplot
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))

# ciclo sui tipi di dominio, creazione del grafico a barre corrispondente e impostazione dei parametri dell'asse x e del titolo
for i, domain_type in enumerate(grouped.columns):
    grouped[domain_type].plot(kind='bar', ax=axes[i], width=0.8, edgecolor='white', linewidth=1.5, color=colors[domain_type])
    axes[i].set_xticklabels(settimana)
    axes[i].set_xlabel('Giorno della settimana')
    axes[i].set_ylabel('Numero di tweet')
    axes[i].set_title(domain_type)
    axes[i].legend().set_visible(False)

# ridimensionamento dei subplot per evitare sovrapposizioni
plt.tight_layout()

# visualizzazione del grafico
plt.show()
