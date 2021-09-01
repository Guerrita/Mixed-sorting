import MixedSort as mx
from time import time
import random

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """

    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret

    return wrapper


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    prueba = []
    for i in range(60):
        prueba.append(random.randint(0,200))
    print("Lista desordenada\n" + str(prueba))
    listaPruebaOrdenada = mx.bucketSort(prueba)
    print("Lista ordenada\n" +str(listaPruebaOrdenada))
    numeros = []
    for i in range(1000000):
        numeros.append(random.randint(0,100000000))
    start_time = time()
    mx.bucketSort(numeros)
    elapsed_time = time() - start_time
    print("Numero de datos " + str(len(numeros)))
    print("Tiempo transcurrido: %.10f segundos." % elapsed_time)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
