import socket
import tkinter as tk
from tkinter import messagebox

# UDP Client Configuration
server_address = ('localhost', 12345)

def send_number():
    """ Sends the entered number to the server and waits for the response. """
    try:
        number = int(entry.get())
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(str(number).encode(), server_address)

        # Receive response from server
        data, _ = client_socket.recvfrom(1024)
        result_label.config(text=f"Server Response: {data.decode()}")

        client_socket.close()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Create GUI Window
root = tk.Tk()
root.title("UDP Client")
root.geometry("300x200")

# GUI Elements
tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_number)
send_button.pack(pady=5)

result_label = tk.Label(root, text="Waiting for response...")
result_label.pack(pady=5)

# Run the GUI
root.mainloop()
