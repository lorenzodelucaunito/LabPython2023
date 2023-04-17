# -*- coding: utf-8 -*-
"""

Esercizio 6: 
Calcolare quante mentions ci sono in un tweet usando la funzione get_mentions_number;
Calcolare se un tweet è un retweet (cioè se comincia con 'rt '). C
alcolare il numero medio di mentions e retweet per news, fake news e fact checking.

"""

import pandas as pd
import matplotlib.pyplot as plt
import re

def get_mention_number(text):
    return len(re.findall('@[0-9]+', text))

#Calcolo se un tweet è un retweet con il metodo startwith() della classe Stringa se inizia un testo con "rt". Esso restituisce true
# oppure false. 
def is_retweet(tweet_text):
    return tweet_text.startswith("rt")

tweet = pd.read_csv("tweets.csv") 
domini = pd.read_csv("domains.csv")

unione_df = pd.merge(tweet,domini,on="domain")



# Calcolo il numero medio di menzioni e retweet per ogni dominio usando il groupby sul dataframe:
# Credo una colonna "mentions_number" e la riempio con il numero di menzioni presenti nel testo di ogni tweet(get_mentions_number)
# La funzione apply prende una funzione come argomento e la applica a ciascun elemento della serie del df
unione_df["mentions_number"] = unione_df["text"].apply(lambda x:get_mention_number(x))


# Creazione colonna "is_retweet" e la riempie con un valore booleano richiamando la funzione(is_retweet) e viene utilizzata la funzione
# Apply per applicare la funzione a ogni riga del df nella colonna "text". 
unione_df["is_retweet"] = unione_df["text"].apply(is_retweet) 
unione_df = unione_df.rename(columns = {'mentions_number': 'Numero_di_menzioni', 'is_retweet' : 'Retweet'})

#il risultato lo salvo in un altro df e poi printo:
calcolo_df = unione_df.groupby("domain_type").agg({"Numero_di_menzioni":"mean","Retweet":"mean"})
# calcolo_df = calcolo_df.rename(columns={'mentions_number': 'Numero_di_menzioni', 'is_retweet' : 'Retweet'})
print(calcolo_df)

# G R A F I C O 

#grafico a barre che mostra la media di menzioni e retweet per tipo
media = calcolo_df.groupby("domain_type").mean()[["Numero_di_menzioni", "Retweet"]]

fig,ax = plt.subplots()
media.plot(kind = "bar", ax = ax)
plt.title("Media di menzioni e retweet per ogni tipologia di notizia",fontweight="bold")
ax.set_xlabel("Tipo di sito", fontweight = "bold")
ax.set_ylabel("Media", fontweight = "bold")
plt.tick_params(axis = 'x', labelrotation = 0)

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_06.png")

plt.show()









