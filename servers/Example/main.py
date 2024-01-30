import os
import db 
import sys
import socket
import UserManager as um
from   _thread import *
from   dotenv  import load_dotenv as ld

#hope some day validate Assets from the server side


def Init():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ld()
    server = os.getenv("server")
    port = int(os.getenv("port"))

    try:
        s.bind((server, port))
    except socket.error as e:
        print(str(e))

    print("Server Started")

    s.listen()

    print("Waiting for a connection...")

def Client(conn : socket.socket):
    reply = ""
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                reply = data
            
            print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            print("Error")
            break

def main():
    Bans : dict = um.LoadBans()
    Db = db.DataBase()
    Init()
    try:
        while True:
            conn, addr = s.accept()
            print("New Conection!")
            print("Connected to:", addr)

            if addr in Bans["ips"]:
                print("this ip was Banned")
            else:
                start_new_thread(Client, (conn,))
    except:
        print("Error")
        um.SaveBans(Bans)