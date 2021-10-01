import random, time

init_time = float(time.time())

def factorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


vector_a = []
vector_b = []

for n in range(1, 10000000):
    vector_a.append(random.randint(1, 20))



for num in vector_a:    
    vector_b.append(factorial(num))

end_time = float(time.time())

print(vector_b)


print(f"TEMPO INICIO {init_time}")
print(f"TEMPO FINAL {end_time}")

print(f"DIFERENÇA = { end_time - init_time }")

# N 1.000.000 = 2.5s
# N 5.000.000 = 12.5s
# N 10.000.000 = 25.14s