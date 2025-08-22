import socket
import sys

# Usage: python scanner.py <target_ip>

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python scanner.py <target_ip>")
    sys.exit(1)

# Get the target IP from command-line arguments
target_ip = sys.argv[1]

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print("-" * 50)

try:
    # Iterate over a common range of ports
    for port in range(1, 1025):  # Scans ports 1 through 1024
        # Create a new socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        socket.setdefaulttimeout(1)
        
        # Attempt to connect to the target IP and port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}:    Open")
        
        # Close the socket
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit()

