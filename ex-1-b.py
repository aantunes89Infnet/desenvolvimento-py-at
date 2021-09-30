import psutil as ps


def get_process_name_and_pid(process_list):
    for process in process_list:
        if ps.pid_exists(process.pid) and process is not None:
            print(f"O nome deste processo é: {process.name()} \n"
                  f"O Seu PID é : {process.pid}")


process_info_list = ps.process_iter()

get_process_name_and_pid(process_info_list)
