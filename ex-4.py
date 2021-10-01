
try:
    file = open('ex-4/ex-4.txt', 'r')
except:
    file = open('ex-4/ex-4.txt', 'w+')
    file.write("Bom dia\nComo vai você? Tudo bem")
    file.close()
    file = open('ex-4/ex-4.txt', 'r')
# file = open('ex-4/ex-4.txt', 'r')

# line_list = []

# for line in file:
#     line_list.append(line)


# for i in range(len(line_list)-1, -1, -1):
#     line_content = line_list[i]
#     print(line_content[::-1])

line_list = []

for line in file:
    line_list.append(line)


line_list.reverse()

for i in line_list:
    print(i[::-1])

file.close()