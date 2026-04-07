
#appunti slide 6/7
#esempio 1
my_var = 'Ciao'

try:
 my_var = float (my_var)
except Exception as e:
 print( 'Non posso convertire "my_var" a valore numerico!')
 print('La variabile "my_var" valeva: "{}"'.format(my_var))
 print('Ed ho avuto questo errore: "{}"'.format(e)) #stampa il messaggio di errore associato all'eccezione

#esempio 2
try:
 file_parametro = open (nome_file_parametro) # type: ignore
 parametro_come_stringa = file_parametro.read() #legge il contenuto del file e lo memorizza in parametro_come_stringa
 parametro_come_float = float(parametro_come_stringa)#prova a convertire il valore letto dal file a un numero decimale
except IOError:
 print('Non posso leggere il file!')
 print('Userò il vaore di default per il parametro')
except ValueError:
 print('Non posso convertire il parametro a valore numerico!')
 print('Errore di valore, il parametro valeva "{}".'.format(parametro_come_stringa))
 print('Userò il valore di default per il parametro')
except Exception as error:
 print ('Errore generico: "{}". '.format(error))
 print ('Userò il valore di default per il parametro')
else:
 parametro = parametro_come_float
finally:
 file_parametro.close()

#esercizio1
#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste,
#ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

class CSVFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        lst = []
        with open(self.name) as f:
            for line in f:
                elements = line.strip().split(',')
                lst.append(elements)
        return lst

#es2
#Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a
#schermo un messaggio di errore* se si cerca di aprire un file non esistente.
#Potete fare questo controllo:
#a) nella funzione get_data(), oppure
#  b) nell’__init__() (basta che leggiate la prima riga per vedere se il file esiste)
class CSVFile:
    def __init__(self, name):
        self.name = name
        try:
            with open(self.name) as f:
                pass
        except Exception as e:
            print('Errore: il file "{}" non esiste!'.format(self.name))
            print('Errore specifico: "{}"'.format(e))
    
    def get_data(self):
        lst = []
        with open(self.name) as f:
            for line in f:
                elements = line.strip().split(',')
                lst.append(elements)
        return lst
#es3
#Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che
#converta automaticamente a numero floattutte le colonne tranne la prima (della data).
#hiamate la get_data originale con super().get_data(), poi converite tutto a float.
#A questo punto, aggiungete a mano questi due campi al file “shampoo_sales.csv”:
#01-01-2015,
#01-02-2015,ciao
#e gestite gli errori che verranno generati in modo che le linee vengano saltate senza
#bloccare il programma ma che venga stampato a schermo l’errore

class NumericalCSVFile(CSVFile):
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []

        for line in string_data:
            try:
                new_line = [line[0]]  # la prima colonna (data) resta stringa

                for element in line[1:]:
                    new_line.append(float(element))

                numerical_data.append(new_line)

            except Exception as e:
                print("Errore nella riga:", line)
                print("Tipo di errore:", e)

        return numerical_data
    
#Modificate l’oggetto CSVFile della lezione precedente in modo che alzi
# un'eccezione se il nome del file non è una stringa (nell’ __init__()).
#Poi, modificate la funzione get_data() di CSVFilein modo da leggere solo un’ intervallo di righe del file*,
#  aggiungendo gli argomenti started get_data(self, start=None, end=None)
#endopzionali, controllandone la correttezza e sanitizzandoli se serve.
#inclusa l’intestazione, estremi inclusi, e partendo da “1”.

class CSVFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Il nome del file deve essere una stringa")
        self.name = name

    def get_data(self, start=None, end=None):
        data = []

        with open(self.name, "r") as f:
            for line in f:
                data.append(line.strip().split(","))

        # sanitizzazione di start
        if start is None:
            start = 1
        elif not isinstance(start, int):
            raise Exception("start deve essere un intero")
        elif start < 1:
            start = 1

        # sanitizzazione di end
        if end is None:
            end = len(data)
        elif not isinstance(end, int):
            raise Exception("end deve essere un intero")
        elif end < 1:
            end = 1

        # se start è maggiore del numero di righe, restituisco lista vuota
        if start > len(data):
            return []

        # se end supera la lunghezza del file, lo porto all'ultima riga
        if end > len(data):
            end = len(data)

        # se start > end, restituisco lista vuota
        if start > end:
            return []

        # slicing: start ed end sono inclusi, ma Python esclude l'ultimo
        return data[start - 1:end]
    

#Esercizio 5
#Scrivete un programma che riceva una data di nascita come input e visualizzi
#l’età dell’utente e il numero di giorni, ore, minuti e secondi che mancano al
#prossimo compleanno.



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

