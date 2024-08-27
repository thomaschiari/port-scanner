import socket
import threading
import ipaddress
from tkinter import Tk, Label, Entry, Button, Text, END

KNOWN_PORTS = {
    20: "FTP Data Transfer",
    21: "FTP Command Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def scan_port(host, port, output):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            service = KNOWN_PORTS.get(port, "Unknown Service")
            if result == 0:
                output.insert(END, f"Port {port} is open: service {service} \n")
            else:
                output.insert(END, f"Port {port} is closed: service {service} \n")
    except Exception as e:
        output.insert(END, f"Error: {str(e)} on port {port} \n")

def scan_all_ports(host, start_port, end_port, output):
    output.delete(1.0, END)
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port, output))
        thread.start()

def start_scan(host_entry, start_port_entry, end_port_entry, output):
    host = host_entry.get()
    if not host:
        output.insert(END, "Host or IP is required.\n")
        print("Host or IP is required.")
        return
    
    try:
        ipaddress.ip_address(host)
    except ValueError:
        output.insert(END, "Invalid IP address.\n")
        print("Invalid IP address.")
        return

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port < 0 or end_port < 0 or start_port > 65535 or end_port > 65535:
            raise ValueError("Port numbers must be between 0 and 65535.")
        if start_port > end_port:
            output.insert(END, "Start port must be less than or equal to end port.\n")
            print("Start port must be less than or equal to end port.")
            return
        scan_all_ports(host, start_port, end_port, output)
    except ValueError as ve:
        output.insert(END, f"Invalid port range: {ve}\n")
        print(f"Invalid port range: {ve}")

def main():
    root = Tk()
    root.title("TCP Port Scanner")
    
    Label(root, text="Host or IP:", bg="black", fg="white").grid(row=0, column=0, padx=10, pady=5)
    host_entry = Entry(root, bg="white", fg="black")
    host_entry.grid(row=0, column=1, padx=10, pady=5)
    
    Label(root, text="Start Port:", bg="black", fg="white").grid(row=1, column=0, padx=10, pady=5)
    start_port_entry = Entry(root, bg="white", fg="black")
    start_port_entry.grid(row=1, column=1, padx=10, pady=5)
    
    Label(root, text="End Port:", bg="black", fg="white").grid(row=2, column=0, padx=10, pady=5)
    end_port_entry = Entry(root, bg="white", fg="black")
    end_port_entry.grid(row=2, column=1, padx=10, pady=5)
    
    output = Text(root, width=50, height=15, bg="white", fg="black")
    output.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    Button(root, text="Start Scan", command=lambda: start_scan(host_entry, start_port_entry, end_port_entry, output)).grid(row=3, column=0, columnspan=2, pady=5)
    
    root.mainloop()

if __name__ == '__main__':
    main()