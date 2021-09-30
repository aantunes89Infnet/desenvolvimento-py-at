first = open('ex-5/a.txt', 'r')
second = open('ex-5/b.txt', 'r')

first_lines = []
second_lines = []

for line in first:
    first_lines.append(line)

for line in second:
    second_lines.append(line)

calc_first = first_lines[0].split()
calc_second = second_lines[0].split()

if len(calc_first) > len(calc_second):
    result = len(calc_first) - len(calc_second)
    for i in range(result):
        calc_second.append("0")
elif len(calc_second) > len(calc_first):
    result = len(calc_second) - len(calc_first)
    for i in range(result):
        calc_first.append("0")


for el in range(len(calc_first)):
    print(int(calc_first[el]) + int(calc_second[el]))
