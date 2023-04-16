"""
Fra i tweet che contengono una determinata URL, 
qual è la percentuale di tweet scritti
entro 48 ore dalla prima volta che la URL è stata mai twittata?

Calcolare per ciascuna URL la prima volta che appare nel dataset. 
Con la funzione hours_difference
calcolare per ogni tweet quante ore di distanza c’è fra data e ora di
pubblicazione rispetto alla prima apparizione della URL che contiene. 

Qual è il valore medio per news, fake news e fact checking?
"""

#Import delle librerie
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#Leggiamo i file .csv tramite la libreria pandas
tweets = pd.read_csv("tweets.csv")
domains = pd.read_csv("domains.csv")

#Merge dei due file .csv
merged = pd.merge(tweets,domains,
                  left_on = 'domain', right_on = 'domain')

#Definiamo un metodo per fare la differenza tra due date
def hours_difference( date1, date2 ):
    format = '%Y-%m-%d %H:%M:%S'
    date1 = datetime.datetime.strptime(date1, format)
    date2 = datetime.datetime.strptime(date2, format)
    diff = date1 - date2
    hours = (diff.total_seconds()) // 60
    return hours

#Filtriamo il DataFrame solamente per gli attributi che ci servono
merged = merged[['date','url','domain_type']]

#Raggruppiamo per url e data, la data 'minore'(ovvero la prima apparizione) tra per ogni url
primo_tweet = merged.groupby('url')['date'].min()

#Inseriamo una nuova colonna e applichiamo una funzione lambda per fare la differenza tra le due date
merged['differenza_ore'] = merged.apply(lambda x: hours_difference(x['date'], primo_tweet[x['url']]), axis=1)

#Numero di tweet con differenza_ore minore o uguale 48
numero_tweets_48_ore = len(merged[merged['differenza_ore']<=48])

#Numero di tweet totali nel dataframe
tweets_totali = len(merged)

#Percentuale tra i numeri di tweet totali e tweet con 48 ore di pubblicazione dal primo
percentuale_tweets_48_ore = (numero_tweets_48_ore / tweets_totali) * 100

#Media ore per ogni tipo di dominio
media_ore_news = merged[merged['domain_type'] == 'news']['differenza_ore'].mean()
media_ore_fake_news = merged[merged['domain_type'] == 'fake news']['differenza_ore'].mean()
media_ore_fact_checking = merged[merged['domain_type'] == 'fact checking']['differenza_ore'].mean()

#Grafico
labels = ['Nelle prime 48 ore', 'Dopo le 48 ore']
sizes = [numero_tweets_48_ore, tweets_totali - percentuale_tweets_48_ore]
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.set_title("Percentuale di tweet pubblicati entro 48 ore", pad=20, fontweight='bold')

categories = ['News', 'Fake news', 'Fact checking']
values = [media_ore_news, media_ore_fake_news, media_ore_fact_checking]

#Colori per le barre
colors = ['green', 'red', 'blue']

ax2.bar(categories, values, color=colors)
ax2.set_title("Differenza media di ore tra il tweet e il primo tweet", pad=20, fontweight='bold')
ax2.set_ylabel("Media ore tweet")

#Legenda
legend_labels = ['News', 'Fake news', 'Fact checking']
legend_colors = [colors[0], colors[1], colors[2]]
legend_elements = [plt.Rectangle((0,0), 1, 1, color=color) for color in legend_colors]
ax2.legend(legend_elements, legend_labels, loc='upper left')

#Evitiamo la sovrapposizione tra gli elementi dei due subplot
plt.tight_layout()

#Mostriamo il grafico
plt.show()
