# -*- coding: utf-8 -*-
"""
Esercizio 5 Fake News
"""
import pandas as pd
import matplotlib.pyplot as plt

tweet = pd.read_csv("tweets.csv") 
domini = pd.read_csv("domains.csv")

#Unisco i due dataset con merge e utilizzo la colonna "domain" come chiave di unione
unione_df = pd.merge(tweet,domini,on="domain")

# Filtro i tweet per tipo di dominio(news,fake news,fact checking) utilizzando la colonna "domain_type" e creo dei sotto-dataframe
# News:
news = unione_df[unione_df["domain_type"] == "news"]     
news = news[['user_id', 'text']].groupby(['user_id']).count().reset_index()
news = news.sort_values('text', ascending = False)
top_news = news.head(10) 
print(top_news)

# Fake News:
fake_news = unione_df[unione_df["domain_type"]=="fake news"]
fake_news = fake_news[['user_id', 'text']].groupby(['user_id']).count().reset_index()
fake_news = fake_news.sort_values('text', ascending = False)
top_fake_news = fake_news.head(10) 
print(top_fake_news)

#Fact Checking:
fact_checking = unione_df[unione_df["domain_type"] == "fact checking"]
fact_checking = fact_checking[['user_id', 'text']].groupby(['user_id']).count().reset_index()
fact_checking = fact_checking.sort_values('text', ascending = False)
fact_checking = fact_checking.head(10) 
print(fact_checking)

# Creazione di una figura con 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15,5))

# Grafico a torta delle news
top_news.plot.pie(y = 'text', labels = top_news['text'], legend = False, ax = axs[0])
axs[0].set_title('Top 10 utenti che pubblicano news')
axs[0].set_ylabel('')

# Grafico a torta delle fake news
top_fake_news.plot.pie(y='text', labels = top_fake_news['text'], legend = False, ax = axs[1])
axs[1].set_title('Top 10 utenti che pubblicano fake news')
axs[1].set_ylabel('')

# Grafico a torta del fact checking
fact_checking.plot.pie(y = 'text', labels = fact_checking['text'], legend = False, ax = axs[2])
axs[2].set_title('Top 10 utenti che pubblicano fact checking')
axs[2].set_ylabel('')

# Mostra il plot completo
plt.show()

# Salvo la figura prodotta dal grafico
plt.savefig("Esercizio_05.png")

# Mostro il grafico
plt.show()













