#parte di appunti
#utilizzo ciclo for sostituendolo con list comprehension
pari2 = [n for n in range(10) if n%2==0] #[espressione for elemento in iterabile if condizione]
print(pari2)
#versione con for
pari = []
for n in range(10):
 if n%2==0:
  pari.append(n)
print(pari)

#Funzioni anonime/ lambda function
def f(x):
 return x + 1
somma = lambda a, b: a + b
print(somma(2, 3)) # 5

f = lambda x: x + 1
print(f(5)) # 6
somma = lambda a, b: a + b
print(somma(2, 3)) # 5



#Mappare: applicare una funzione su ciascun elemento di una sequenza.
#map(f, collection)
#applica la funzione f a tutti gli elementi della collezione

lista_numeri = [1,3,6]
dizionario_numeri_stringhe = {0: "zero", 1: "uno", 2: "due", 3: "tre", 4:
"quattro", 5: "cinque", 6: "sei", 7: "sette", 8: "otto", 9: "nove"}
list_comp =[dizionario_numeri_stringhe[n] for n in lista_numeri]
list_con_map = list(map(lambda n: dizionario_numeri_stringhe[n], lista_numeri))
print(list_comp, list_con_map)


#Filtrare: selezionare alcuni elementi di una lista per formare una sottolista
lista =[1,2,3,4,5,6,7,8,9]
list_comp = [n for n in lista if n%2==0]
list_con_filter = list(filter(n%2==0, lista))
print(list_comp, list_con_filter)


#reduce(f, collection)
#usa la funzione f (che ha due argomenti) per ridurre la collezione ad un solo valore:

#Esempio di grafico con matplolib
import matplotlib.pyplot as plt
import random
y = [random.randint(1, 100) for _ in range(10)]
# Plot dei dati
plt.figure(figsize=(12, 6))
plt.plot(y, marker='o', linestyle='-', label='ettichetta')
plt.title('Grafico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()