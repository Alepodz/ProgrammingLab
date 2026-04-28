from datetime import datetime

def prossimocompleanno (oggi,datanascita):
   pc=datetime(oggi.year,datanascita.month,datanascita.day)
   if (pc<oggi):
      pc=datetime(oggi.year+1,datanascita.month,datanascita.day)
   differenza=pc-oggi
   giorni = differenza.days
   secondi = differenza.seconds
   ore = secondi // 3600
   minuti = (secondi % 3600) // 60
   secondi_finali = secondi % 60
   print("Mancano al prossimo compleanno:")
   print(giorni, "giorni,", ore, "ore,", minuti, "minuti,", secondi_finali, "secondi")

    

print("Inserisci giorno di nascita")
giorno = int(input())
print("Inserisci mese di nascita")
mese = int(input())
print("Inserisci anno di nascita")
anno = int(input())
datanascita = datetime(anno, mese, giorno)
oggi = datetime.now()
eta = oggi.year - datanascita.year
if (oggi.month, oggi.day) < (datanascita.month, datanascita.day):
    eta -= 1
print("La tua età è:", eta)
prossimocompleanno(oggi,datanascita)


#Esercizio 6
#Scrivete un programma che chieda all'utente di inserire un numero intero. Se
#l'utente inserisce un valore valido, il programma deve stampare il quadrato del
#numero. Se l'utente inserisce un valore non valido, il programma deve
#visualizzare un messaggio di errore e richiedere nuovamente l'input.
numero = None

while numero == None:
    try:
        print("dammi un numero intero")
        numero = int(input())
    except Exception as e:
        print(e)
        numero = None

quadrato = numero * numero
print("il quadrato è:", quadrato)


#Esercizio 7
#Create un programma che mostri un menù all'utente con tre opzioni:
#1. Calcolare la somma di due numeri.
#2. Calcolare la differenza tra due numeri.
#3. Uscire.
#Il programma deve:
#1. Chiedere all'utente di scegliere un'opzione (1, 2 o 3).
#2. Eseguire l'operazione corrispondente se l'input è valido.
#3. Gestire input non validi mostrando un messaggio di errore.
#4. Continuare a mostrare il menù fino a quando l'utente sceglie di uscire (opzione 3)

while True:

    print("Menu:")
    print("1. Somma di due numeri")
    print("2. Differenza tra due numeri")
    print("3. Uscire")

    scelta = input("Scegli un'opzione (1,2,3): ")

    if scelta == "1":
        try:
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            print("La somma è:", a + b)
        except:
            print("Errore: inserisci numeri validi")

    elif scelta == "2":
        try:
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            print("La differenza è:", a - b)
        except:
            print("Errore: inserisci numeri validi")

    elif scelta == "3":
        print("Uscita dal programma")
        break

    else:
        print("Errore: scelta non valida")