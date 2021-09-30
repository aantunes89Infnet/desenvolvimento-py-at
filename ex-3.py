import os

dirpath = input("Digite o nome do diretório: ")

is_dir = os.path.isdir(dirpath)

file_structure = dict()

if not is_dir:
    os.mkdir(dirpath)

for f in os.listdir():
    file_structure[f] = os.stat(f).st_size

file = open(f"{dirpath}/new.txt", 'w')

for k, v in file_structure.items():
    file.write(f"{k}: {v} bytes \n")

file.close()


# SORTING

sorted_file = open(f"{dirpath}/sorted.txt", "w")

sorted_dict = dict()

for el in sorted(file_structure.items(),key = lambda kv:(kv[1], kv[0])):
    sorted_dict[el[0]] = el[1]

print(sorted_dict)

for k, v in sorted_dict.items():
    sorted_file.write(f"{k}: {v} bytes \n")

sorted_file.close()


#

