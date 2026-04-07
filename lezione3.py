#stringhe
#es 1 somma lista
def sommalist(lista):
    somma=0
    for i in lista:
        somma+=i
    return somma

#es 2 verificare se una parola è palindroma
def palindroma(parola):
    invert= stringa[::-1]
    if stringa==invert:
        return True
    else:        return False

stringa= 'ciao'
print(stringa[1:2])

#verifia elemento in comune tra stringhe
def comune(stringa1,stringa2):
    for i in stringa1:#per ogni elemento i in stringa1
        if i in stringa2:#se i è presente in stringa2 allora
            return True
    return False 

#Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno
# almeno un elemento in comune
def elementcomune (lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
    return False
#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una
#lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] -
#>["uno","zero","sette","nove","otto"]
def ritornostringa(lista):
    stringa=[]
    for i in lista:
        if i==0:
            stringa.append("zero")
        elif i==1:
            stringa.append("uno")
        elif i==2:
            stringa.append("due")
        elif i==3:
            stringa.append("tre")
        elif i==4:
            stringa.append("quattro")
        elif i==5:
            stringa.append("cinque")
        elif i==6:
            stringa.append("sei")
        elif i==7:
            stringa.append("sette")
        elif i==8:
            stringa.append("otto")
        elif i==9:
            stringa.append("nove")
    return stringa

#Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il
#conteggio delle occorrenze.
def contocc(lista):
    dizionario={}
    for i in lista:
        if i in dizionario:
            dizionario[i]+=1
        else:
            dizionario[i]=1
    return dizionario

print('dammi una lista di parole')
lista = input().split()
print(contocc(lista))

#Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file
#passato come argomento

def sommafile(file):
    somma=0
    with open(file) as f:
        for line in f:
            somma+=float(line)
    return somma

#Definire una funzione che prende in input un file ed una parola e conta quante volte
#quella parola è presente sul file

def conta_parola(file, parola):
    count = 0
    with open(file) as f:
        for line in f:
            count += line.count(parola)
    return count

#Definire una funzione conteggio che prende come input un file e ritorna un dizionario
#con chiave le parole e valore il numero di volte che la parola è presente nel file.
def conteggio(file):
    dizionario = {}
    with open(file) as f:
        for line in f:
            parole = line.split()
            for parola in parole:
                if parola in dizionario:
                    dizionario[parola] += 1
                else:
                    dizionario[parola] = 1
    return dizionario
#Definire una funzione che prende come input un file, rimuove tutte le righe duplicate,
#scrive il risultato in un nuovo file chiamato unique.txt.
def rimuovi_duplicate(file):
    unique_lines = set()#uso set perche non ammette duplicati
    with open(file) as f:
        for line in f:
            unique_lines.add(line)#aggiungo ogni riga al set, se è già presente non viene aggiunta
    with open('unique.txt', 'w') as f:#apro il file in scrittura
        for line in unique_lines:
            f.write(line)
