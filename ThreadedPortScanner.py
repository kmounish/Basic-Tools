import socket
import subprocess
import sys
import threading
from queue import Queue


def scan( port):
	try:		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((r_host,port))
			
		if result ==0:
			print("port {} open".format(port))
			return true
		
		return false
	except KeyboardInterrupt:
		print("Exiting")
		sys.exit()
	except Exception as e:
		pass

def threadWork():
	while not queue.empty():
		port = queue.get()
		scan(port)
	
	
global r_host
r_host= input("Enter host to be scanned: ")
queue = Queue()
threads = []

for port in range(1,1025):
	queue.put(port)

for t in range(100):
	thread = threading.Thread(target=threadWork)
	threads.append(thread)

for thread in threads:
	thread.start()

