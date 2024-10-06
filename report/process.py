import psutil
from tabulate import tabulate

def check_process(process_name):
    process_found = False
    process_info_list = []

    for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_info']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                process_found = True
                process_info_list.append([
                    proc.info['pid'],
                    proc.info['name'],
                    proc.info['status'],
                    proc.info['create_time'],
                    proc.info['memory_info'].rss // (1024 * 1024)  # Convert to MB for readability
                ])

        except (psutil.NoSuchProcess):
            continue
        except(psutil.AccessDenied):
            continue



    if process_found:
        
        print(tabulate(process_info_list, headers=["Process ID", "Process Name", "Status", "Created Time", "Memory (MB)"], tablefmt="latex"))
    else:
        print(f"No process found with the name '{process_name}'.")

def main():
    process_name = input("Enter the name of the process to check: ")
    check_process(process_name)

main()
