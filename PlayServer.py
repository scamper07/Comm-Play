import socket
import time
import sys
from datetime import datetime
from thread import start_new_thread
import threading

# host_ip = "10.0.0.1"
host_ip = "127.0.0.1"
host_port = 9000

client_number = 0
client_name = []
client_ip = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "* Socket created successfully!"
time.sleep(1)

s.bind((host_ip, host_port))
print "* Bind complete"
time.sleep(1)

s.listen(10)
print "* Server is now listening"
time.sleep(1)

print "* Waiting for devices to connect..."
time.sleep(1)

local = threading.local()


def client_thread(conn):
    local.client_number = client_number
    local.name = conn.recv(1024)
    local.address = address[0]
    print "Device name : " +local.name
    print "Device IP   : " +local.address +"\n"

    while True:
        data = conn.recv(1024)
        if data == "end":
            sys.exit()
        now = datetime.now()
        timestamp = now.strftime("%d %b %Y %H:%M:%S")
        print "[Player-" +str(local.client_number) +" " +timestamp +" " +local.address +"]" +" : " +data

while True:
    conn, address = s.accept()
    print "\nConnected with " + address[0] + ":" + str(address[1])
    conn.send("\n" + "[" + host_ip + "]" + " : " + "Welcome to the Community Play!")
    start_new_thread(client_thread, (conn,))
    client_number += 1

# s.close()
