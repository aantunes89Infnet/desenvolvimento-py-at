import psutil as ps


def get_process_name(process_list):
    for process in process_list:
        if ps.pid_exists(process.pid) and process is not None:
            print(f"O nome deste processo é: {process.name()}")


process_info_list = ps.process_iter()

get_process_name(process_info_list)
