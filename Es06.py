# -*- coding: utf-8 -*-
"""
Esercizio 6: Calcolare quante mentions ci sono in un tweet
usando la funzione get_mentions_number;
Calcolare se un tweet è un retweet (cioè se
comincia con 'rt '). Calcolare il numero medio di
mentions e retweet per news, fake news e
fact checking.
"""

import pandas as pd
import matplotlib.pyplot as plt
tweet=pd.read_csv("tweets.csv") 
domini=pd.read_csv("domains.csv")
unione_df=pd.merge(tweet,domini,on="domain")

# Definisco una funzione che ha come parametro il testo di un tweet e restituisce il numero di menzioni presenti nel testo
# del tweet. Poi divido il testo in parole e filtro solo quelle che iniziano con @ utilizzando il filter con lambda della variabile words
# Poi con return , restituisco la lunghezza della lista risultante delle menzioni
def get_mentions_number(tweet_text):
    words=tweet_text.split()  #divido il testo del tweet in parole
    
    #filer prende come argomento una funzione lambda che specifica il criterio di selezione: restituisce true se la stringa x inizia con il carattere @. Altrimenti False.
    # Dopo le aggiunge alla lista "mentions". 
    mentions=list(filter(lambda x:x.startswith("@"),words))
    
    return len(mentions)

#Calcolo se un tweet è un retweet con il metodo startwith() della classe Stringa se inizia un testo con "rt". Esso restituisce true
# oppure false. 

def is_retweet(tweet_text):
    return tweet_text.startswith("rt")

#Calcolo il numero medio di menzioni e retweet per ogni dominio usando il groupby sul dataframe:
    #credo una colonna "mentions_number" e la riempio con il numero di menzioni presenti nel testo di ogni tweet(get_mentions_number)
    #la funzione apply prende una funzione come argomento e la applica a ciascun elemento della serie del df
unione_df["mentions_number"] = unione_df["text"].apply(lambda x:get_mentions_number(x))

#Creazione colonna "is_retweet" e la riempie con un valore booleano richiamando la funzione(is_retweet) e viene utilizzata la funzione
# apply per applicare la funzione a ogni riga del df nella colonna "text". 
unione_df["is_retweet"] = unione_df["text"].apply(is_retweet) 

#il risultato lo salvo in un altro df e poi printo:
calcolo_df = unione_df.groupby("domain_type").agg({"mentions_number":"mean","is_retweet":"mean"})
print(calcolo_df)

# G R A F I C O 

#grafico a barre che mostra la media di menzioni e retweet per tipo
media=unione_df.groupby("domain_type").mean()[["mentions_number","is_retweet"]]

fig,ax=plt.subplots()
media.plot(kind="bar",ax=ax)
plt.title("Media di menzioni e retweet per ogni tipologia di notizia",fontweight="bold",color="red")
ax.set_xlabel("Tipo di sito",fontweight="bold")
ax.set_ylabel("Media",fontweight="bold")
plt.show()









