# -*- coding: utf-8 -*-
"""
Esercizio 5 Fake News
"""
import pandas as pd
import matplotlib.pyplot as plt
tweet=pd.read_csv("tweets.csv") 
domini=pd.read_csv("domains.csv")

#Unisco i due dataset con merge e utilizzo la colonna "domain" come chiave di unione
unione_df=pd.merge(tweet,domini,on="domain")


#Filtro i tweet per tipo di dominio(news,fake news,fact checking) utilizzando la colonna "domain_type" e creo dei sotto-dataframe
    
#News:
news=unione_df[unione_df["domain_type"] == "news"]
        
#Fake News:
fake_news=unione_df[unione_df["domain_type"]=="fake news"]

#Fact Checking:
fact_checking=unione_df[unione_df["domain_type"] == "fact checking"]

#Calcolo il numero di tweet per utente per tipo di dominio con group by, sulla colonna User_id e poi conto il numero di righe con count

#Utenti news
utenti_news=news.groupby("user_id")["text"].count()

#Utenti fake news
utenti_fake_news=fake_news.groupby("user_id")["text"].count()

#Utenti   fact checking
utenti_fact_checking=fact_checking.groupby("user_id")["text"].count()

#Ora creo un unico dataframe con i risultati qua sopra usando il metodo concat()
dati_utente=pd.concat([utenti_news,utenti_fake_news,utenti_fact_checking],axis=1)

#Sostituisco i NaN con 0 per ogni colonna con un ciclo e uso il metodo fillna()
for col in dati_utente.columns:
    dati_utente[col]=dati_utente[col].fillna(0)

#Creo le colonne per tipo di dominio e vengono rinominate con il metodo columns()
dati_utente.columns = ["news","fake news","fact checking"]

#Creo una colonna totale nel dataframe "dati_utente", calcolo il totale dei tweet per ogni utente sommando i numeri di tweet per tipo di dominio con sum
dati_utente["totale"] = dati_utente.sum(axis=1)

#Ora ordino il dataframe con sort_values() in base alla colonna"totale" in ordine discendente uso head selezionando i primi 10
lista_utenti=dati_utente.sort_values("totale",ascending=False).head(10)

#Ho convertito i numeri in interi con il metodo astype() in modo da eliminare i numeri con la virgola
lista_utenti=lista_utenti.astype(int)


#printo
print("I 10 utenti più attivi sono:")
print("\n")
print(lista_utenti) 


# G R A F I C O
# PROPONGO UNA MODIFICA SE SIETE TUTTI D'ACCORDO SE NO VA BENE COSI'

#Ho selezionato solo la colonna "totale" per fare il grafico  e li salvo in una variabile
grafico = lista_utenti["totale"].head(10)
#Creo una lista di etichette con i primi 10 utenti  e salvo in una variabile
labels = lista_utenti.index[:10] 

#Ho sostituito le label originali con gli id con una lista di numeri da 1 a 10
nuove_labels = ["primo","secondo","terzo","quarto","quinto","sesto","settimo","nono","decimo"]

#lista colori
colors = ["green","red","yellow","blue","orange","pink","brown","purple","#007FFF","gray"]

#Cerchio bianco al centro della torta
grafico_torta=plt.Circle((0,0),0.7,color="white")

#Creo il grafico a torta passando le variabili grafico,labels e colors. Ho tolto le label dal grafico e ho utilizzato una legenda
#wedgeprops serve per specificare le proprietà delle fette impostando un spessore di linea a 2 e il colore bianco sul bordo
#startangle l'ho utilizzato per specificare l'angolo di inizio del grafico a torta a 90 gradi
#autpct è un formato delle etichette in percentuale 
#pctdistance l'ho utilizzato per distanziare i valori dal centro della torta al 70%
plt.pie(grafico,labels=None,colors=colors,wedgeprops={"linewidth":2,"edgecolor":"white"},startangle=90,autopct='%1.0f%%',pctdistance=0.7)

plt.subplots_adjust(top=1.5)
plt.title("i 10 utenti più attivi nel dataframe:",fontweight="bold")
plt.axis("equal")
#Legenda, best indica la posizione migliore in qui metterlo, poi ci sono le coordinate e le dimensioni
plt.legend(nuove_labels,loc="best",bbox_to_anchor=(-0.1,1),fontsize=10)
#sotto-titolo con coordinate e testo al centro
plt.text(0,-1.2,"Grafico che mostra la percentuale di tweet pubblicati dai 10 utenti più attivi",ha="center",fontweight="bold")

plt.show()














