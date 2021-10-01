import psutil as ps

#mac
def get_cpu_percent_and_memory_info():
    cpu_list = ps.cpu_percent(interval=1, percpu=True)
    print("-------CPU % --------")
    for i in cpu_list:
        print(f"{i}%")
    print("-------Memory use--------")
    v_memory = ps.virtual_memory()
    print(f"Uso de memória: {v_memory.percent}%")


get_cpu_percent_and_memory_info()

# windows
# def get_cpu_percent_and_memory_info(process_list):
#     counter = 0
#     for process in process_list:
#         if ps.pid_exists(process.pid) and process is not None:
#             print(f"Porcentagem de memória é : {process.memory_percent()}")
#             print(f"Porcentagem de CPU é: {process.cpu_percent(interval=1.0)}")
#             counter += 1
#             if counter > 10:
#                 break

# process_info_list = ps.process_iter()

# get_cpu_percent_and_memory_info(process_info_list)
