import socket
import tkinter as tk
import subprocess
from tkinter import scrolledtext
from tkinter import PhotoImage
import webbrowser

def start_server():
    subprocess.Popen(['python', 'servercode.py'])


class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Client Chat")
        
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_area.pack(padx=20, pady=10)
        self.chat_area.config(state=tk.DISABLED)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(padx=20, pady=5, fill=tk.X)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.server_ip = '172.20.10.14'  
        self.server_port = 53441 

        self.connect_to_server()

      
        self.image = PhotoImage(file='image/25231 (2).png')
        self.image_label = tk.Label(master, image=self.image, cursor="hand2")
        self.image_label.pack(pady=10)
        self.image_label.bind("<Button-1>", lambda e: self.open_url("https://github.com/LunarTear9"))

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "Connected to the server\n")
        self.chat_area.config(state=tk.DISABLED)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message.lower() == 'exit':
            self.client_socket.close()
            self.master.quit()
        else:
            self.client_socket.send(message.encode())
            data = self.client_socket.recv(1024)
            self.display_message(f"Server: {data.decode()}")

    def display_message(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)
        self.message_entry.delete(0, tk.END)

    def open_url(self, url):
        webbrowser.open_new(url)


if __name__ == "__main__":
    start_server()
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
