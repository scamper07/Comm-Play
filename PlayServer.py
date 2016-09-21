import socket
import time
from datetime import datetime
from thread import start_new_thread
import threading
import pykeyboard

host_ip = "192.168.1.103"
#host_ip = "127.0.0.1"
host_port = 9000

client_number = 0
client_name = []
client_ip = []
k = pykeyboard.PyKeyboard()

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


def key_action(data):
    if data == 'w':
        k.press_key('w')
        time.sleep(0.25)
        k.release_key('w')
    elif data == 's':
        k.press_key('s')
        time.sleep(0.25)
        k.release_key('s')
    elif data == 'a':
        k.press_key('a')
        time.sleep(0.25)
        k.release_key('a')
    elif data == 'd':
        k.press_key('d')
        time.sleep(0.25)
        k.release_key('d')
    elif data == 'n':
        k.press_key('n')
        time.sleep(0.25)
        k.release_key('n')
    elif data == 'm':
        k.press_key('m')
        time.sleep(0.25)
        k.release_key('m')
    elif data == 'j':
        k.press_key('j')
        time.sleep(0.25)
        k.release_key('j')
    elif data == 'k':
        k.press_key('k')
        time.sleep(0.25)
        k.release_key('k')
    elif data == 'i':
        k.press_key('i')
        time.sleep(0.25)
        k.release_key('i')
    elif data == 'o':
        k.press_key('o')
        time.sleep(0.25)
        k.release_key('o')
    else:
        print "Invalid!"


def client_thread(conn):
    local.client_number = client_number
    local.name = conn.recv(1024)
    local.address = address[0]
    print "Device name : " +local.name
    print "Device IP   : " +local.address +"\n"

    while True:
        data = conn.recv(1024)
        key_action(data)
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
#test1