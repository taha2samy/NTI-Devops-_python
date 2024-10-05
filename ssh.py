import paramiko

def ssh_client(hostname, username, password):
    try:
        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        client.connect(hostname, username=username, password=password)
        print(f"Connected to {hostname}")

        output_content = ""

        while True:
            # Get command input from user
            command = input("Enter command (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            
            # Execute command
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
            print(output)
            output_content += output + "\n"

    except Exception as e:
        print(f"Connection failed: {e}")
    finally:
        client.close()
        print("Connection closed.")


if __name__ == "__main__":
    hostname = input("Enter hostname: ")  # Your server's IP address
    username = input("Enter username: ")    # Your username
    password = input("Enter password: ")    # Your password

    ssh_client(hostname, username, password)
