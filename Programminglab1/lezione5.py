#classi di oggetti
# Un metodo di classe è un metodo che è della classe e non dell’oggetto:
#● Metodi normali:
#q = Queue()
#q.enqueue(3)
#● Metodo di classe:
#Queue.do_stuff()
#● Perché dovrebbero servirci? 

#● Perché a volte vogliamo che un metodo sia associato alla classe e non all’oggetto.
#● Per esempio, se vogliamo tenere traccia di quante istanze di una classe sono state create,
#  potremmo usare un metodo di classe per incrementare un contatore ogni volta che viene creata
# # una nuova istanza.


def from_list(cls, lst):
 q =cls()
 q.__data = lst
 return q

#esempio 1

class Student:
 def __init__(self, name, grade):
  self.name = name
  self.grade = grade

 def __lt__(self, other):
  return self.grade < other.grade
 def __eq__(self, other):
  return self.grade == other.grade
 
s1 = Student("Anna", 28)
s2 = Student("Marco", 30)
print(s1 < s2) # True
print(s1 == s2) # False

#esempio 2 con vettori

class Vector:
 def __init__(self, x, y):
  self.x = x
  self.y = y

 def __add__(self, other):
  return Vector(self.x + other.x, self.y + other.y)
 
 def __mul__(self, other):
  return Vector(self.x * other, self.y * other)
 
v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2
print(v3.x, v3.y)
v4 = v1 * 3
print(v4.x, v4.y)

#Python imposta automaticamente la variabile __name__ quando si esegue o
#si importa uno script
#○ __name__ = __main__ se si esegue lo script
#○ __name__ = nomescript se si importa il file python nomescript.py

#Scrivete una definizione di una classe di nome Canguro con i metodi seguenti:
#1. Un metodo .__init__ che inizializza un attributo lista contenuto_tasca
# con paramatro di default lista vuota
#2. Un metodo di nome intasca che prende un oggetto di qualsiasi tipo e lo inserisce in
#contenuto_tasca.
#3. Un metodo __str__ che restituisce una stringa di rappresentazione dell’oggetto Canguro e 
# dei contenuti della tasca.
#● Provate il codice creando due oggetti Canguro, assegnandoli a variabili di
#nome can e guro, e aggiungendo elementi a can. Cosa succede a guro?

class Canguro:
    
    def __init__(self, contenuto_tasca=[]): # iniziallizza contenuto tasca come lista vuota
        self.contenuto_tasca = contenuto_tasca
    
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)#cosa fa append? 
        #aggiunge un elemento alla fine della lista contenuto_tasca
    
    def __str__(self):
        return "Canguro con nella tasca: " + str(self.contenuto_tasca)
    
can = Canguro()
guro = Canguro()

can.intasca("mela")
can.intasca("chiavi")

print(can)
print(guro)
#Il problema è che quando si inizializza un attributo di classe con un valore mutabile 
# #(come una lista), tutte le istanze della classe condividono lo stesso oggetto mutabile. 
# Quindi, quando si aggiunge un elemento alla lista contenuto_tasca di can, 
# si sta effettivamente modificando la stessa lista condivisa da guro.
#  Per risolvere questo problema, è necessario inizializzare l'attributo contenuto_tasca all'interno
#  del metodo __init__ in modo che ogni istanza abbia la propria lista separata.

#versione corretta
class Canguro:
    
    def __init__(self): # iniziallizza contenuto tasca come lista vuota
        self.contenuto_tasca = []
    
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    
    def __str__(self):
        return "Canguro con nella tasca: " + str(self.contenuto_tasca)