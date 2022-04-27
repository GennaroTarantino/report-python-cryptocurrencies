# Task
# 1- La criptovaluta con il volume maggiore (in $) delle ultime 24 ore - DONE
# 2-Le migliori e peggiori 10 criptovalute (per incremento in percentuale delle ultime 24 ore) - DONE
# 3-La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute - DONE
# 4-La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$ - DONE
# 5-La percentuale di guadagno o perdita che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute*
# il giorno prima (ipotizzando che la classifca non sia cambiata)Le prime 20 criptovalute secondo la classifica predefinita di CoinMarketCap,
# quella visibile sul sito, dunque ordinate per capitalizzazione. DONE
# -Per evitare che il vostro programma sovrascriva lo stesso file JSON, denominatelo con la data del momento in cui il programma viene eseguito.* - DONE


# Packages
import json
import requests
from datetime import datetime
import time
from pprint import pprint
import itertools


# Data
class Report:
    def __init__(self):

        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        self.params = {
            'start': '1',
            'limit': '100',
            'convert': 'USD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'lol'  # Inserisci qui la tua chiave privata
        }



    def fetchCurrenciesData(self):
        r = requests.get(url = self.url, headers=self.headers, params=self.params).json()
        return r['data']

# Logic

impactReport = Report()

while(1):
    currenttime = str(datetime.now())
    print(currenttime)
    a = 0 # Trigger di stampa
    b = 0 # Trigger di stampa
    c = 0 # Trigger di stampa
    d = 0  # Trigger di stampa
    e = 0  # Trigger di stampa
    currencies= impactReport.fetchCurrenciesData() # Carica Dati

    # Dichiarazione Liste

    currencyVol = ({}) # Dizionario  Volumi
    sortedDictPlus = [] # Lista Decrescente
    sortedDictMalus = [] # Lista Crescente
    currencyHightVolume = [] # Lista Migliori Token Volume
    currencyChangePlus = ({}) # Dizionario Simbolo - Variazioni Positive
    currencyChangeMalus = ({}) # Dizionario Simbolo - Variazioni Negative
    currencyPriceMCap = ({}) # Dizionario Prezzo - Market Cap
    sortcurrencyPrice = ({}) # Dizionario Prezzi Ordinato secondo Market Cap
    currencyChangeMCap = ({}) # Dizionario Cambio Giornaliero - Market Cap
    sortcurrencyChange = ({}) # Dizionario Cambio Giornaliero Ordinato secondo Market Cap
    firstcoinVol = []  # Miglior Criptovaluta per volume scambiato
    sumlistsortcurrencyPrice = [] #Somma dei prezzi
    listsortcurrencyPrice = [] # Lista dei Prezzi
    sumlistcurrencyHightVolume = [] # Somma dei prezzi nella condizione volume > 76000000
    sumlistlastdayprice = [] # Somma dei prezzi del giorno precedente
    percentvarCap = 0 # Variazione percentuale del capitale



    for currency in currencies:

    # Lista Migliore Volume
        currencyVol.update({currency['symbol']:currency['quote']['USD']['volume_24h']})

    # Lista Migliori Peggiori Cambio Percentuale
        if currency['quote']['USD']['percent_change_24h'] > 0:
            currencyChangePlus.update({currency['symbol']: currency['quote']['USD']['percent_change_24h']})
        else:
            currencyChangeMalus.update({currency['symbol']: currency['quote']['USD']['percent_change_24h']})

    # Lista delle Migliori 20 Criptovalute ordinata per Market Cap
        currencyPriceMCap.update({currency['quote']['USD']['price']: currency['quote']['USD']['market_cap']})

    # Lista Cambio Percentuale delle 20 Criptovalute ordinata per Market Cap
        currencyChangeMCap.update({currency['quote']['USD']['percent_change_24h'] : currency['quote']['USD']['market_cap']})

    # Lista Criptovalute con volume scambiato maggiore di 76'000'000$
        if currency['quote']['USD']['volume_24h'] > 76000000 :
          currencyHightVolume.append(currency['quote']['USD']['price'])



# Logica Migliore Volume


    if a==0 :
           a=1
           sortedcurrencyVol = dict(sorted(currencyVol.items(), key=lambda x: x[1], reverse=True)) # Ordino
           # sortedcurrencyVol = dict(currencyVol)
           listsortcurrencyVol = list(sortedcurrencyVol.keys())
           #listsortcurrencyVol = list(listsortcurrencyVol)
           firstcoinVol = listsortcurrencyVol[0]

           print(F'Le Migliore Cryptovaluta per volume scambiato nelle ultime 24h -> {firstcoinVol}$')


