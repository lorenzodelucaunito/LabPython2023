# -*- coding: utf-8 -*-
"""
Esercizio 4 di Fake News
"""
import pandas as pd
import matplotlib.pyplot as plt

tweet = pd.read_csv("tweets.csv") 
domini = pd.read_csv("domains.csv")

#Unisco i due dataset
merged_df = pd.merge(tweet,domini,on="domain")

unione_df = merged_df.rename(columns={"domain_type":"Tipo di dominio"})

#Calcolare il numero di articoli unici per tipo usando groupby
domini_unici = unione_df.groupby("Tipo di dominio")["domain"].nunique() #nunique  restituisce i valori unici in una colonna

#Calcolo il numero di tweet per tipo di dominio
tweet_type = unione_df.groupby("Tipo di dominio")["text"].count()

#Definisco una variabile che racchiuda il totale dei domini
totDomini = domini["domain"].nunique()

#Calcolo la proporzione di articoli unici per dominio e printo
articoliProp = domini_unici / totDomini
print("Articoli unici per tipo di dominio:")
print("\n")
print(articoliProp)

#Definisco una variabile che racchiuda il numero totale di Tweet
totTweet = tweet["text"].count()
#Calcolo la proporzione e printo
tweetProp = tweet_type/totTweet
print("\nLa proporzione di tweet per tipo di dominio è:")
print("\n")
print(tweetProp) 


# G R A F I C O

# Set colors
colors = ['blue', 'red', 'green']

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Grafico 1
articoliProp.plot(kind="pie", ax=ax1, colors=colors, autopct='%1.1f%%')
ax1.set_title("Proporzione di articoli unici per tipo di dominio", fontweight="bold")

ax1.set_xlabel("") # Rimuove la label sull'asse x

# Grafico 2
tweetProp.plot(kind="pie", ax=ax2, colors=colors, autopct='%1.1f%%') 
ax2.set_title("Proporzione di tweet per tipo di dominio", fontweight="bold")
ax2.set_xlabel("") # Rimuove la label sull'asse x

# Crea la legenda
#ax1.legend(labels=articoliProp.index, loc="upper right")
#pie2 = tweetProp.plot(kind="pie",ax=ax2, colors=["blue","red","green"])
ax2.legend(bbox_to_anchor=(1.1,1),title="Tipo di dominio",labelspacing=0.5)
#ax2.legend(labels=tweetProp.index, loc="upper right")
ax1.axis("off")
ax2.axis("off")

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_04.png")
 
# Stampo il grafico
plt.show()



