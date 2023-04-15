# -*- coding: utf-8 -*-
"""
Esercizio 4 di Fake News
"""
import pandas as pd
import matplotlib.pyplot as plt
tweet=pd.read_csv("tweets.csv") 
domini=pd.read_csv("domains.csv")

#Unisco i due dataset
merged_df=pd.merge(tweet,domini,on="domain")

unione_df=merged_df.rename(columns={"domain_type":"Tipo di dominio"})

#Calcolare il numero di articoli unici per tipo usando groupby
domini_unici=unione_df.groupby("Tipo di dominio")["domain"].nunique() #nunique  restituisce i valori unici in una colonna

#Calcolo il numero di tweet per tipo di dominio
tweet_type=unione_df.groupby("Tipo di dominio")["text"].count()

#Definisco una variabile che racchiuda il totale dei domini
totDomini=domini["domain"].nunique()

#Calcolo la proporzione di articoli unici per dominio e printo
articoliProp=domini_unici/totDomini
print("Articoli unici per tipo di dominio:")
print("\n")
print(articoliProp)

#Definisco una variabile che racchiuda il numero totale di Tweet
totTweet=tweet["text"].count()
#Calcolo la proporzione e printo
tweetProp=tweet_type/totTweet
print("\nLa proporzione di tweet per tipo di dominio è:")
print("\n")
print(tweetProp) 

# G R A F I C O

fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(10,5))

#grafico1
articoliProp.plot(kind="bar", ax=ax1,color=["blue","red","green"])
ax1.set_title("Proporzione di articoli unici per tipo di dominio",fontweight="bold")
ax1.set_xlabel("Tipo di dominio",fontweight="bold")
ax1.set_ylabel("Proporzione",fontweight="bold")

#Grafico 2
tweetProp.plot(kind="bar",ax=ax2,color=["blue","red","green"]) 
ax2.set_title("Proporzione di tweet per tipo di dominio",fontweight="bold") #grassetto
ax2.set_xlabel("Tipo di domino",fontweight="bold")
ax1.set_ylabel("Proporzione",fontweight="bold")

plt.tight_layout() #ridimensiona automaticamente i subplot in modo che non si sovrappongano, quindi evita che i label/ticks/titoli si taglino
plt.show()





