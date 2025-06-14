import socket
import time

target = input("Enter host to scan (127.0.0.1 or scanme.nmap.org): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # half-second timeout
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
        time.sleep(0.1)  # delay between attempts
    except socket.gaierror:
        print("Error: Invalid host")
        break
    except ValueError:
        print("Error: Invalid port number")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
