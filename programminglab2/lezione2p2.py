#1. Indicizzazione booleana
#Creare un nuovo vettore con tutti i numeri primi tra 0 e 20. I numeri primi 
# compresi tra 0 e 20 sono: 2, 3, 5, 7, 11, 13, 17, 19.
#Utilizza un test logico (ad esempio >, <, ==, !=) per selezionare tutte le voci del vettore 
# maggiori di 10.
#Utilizza un test logico per selezionare tutti i numeri primi pari dalla lista.

import numpy as np
np.random.seed(0)
a = np.random.ranf(30).reshape([10, 3])
a = np.random.rand(10, 3)
m = np.argmin(np.abs(a - 0.5), axis=1)
print(m)
a[np.arange(a.shape[0]), m]

#esercizio2


