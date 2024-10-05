from fabric import Connection

def ssh_client(hostname, username, password=None):
    # Create a connection
    conn = Connection(host=hostname, user=username, connect_kwargs={"password": password})
    
    try:
        print(f"Connected to {hostname}")

        while True:
            # Get command input from user
            command = input("Enter command (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            
            # Execute command
            result = conn.run(command, hide=True)
            print(result.stdout.strip())
    
    except Exception as e:
        print(f"Connection or command execution failed: {e}")
    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    hostname = input("Enter hostname: ")  # Your server's IP address
    username = input("Enter username: ")    # Your username
    password = input("Enter password: ")    # Your password

    ssh_client(hostname, username, password)
