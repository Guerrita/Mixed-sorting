import numpy as np;

def bucketSort(lista):
    num_buckets = int(np.sqrt(len(lista)));         #numero de buckets que se tendran
    max_value = max(lista);                         #maximo valor que se tendra en la lista ingresada
    limit_bucket = max_value/num_buckets            #Valor que nos ayudara a determinar en que bucket ira el numero
    bucket = []                                     #Creamos el bucket
    for i in range(num_buckets):
        bucket.append([]);                          #Agregaremos el numero de subbuckets que se tendran dentro del bucket ppal
    for i in lista:
        des_bucket = int(np.floor(i/limit_bucket))  #Encontramos el bucket al que ira el numero
        if des_bucket==len(bucket):                 #si el bucket es mayor que el numero de la lista se le respa 1
            des_bucket-=1
        bucket[des_bucket].append(i)                #se agrega el numero al bucket

    for i in range(len(bucket)):                    #Se ingresa dentro de cada subbucket y los organizamos
        #print(f"Bucket {i} desordenado \n" + str(bucket[i]))       Imprime el bucket desordenado
        quickSort(bucket[i],0,len(bucket[i])-1)
        #print(f"Bucket {i} ordenado \n" + str(bucket[i]))          Imprime el bucket ordenado
    listaOrdenada = []
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            listaOrdenada.append(bucket[i][j])
    return listaOrdenada


def quickSort(arr,low, high):

    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)