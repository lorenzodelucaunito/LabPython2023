# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:19:09 2023

@author: simone

Esercizio 01

Calcolare il numero di tweet per dominio. 
C'è un modo per mostrare anche il tipo del dominio nello stesso plot?

"""

import pandas as pd
import matplotlib.pyplot as plt

# Importo li dati su cui lavorare
tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")


tweet_dominio= tweet[['domain', 'text']].groupby(['domain']).count().reset_index()

unione = tweet.merge(domini, left_on = 'domain', right_on='domain')

tweet_dominio= unione[['domain', 'text', 'domain_type']].groupby(['domain', 'domain_type']).count().reset_index()

# Riassegno il nome della colonna che contiene il numero di tweet
tweet_dominio = tweet_dominio.rename(columns={'text': 'numero_di_tweet'})

# Ordino il dataset per numero di tweet crescente
tweet_dominio = tweet_dominio.sort_values('numero_di_tweet') 

print(tweet_dominio)

# =============================================================================
#     Creazione del grafico
# =============================================================================

# Imposto i valori del padding per i sottografici
padding_top = 1.2       # Padding superiore
padding_middle = 2     # Padding tra il primo e secondo grafico
padding_bottom = 3   # Padding inferiore

# Creo una Figure con 3 Axes, uno sotto l'altro
fig, axs = plt.subplots(nrows = 3, 
                        ncols = 1, 
                        figsize = (10, 15))

# Imposto il primo padding
#fig.subplots_adjust(hspace=padding_top)

# Creo il grafico per le fake news
axs[0].bar(tweet_dominio[tweet_dominio['domain_type'] == 'fake news'].domain,
           tweet_dominio[tweet_dominio['domain_type'] == 'fake news'].numero_di_tweet,
           color = 'red')
axs[0].set_title('Fake News')
axs[0].tick_params(axis = 'x', labelrotation = 90)
# Imposto una scala logaritmica sull'asse delle y per migliorare la leggibilità del grafico
axs[0].set_yscale('log')


# Imposto il secondo padding
#fig.subplots_adjust(hspace=padding_middle)

# Creo il grafico per le news
axs[1].bar(tweet_dominio[tweet_dominio['domain_type'] == 'news'].domain,
           tweet_dominio[tweet_dominio['domain_type'] == 'news'].numero_di_tweet,
           color = 'Green')
axs[1].set_title('News')
axs[1].tick_params(axis = 'x', labelrotation = 90)

# Imposto il terzo padding
#fig.subplots_adjust(hspace=padding_bottom)

# Creo il grafico per il fact checjing
axs[2].bar(tweet_dominio[tweet_dominio['domain_type'] == 'fact checking'].domain,
           tweet_dominio[tweet_dominio['domain_type'] == 'fact checking'].numero_di_tweet,
           color = 'Blue')
axs[2].set_title('Fact Checking')
#axs[2].tick_params(axis = 'x', labelrotation = -75)

# Aggiungo il titolo globale
fig.suptitle('Tweet per dominio', fontsize = 14)

# Aggiungo del padding tra gli axes per evitare la sovrapposizione con le etichette dell'asse x
fig.subplots_adjust(hspace=(0.8, 3, 1))

plt.ylabel('Numero di tweet')

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_01.png")

# Mostro il grafico
plt.show()