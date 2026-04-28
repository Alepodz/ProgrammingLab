data= "2025-06-01"
parti=data.split("-")
print(parti)

my_list = ["marco", "irene", "paolo"]
for i in range(len(my_list)):
 print(my_list[i])

my_list = ["marco", "irene", "paolo"]
for item in my_list:
 print(item)

 #Scrivete una funzione che sommi tutti gli elementi di una lista
def somma_lista(lista):
  sum=0
  for item in lista:
        sum+=item
  return sum
 
print(somma_lista([1,2,3,4,5]))
