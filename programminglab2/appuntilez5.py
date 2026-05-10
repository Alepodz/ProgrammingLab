#esempio di codice vari
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd
import seaborn as sns #swerve per grafici piu belli

# inserisco i dati
colori = np.array(['nero', 'blu', 'verde', 'marrone'])
vettore_probabilita = np.array([1/20,4/20,5/20,10/20])

#DISTRIBUZIONE DISCRETA (valori fniti)
# creo il grafico
plt.bar(colori, vettore_probabilita, color= ['black', 'blue', 'green', 'brown'])
# do un titolo al grafico
plt.title('distribuzione discreta')
# mostro il grafico
plt.show()

#discreta quantitativa
numeri = np.array(['18', '19', '20', '21', '22'])
vettore_probabilita = np.array([1/20,9/20,6/20,3/20,1/20])
plt.bar(numeri, vettore_probabilita)
plt.title('distribuzione discreta (quantitativa)')
plt.show()#la variabile può assumere valori separati, non infiniti.


#distrubuzione uniforme discreta
numeri = [1,2,3,4,5,6]
vettore_probabilita = [1/6,1/6,1/6,1/6,1/6,1/6]
plt.bar(numeri,vettore_probabilita)
plt.title('distribuzione uniforme discreta')
plt.show()#ogni numero ha la stessa probabilità



