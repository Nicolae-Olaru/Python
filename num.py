import numpy as array_definition
# variable = array_definition.array
array = array_definition.array([20,50,11,22,34,65])
print("Array ->")
print(array)
print(".................................")
print("Cambio valore di positione: 0")
print(array[0])
array[0] = 900
print(array[0])
print(".................................")
print("Aggoingere un valore ad ogni positione ")
print(array +5)
print("operazione in print cioe non cambia il valore default")
print(".................................")
print(array)
print(".................................")
print("Sottrare ad ogni positione valore di 10")
print(array - 10)
print("operazione in print cioe non cambia il valore default")
print(".................................")
array = array -10
print(array)
print("Adesso cambio proprio")
print(array)
print(".................................")
print("Funzione somma in print")
print(array.sum())
print(".................................")
risultato = array.sum()
print(risultato)
print("Funzione somma salvato in una variabile")
print(".................................")
array1 = array_definition.array([10,20])
array2 = array_definition.array([10,20])
print(array1 + array2)
print(".................................")
print("Data type")
print(array.dtype)
print(".................................")
new_array = array_definition.array([5,4,3,2,1,0],dtype = array_definition.float64)
print(new_array)
print("array,float")
print(".................................")
sum = array_definition.add(array1,array2)
print(sum)
print("somma 2 array tra di loro")
print(".................................")
sum1 = array_definition.sum(array1)
print(sum1)
print("Somma di un intero array e ris in una var")
print(".................................")
amp = array_definition.sqrt(array1)
print(amp)
print("Radice quadrata di ogni elemento di una array")
print(".................................")
spazio = array1.T 
print(spazio)
print("Ritorna alla normalita")
print(".................................")