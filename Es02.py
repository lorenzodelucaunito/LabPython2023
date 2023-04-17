# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:41:33 2023

@author: simone

Esercizio 02:
    
    Calcolare il numero di utenti unici che twittano ciascun dominio.
    Confrontarlo con i valori precedenti.
    
"""
import pandas as pd
import matplotlib.pyplot as plt

# Carica i dati dai file CSV
tweet= pd.read_csv("tweets.csv")
domini= pd.read_csv("domains.csv")

unione = tweet.merge(domini, left_on = 'domain', right_on = 'domain')

utenti_unici= unione[['domain', 'user_id']].groupby(['domain']).nunique()

tweet_dominio= unione[['domain', 'text']].groupby(['domain']).count().reset_index()

merged= utenti_unici.merge(tweet_dominio, left_on = 'domain', right_on='domain')

# Cambio nome delle colonne con nomi piu evocativi
merged = merged.rename({'user_id': 'utenti_unici'}, axis = 1)
merged = merged.rename({'text': 'tweetXdominio'}, axis = 1)

# Riordino i dati in base al numero di utenti unici
merged = merged.sort_values('utenti_unici')

# Stampo i dati a video
print(merged)   


# =============================================================================
#   Creazione del grafico
# =============================================================================


# Crea una figura con due assi
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (20, 25))

# Crea un grafico a barre per gli utenti unici
ax1.bar(merged['domain'], 
        merged['utenti_unici'],
        color = 'purple')
ax1.set_title('Utenti unici per dominio', weight = 'bold')
ax1.set_ylabel('Numero di utenti unici', weight = 'bold')
ax1.tick_params(axis = 'x', labelrotation = 90)
# Rendo la scala logaritmica per aumentarne la leggibilità
ax1.set_yscale('log')

# Crea un grafico a barre per i tweet per dominio
ax2.bar(merged['domain'], 
        merged['tweetXdominio'],
        color = 'orange')
ax2.set_title('Tweet per dominio', weight = 'bold')
ax2.set_xlabel('Dominio', weight = 'bold')
ax2.set_ylabel('Numero di tweet', weight = 'bold')
ax2.tick_params(axis = 'x', labelrotation = 90)
# Rendo la scala logaritmica per aumentarne la leggibilità
ax2.set_yscale('log')

# Aggiungo del padding tra gli axes per evitare la sovrapposizione con le etichette dell'asse x
fig.subplots_adjust(hspace = 0.5)

# Evito l'overlap dei subplots
# plt.tight_layout()

# Aggiungo il titolo globale
fig.suptitle('Utenti unici per dominio', fontsize = 20, weight = 'bold')

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_02.png")

# Mostro il grafico
plt.show()