#calcolo media moda e mediana
colori = np.array(['18', '19', '20', '21', '22'])
vettore_valori=np.array([18,19,19,19,19,19,19,19,19,19,20,20,20,20,20,20,21,21,21,22])
n = len(vettore_valori)
media = np.sum(vettore_valori)/n
if n%2==0:  # se n è pari
  mediana = (vettore_valori[n//2-1] + vettore_valori[n//2])/2.  # considerando l'indice che parte da zero quindi devo "slittare" di uno indietro
else:
  mediana = vettore_valori[(n-1)//2] # (n+1)/2 -1 , considerando l'indice che parte da zero quindi devo "slittare di uno indietro"
print('media:', media)
print('mediana:', mediana)

#esistono i metodi in numpy
print('media:', np.mean(vettore_valori))
print('mediana:', np.median(vettore_valori))




#DISTRIBUZIONI VAL CONTINUI

#distribuzione uniforme (tutti i valori dell'intervallo sono equalmente possibili)
X = st.uniform(0,1) #cosi creo due distribuzioni uniformi continue (predno numeri da zero a uno)
X2 = st.uniform(2,2)# è uniforme su 2 e 4
fig, ax = plt.subplots() #fig=foglio,ax=grafico sul foglio, subplots crea un grafico vuoto pronto per essere disegnato
xs = np.linspace(-0.1, 4.1, 200) #Crea 200 numeri equidistanti tra -0.1 e 4.1., serve per disegnare la curva
ax.plot(xs, X.pdf(xs),label='U[0,1]') #disegna il grafico della sitribuzione(x.pdf calcola la densità del grafico(altezza))
#ax.plot(val asse x, val asse y)


#distribuzione normale
#es 1
mu = 175.0
sigma = 10.0 #curva piu stretta es 2
X = st.norm(loc=mu, scale=sigma)#
fig, ax = plt.subplots()#crea grafico
xs = np.linspace(mu - 6.0 * sigma, mu + 6.0 * sigma, 100)#costruzioni lasse x,crea 100 numeri equispaziati tra due estremi
ax.plot(xs, X.pdf(xs))#disegno curva
ax.axvline(np.mean(xs), color='r', linestyle='--', label="Mean")#disegnaline verticale
ax.axvline(np.median(xs), color='g', linestyle='-', label="Median") #IMPORTANTE:nella normale media e mediana coincidono
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')#il dollaro dice a matlob che questa è una formula matematica
plt.xlim([100, 250]) #restringe il grafico
ax.legend()

#es2
mu = 175.0
sigma = 20.0#curva piu larga es 1
X = st.norm(loc=mu, scale=sigma)

fig, ax = plt.subplots()
xs = np.linspace(mu - 6.0 * sigma, mu + 6.0 * sigma, 100)
ax.plot(xs, X.pdf(xs))
ax.axvline(np.mean(xs), color='r', linestyle='--', label="Mean")
ax.axvline(np.median(xs), color='g', linestyle='-', label="Median")
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')
plt.xlim([100, 250])
ax.legend()

#DISTRIBUZIONE PROBABILITà
# Estrarre un singolo numero casuale distribuito uniformemente tra 0 e 1
np.random.uniform(low=0.0, high=1.0, size=None)
# Estrarre un singolo numero casuale da una distribuzione normale con media 0 e deviazione standard 1
np.random.normal(loc=0.0, scale=1.0, size=None)
# Estrarre un singolo numero casuale da una distribuzione discreta con il seguente vettore di propbabilità
vettore_probabilita = [0.05,0.1,0.2,0.3,0.35]
np.random.choice(a=[1,2,3,4,5], size=None, replace=True, p=vettore_probabilita)

help(np.random.choice)


# Facciamo il plot orizzontale e cambiamo il colore delle barre in un giallo più scuro.
stelle = [1, 2, 3, 4, 5]
freq_assoluta_stelle = [1, 2, 4, 6, 7]

# Creazione del diagramma a barre orizzontali con un colore giallo più scuro
plt.figure(figsize=(10, 6))
bars = plt.barh(stelle, freq_assoluta_stelle, color='gold')

# Aggiunta del titolo e delle etichette agli assi
plt.title('Frequenza Assoluta delle Stelle')
plt.ylabel('Numero di Stelle')
plt.xlabel('Frequenza Assoluta')

# Visualizzazione del diagramma
plt.show()

# Dati estratti dalle tabelle fornite
altezze = ['1.50–1.60', '1.60–1.70', '1.70–1.80', '1.80–1.90', '1.90–2.00']
freq_assoluta_m = np.array([0, 1, 3, 4, 2])  # Frequenza assoluta maschile
freq_assoluta_f = np.array([1, 3, 4, 2, 0])  # Frequenza assoluta femminile

# Larghezza delle barre
bar_width = 0.35

# Creazione del diagramma a barre sovrapposte
fig, ax = plt.subplots(figsize=(12, 7))

# Posizioni delle barre
r1 = np.arange(len(freq_assoluta_m))
r2 = [x + bar_width for x in r1]

# Impostiamo le posizioni delle barre per maschi e femmine
posizioni_m = np.arange(5)  # Posizioni per maschi
posizioni_f = posizioni_m + bar_width  # Posizioni per femmine con uno spostamento

# Creiamo le barre per maschi e femmine
barre_m = ax.bar(posizioni_m, freq_assoluta_m, bar_width, label='Maschi', color='blue')
barre_f = ax.bar(posizioni_f, freq_assoluta_f, bar_width, label='Femmine', color='red')

# Aggiungiamo titolo e etichette agli assi
ax.set_title('Frequenza Assoluta per Altezza e Genere')
ax.set_xlabel('Altezza')
ax.set_ylabel('Frequenza Assoluta')

# Definiamo le etichette per l'asse delle x
ax.set_xticks(posizioni_m + bar_width / 2)
ax.set_xticklabels(altezze)

# Aggiungiamo la legenda
ax.legend()

# Mostra il grafico
plt.show()





#DIAGRAMMI CIRCOLARI
# Dati per il diagramma circolare degli occhi
labels = ['Nero', 'Azzurro', 'Verde', 'Marrone']
sizes = [1, 4, 5, 10]  # Frequenza assoluta per ogni colore di occhi
colors = ['black', 'blue', 'green', 'brown']

# Creazione del diagramma circolare
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Aggiunta del titolo
plt.title('Distribuzione dei Colori degli Occhi')

# Mostra il diagramma circolare
plt.show()


# Dati per il diagramma circolare delle stelle
labels_stelle = ['1 Stella', '2 Stelle', '3 Stelle', '4 Stelle', '5 Stelle']
sizes_stelle = [1, 2, 4, 6, 7]  # Frequenza assoluta per ogni categoria di stelle
colors_stelle_gold = [  '#b5b17a','#b5a642','#d4af37', '#ffc700', 'gold']

# Creazione del diagramma circolare
plt.figure(figsize=(8, 8))
plt.pie(sizes_stelle, labels=labels_stelle, colors=colors_stelle_gold, autopct='%1.1f%%', startangle=140)

# Aggiunta del titolo
plt.title('Distribuzione delle Valutazioni a Stelle')

# Mostra il diagramma circolare
plt.show()






#ISTOGRAMMI
dati = [
    1.55,
    1.653, 1.654, 1.655, 1.657,
    1.751, 1.752, 1.753, 1.754, 1.755, 1.756, 1.757,
    1.854, 1.855, 1.856, 1.857, 1.858, 1.859,
    1.951, 1.952
]

plt.figure(figsize=(8,5))
plt.hist(dati, bins=200, range=(1.50, 2.00), edgecolor='black')

plt.title('Distribuzione delle Altezze')
plt.xlabel('Altezza')
plt.ylabel('Frequenza')

plt.show()

vettore_probabilita = [0.05,0.1,0.2,0.3,0.35]
n = np.random.choice(a=[1,2,3,4,5], size=100, replace=True, p=vettore_probabilita)

plt.hist(n, [1, 2, 3, 4, 5, 6], linewidth=0.5, edgecolor="white")
plt.xticks(np.arange(1, 6))
plt.title('DISCRETA: 10 campioni')
plt.show()





#Scatter plot (grafico a dispersione)
import numpy as np

# Generazione di valori casuali per la temperatura esterna e il consumo di gas
np.random.seed(0)  # Per riproducibilità
external_temperature = np.random.uniform(low=0, high=10, size=100)
gas_consumption = np.random.uniform(low=2, high=7, size=100) - external_temperature * 0.5

# Creazione del plot simile all'immagine fornita
plt.figure(figsize=(10, 6))
plt.scatter(external_temperature, gas_consumption, color='blue')
plt.title('Consumo di Gas di una Casa vs. Temperatura Esterna Media')
plt.xlabel('temperatura esterna media')
plt.ylabel('consumo di gas di una casa')
plt.grid(True)  # Aggiunge una griglia per migliorare la leggibilità
plt.show()





#SUBPLOTS
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crea 2 sottotrame (1 riga, 2 colonne)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Primo subplot
ax[0].plot(x, y1)
ax[0].set_title("Seno")

# Secondo subplot
ax[1].plot(x, y2)
ax[1].set_title("Coseno")

plt.tight_layout()
plt.show()



