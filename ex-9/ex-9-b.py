import threading, time
from numpy.random import seed
from numpy.random import randint


init_time = float(time.time())

def factorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def slice_vector(num_list, fat_list, start, end):
    for num in num_list[start:end]:
        fat_list.append(factorial(num))


def generate_array_or_random_integers(qtd):
    seed(1)
    return randint(1, 6, qtd)


global end_time

def calc_factorial_in_threads():
    n_thread = 4
    array_a = generate_array_or_random_integers(10000000)

    divide_list_by_thread = len(array_a) / n_thread

    array_b = []

    for index in range(n_thread):
        start = int(index * divide_list_by_thread)
        end = int((index + 1) * divide_list_by_thread)

        thread = threading.Thread(target=slice_vector, args=(array_a, array_b, start, end))
        thread.start()
        thread.join()

    print("---------- ARRAY DE FATORIAIS ----------")
    print(array_b)
    print("----------------- FIM ------------------")    


calc_factorial_in_threads()

end_time = float(time.time())

print(end_time - init_time)

# N = 1.000.000 = 3.4 segundos
# N = 5.000.000 = 18.14 segundos
# N = 10.000.000 = 32.5 segundos