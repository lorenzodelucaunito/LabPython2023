#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Si vuole analizzare il tipo di siti web maggiormente condivisi ad ogni mese,
e capire se ci siano correlazione tra il mese corrispondente e la condivisione dei
domini tra i tweet che contengono link a siti di "news" e quelli che contengono link a siti di "fake news" e "fact checking".
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime

tweets = pd.read_csv("tweets.csv")
domains = pd.read_csv("domains.csv")

tweets['giorno'] = pd.to_datetime(tweets['date']).dt.day

settimana = ["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"]

riferimento = datetime.date(2019, 8, 1)

#Trasforma il numero del giorno nel giorno corrispettivo della settimana
def giorno_settimana(giorno):
    delta = datetime.timedelta(days=giorno-1)
    data = riferimento + delta
    return settimana[data.weekday()]

tweets['giorno_settimana'] = tweets['giorno'].apply(lambda x: giorno_settimana(x))

merged = pd.merge(tweets,domains,
                  left_on = 'domain', right_on = 'domain')


grouped = merged.groupby(['giorno_settimana', 'domain_type'])['giorno_settimana'].count().unstack('domain_type')

fig, ax = plt.subplots(figsize=(8, 6))

colors = { 'fact checking':'#377eb8','fake news':'#b83737','News':'#4daf4a'}

grouped.plot(kind='bar', ax=ax, width=0.8, edgecolor='white', linewidth=1.5, color=colors.values())

ax.legend(['Fact checking', 'Fake news', 'News'])

ax.set_xticklabels(settimana)
ax.set_xlabel('Giorno della settimana')
ax.set_ylabel('Numero di tweet')

plt.show()



