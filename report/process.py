import psutil
from tabulate import tabulate

def check_process(process_name):
    """Check if a process is running and display its information in a table."""
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
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if process_found:
        # Print the process information in a table format
        print(tabulate(process_info_list, headers=["Process ID", "Process Name", "Status", "Created Time", "Memory (MB)"], tablefmt="grid"))
    else:
        print(f"No process found with the name '{process_name}'.")

def main():
    process_name = input("Enter the name of the process to check: ")
    check_process(process_name)

if __name__ == "__main__":
    main()
