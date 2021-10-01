import random


def factorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


vector_a = []

for n in range(1, 20):
    vector_a.append(random.randint(2, 7))


vector_b = []

for num in vector_a:
    vector_b.append(factorial(num))

print(vector_b)
