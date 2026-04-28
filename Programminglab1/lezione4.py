#programmazione ad oggetti
#Creare una classe coin che ha come attributo il valore della faccia
#● E ha due metodi:
#○ uno che simula il lancio della moneta e che salva il valore sull'attributo faccia.
#○ uno che ritorna il valore dell'attributo faccia

class Coin:
    def __init__(self):
        self.face = None

    def toss(self):
        import random
        self.face = random.choice(['heads', 'tails'])

    def get_face(self):
        return self.face
    
#Creare un oggetto coin e simulare 5 lanci, stampando il risultato di ogni lancio
coin = Coin()
for _ in range(5):
    coin.toss()
    print(coin.get_face())

#Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
#● modello (per il modello del veicolo);
#● marca (per la marca del veicolo);
#● anno (per l'anno del veicolo).
#● speed (per la velocità del veicolo)
#E di questi metodi:
#●_init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
#assegnare 0 all’attributo dati speed.
#● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
#● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
#● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
#● get_speed che restituisce la velocità corrente.

class Veicolo:
    def __init__(self, marca, modello, anni):
        self.marca = marca
        self.modello = modello
        self.anno = anni
        self.speed = 0

    def __str__(self):
        return f"{self.marca} {self.modello} ({self.anno}) - Speed: {self.speed} km/h"
    
    def accellerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    
#Creare un oggetto veicolo e simulare l’accelerazione e la frenata, stampando la velocità dopo ogni operazione
veicolo = Veicolo("Toyota", "Corolla", 2020)
print(veicolo)
veicolo.accellerare()
print(veicolo)
veicolo.accellerare()
print(veicolo)
veicolo.frenare() 

#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste,
#ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []
        with open(self.name, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        return data
    
