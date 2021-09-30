file = open('ex-4/ex-4.txt', 'r')

line_list = []

for line in file:
    line_list.append(line)


for i in range(len(line_list)-1, -1, -1):
    line_content = line_list[i]
    print(line_content[::-1])

