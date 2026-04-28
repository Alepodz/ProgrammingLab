#import nunby as np

#esercizi
#1) TRASFORMARE I CCLI IN LIST COMPREHENSION
#Fai tre esempi di cicli producono una lista e poi riscrivi lo stesso codice 
# usando la list comprehension

#con ciclo for
numeri = []
for i in range(1, 6):
    numeri.append(i**2)
print(numeri)

#con list comprehemsion
numeri = [i**2 for i in range(1, 6)]
print(numeri)



#numeri pari con una lista:
lista = [1, 2, 3, 4, 5, 6]
pari = []
for x in lista:
    if x % 2 == 0:
        pari.append(x)
print(pari)

#con list comprehension
lista = [1, 2, 3, 4, 5, 6]
pari = [x for x in lista if x % 2 == 0]
print(pari)



#stringhe in maiuscolo
parole = ["ciao", "python", "esame"]
maiuscole = []
for parola in parole:
    maiuscole.append(parola.upper())
print(maiuscole)

#listh comprehension
parole = ["ciao", "python", "esame"]
maiuscole = [parola.upper() for parola in parole]
print(maiuscole)



#2. VETTORE DI NUMERI PRIMI

#Crea un vettore contenente tutti i numeri primi compresi tra 0 e 10
#(Puoi scriverli direttamente nell'array).
#Conta quanti numeri ci sono nel vettore utilizzando la funzione len(). Ottieni lo stesso
#  numero accedendo all'attributo .size del vettore.
#Quale pensi sia il tipo di dato (dtype) del vettore? Prova a rispondere senza eseguire
#  il codice e Verifica la tua risposta accedendo all'attributo .dtype del vettore
#Scrivi l'array usando una list comprehension che controlla che i numeri siano primi.


#ARRAY COME CREARLO
import numpy as np
v = np.array([2, 3, 5, 7])
print(v)
print(len(v))     # numero di elementi
print(v.size)     # numero di elementi
print(v.dtype)    # tipo di dato


#LIST COMPREHENSION CHE CONTROLLA I NUMERI PRIMI
import numpy as np
v = np.array([
    n for n in range(0, 11)
    if n > 1 and all(n % d != 0 for d in range(2, n))
])

print(v)
print(len(v))
print(v.size)
print(v.dtype)

#3)

import numpy as np
# array 2D senza scriverlo a mano (4 righe, 3 colonne)
a = np.arange(1, 13).reshape(4, 3)
# b: 2ª e 4ª riga (indice 1 e 3)
b = a[[1, 3], :]
# c: solo 3ª riga (indice 2)
c = a[2, :]
# divisione elemento per elemento per colonne (broadcasting)
d = a / c
print("a:\n", a)
print("b:\n", b)
print("c:\n", c)
print("a/c:\n", d)



#4)4. Analisi della Frequenza Cardiaca con NumPy

#Supponiamo che i seguenti valori rappresentino la tua frequenza cardiaca registrata dal tuo 
# #Fitbit durante la giornata:
#68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70
#Inserisci questi valori in un array NumPy.
#Trova la frequenza cardiaca minima registrata durante la giornata.
#(Questo valore rappresenta approssimativamente la tua frequenza cardiaca a riposo, un comune indicatore di salute.)
#Trova la frequenza cardiaca massima registrata durante la giornata.
#(Questo valore è un'indicazione dell'intensità dell'esercizio fisico.)
#Calcoliamo la percentuale di letture effettuate mentre stavi facendo esercizio fisico (frequenza cardiaca sopra a 120):
#Crea un nuovo array che contiene True quando la frequenza cardiaca è superiore a 120, e False quando è inferiore o uguale a 120.
#Utilizza una funzione di sintesi per calcolare la percentuale di osservazioni in cui la tua frequenza cardiaca era sopra 120.

import numpy as np

# array con i dati
hr = np.array([68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 
               162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70])
# minimo
min_hr = hr.min()
# massimo
max_hr = hr.max()
# array booleano (>120)
exercise = hr > 120
# percentuale sopra 120
percentuale = exercise.mean() * 100

print("Min:", min_hr)
print("Max:", max_hr)
print("Sopra 120:", exercise)
print("Percentuale:", percentuale)


#5. Manipolazione di vettori

#Creare un vettore contenente i seguenti stipendi: 50.000, 105.250, 55.000, 89.000.
#Qual è il costo totale del personale (somma di tutti gli stipendi dell'azienda)?

#Supponiamo che il nostro malvagio CEO abbia deciso di darsi un aumento.
#Modifica il vettore degli stipendi in modo che il CEO, la persona che guadagna 105.250 dollari, riceva un aumento del 15%.

#Il 115% di 105.250 dollari è 121.037,50 dollari.
#Questo valore è presente nel tuo array? Se no, riesci a capire il motivo?

#Ricrea il vettore e utilizza l'argomento dtype in modo che, quando il CEO riceve un aumento del 15%, il suo stipendio finale sia esattamente 121.037,50 dollari.

#Questo aumento ha infastidito l'impiegata con lo stipendio più basso (50.000 dollari), che ora pretende un aumento del 20%.
#Modifica il vettore per riflettere questo cambiamento.

#L'aumento dato al CEO e all'impiegata ha irritato gli altri due dipendenti, quindi ora devono ricevere un aumento del 10%.
#Modifica il vettore di conseguenza.

#Calcola il costo totale del personale dopo tutti gli aumenti.
#Alla fine, quanto è costato all'azienda l'aumento di circa 16.000 dollari del CEO?

import numpy as np

# vettore stipendi
stipendi = np.array([50000, 105250, 55000, 89000])

# costo totale iniziale
totale_iniziale = stipendi.sum()
print("Totale iniziale:", totale_iniziale)

# aumento del 15% al CEO
stipendi[stipendi == 105250] = stipendi[stipendi == 105250] * 1.15
print("Dopo aumento CEO:", stipendi)