# Logica Migliori e Peggiori 10 criptovalute per cambio percentuale

    if b == 0 and a== 1:
           b = 1
           sortedDictPlus = sorted(currencyChangePlus.items(), key=lambda x: x[1], reverse=True)  # Ordine Decrescente
           sortedDictMalus = sorted(currencyChangeMalus.items(), key=lambda x: x[1])  # Ordine decrescente

           print('Le Migliori 10 Cryptovalute per cambio percentuale nelle ultime 24h : ')
           pprint(sortedDictPlus[0:10])
           print('Le Peggiori 10 Cryptovalute per cambio percentuale nelle ultime 24h : ')
           pprint(sortedDictMalus[0:10])



# Logica Quantità di denaro necessaria per acquistare 1 Unità delle prime 20 Coin # Le prime 20 criptovalute secondo la classifica predefinita di CoinMarketCap, quella visibile sul sito, dunque ordinate per capitalizzazione

    if b==1 and c == 0:
            c = 1
            sortcurrencyPrice = sorted(currencyPriceMCap.items(), key=lambda x: x[1], reverse=True) # Ordino la lista
            sortcurrencyPrice = dict(sortcurrencyPrice) # Dichiaro il dizionario
            listsortcurrencyPrice = list(sortcurrencyPrice.keys()) # Trasferisco nella lista i valori e Definisco
            sumlistsortcurrencyPrice = sum(listsortcurrencyPrice[0:20]) # Sommo i valori della lista
            print(f'Quantità di denaro necessaria per 1 Unita delle prime 20 Coin -> {sumlistsortcurrencyPrice}')



# Logica Quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$


    if  c==1 and d == 0:
            d = 1
            listcurrencyHightVolume = list(currencyHightVolume)
            sumlistcurrencyHightVolume = sum(listcurrencyHightVolume)
            print(f'Quantità di denaro necessaria per tutte le criptovalute il cui '
                  f'volume delle ultime 24 ore sia superiore a 76.000.000$ -> {sumlistcurrencyHightVolume}')


# Logica La percentuale di guadagno o perdita che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute*
# il giorno prima (ipotizzando che la classifca non sia cambiata)

    if  d==1 and e==0:
            e=1
            sortcurrencyChange = sorted(currencyChangeMCap.items(), key=lambda x: x[1], reverse=True) # Ordino la lista
            sortcurrencyChange = dict(sortcurrencyChange) #Definisco
            listsortcurrencyChange = list(sortcurrencyChange.keys()) # Trasferisco e Definisco
            listlastdayprice = list(map(lambda x,y: (1+(x/100))*y ,listsortcurrencyChange,listsortcurrencyPrice)) # Moltiplico le due Liste: Price*(1+(Change_24h/100))
            sumlistlastdayprice = sum(listlastdayprice[0:20]) # Calcolo capitale investito ieri per le 20 coin
            percentvarCap = ((sumlistsortcurrencyPrice-sumlistlastdayprice)/sumlistlastdayprice)*100 # Calcolo la percentuale di guadagno/perdita
            print(f'Capitale di oggi -> {sumlistsortcurrencyPrice}')
            print(f'Capitale di ieri -> {sumlistlastdayprice}')
            print(f'La percentuale di profitto/perdita è -> {percentvarCap}%')

    jsonData = {

        "Data": currenttime,
        "Le Migliore Cryptovaluta per volume scambiato nelle ultime 24h": firstcoinVol,
        "Le Migliori 10 Cryptovalute per cambio percentuale nelle ultime 24h": sortedDictPlus[0:10],
        "Le Peggiori 10 Cryptovalute per cambio percentuale nelle ultime 24h": sortedDictMalus[0:10],
        "Quantita di denaro necessaria per tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000": sumlistcurrencyHightVolume,
        "Quantita di denaro necessaria per 1 Unità delle prime 20 Coin": sumlistsortcurrencyPrice,
        "Capitale di oggi": sumlistsortcurrencyPrice,
        "Capitale di ieri": sumlistlastdayprice,
        "La percentuale di profitto / perdita ": percentvarCap,

        }
    file = open('Progetto_Python_di_Gennaro_Tarantino.json','w')
    json.dump(jsonData, file, indent=2)
    file.close()








    # Runtime

    minutes = 1440
    seconds = 60 * minutes
    time.sleep(seconds)


# Commit
