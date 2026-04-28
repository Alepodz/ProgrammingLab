# Esercizio 1
dato=538
ora=dato//60
minuti=dato%60
print('h',ora,'m',minuti)

#Esercizio 2
print('dammi un numero')
num=int(input())
print(num*num, num*num*num)

#esercizio 3
print('dammi un numero')
num=int(input())
if num%2==0:
    print('pari')
else:
    print('dispari')

#esercizio 4
def cipipi(lettera, parola):
    i=0
    k=0
    n=len(parola)

    while k<n:
        if parola[k]==lettera:
            i+=1

        k+=1    

    return i


print('dammi una parola')
parola=input()
print('dammi una lettera')
lettera=input()
k=cipipi(lettera, parola)
print(k)

#esercizio5
print('dammi un numero')
num=int(input())
n=num-1
while n>1:
    if (num%n)==0:
        print('non è primo')
        break
    n=n-1
else:
    print('è primo')


#esercizio6  
sum=0
while num!=0:
    print('dammi un numero')
    num=int(input())
    sum+=num    
print(sum)

#esercizio7
def fattoriale(num):
    molt=1
    prod=num
    while molt<=num:
        prod*=molt
        molt+=1
    return prod

#esercizio8
def e_triangolo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
print('dammi tre numeri')
a=int(input())
b=int(input())
c=int(input())
if e_triangolo(a, b, c):
    print('è un triangolo')
else:
    print('non è un triangolo')


#esercizio9
def conta_vocali(parola):
    vocali='aeiouAEIOU'
    count=0
    for lettera in parola:
        if lettera in vocali:
            count+=1
    return count
print('dammi una parola')
parola=input()
print(conta_vocali(parola))

