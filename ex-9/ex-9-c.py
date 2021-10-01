from multiprocessing import Process, Queue
from numpy.random import seed
from numpy.random import randint
import itertools
import time

init_time = float(time.time())

def factorial(n):
  fat = n
  for i in range(n - 1, 1, -1):
      fat = fat * i
  return fat

def generate_array_or_random_integers(qtd):
  seed(1)
  return randint(1, 6, qtd)

def populate_factorial_list(a_list, q):  
  b_list = []
  for num in a_list:
    b_list.append(factorial(num))
  q.put(b_list)


def calc_factorial_in_process():
  array_a = generate_array_or_random_integers(10000000)
  array_b = []
  q1 = Queue()
  process_list = []
  divide_list_by_process = len(array_a) / 4

  if __name__ == "__main__":
    
    for index in range(4):
      start = int(index * divide_list_by_process)
      end = int((index + 1) * divide_list_by_process)

      proc = Process(target=populate_factorial_list, args=(array_a[start:end], q1))

      process_list.append(proc)
      proc.start()      
    
    for j in process_list:
      array_b.append(q1.get())
      j.join()

    array_b = list(itertools.chain.from_iterable(array_b))
    print(array_b)      
  
        


calc_factorial_in_process()

end_time = float(time.time())
print(end_time - init_time)

# N 1.000.000 = 6.7s
# N 5.000.000 = 26s
# N 10.000.000 = 53s