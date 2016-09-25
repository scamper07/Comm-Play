import socket
import time
import subprocess
#import netifaces
import sys

host_ip = "192.168.1.103"
#host_ip = "127.0.0.1"
host_port = 9000
#device_ip =netifaces.ifaddresses('wlan0')[2][0]['addr']

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "* Socket created successfully!"
time.sleep(1)

s.connect((host_ip, host_port))
print "* Connection complete!"
time.sleep(1)

data = s.recv(1024)
print data

print "* Sending client details."
result = subprocess.check_output("hostname")
s.send(result.strip("\n"))

while True:
    try:
        key_data = raw_input("Enter command: ")
        #print "[" +device_ip +"]" + " : " + str(key_data)
        s.send(str(key_data))
    except KeyboardInterrupt:
        print "\nForce stopping client!"
        s.send("end")
        sys.exit()

#s.close()
