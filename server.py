from ssocket import ssocket
import os
from sys import exit,argv

host="localhost"
port=6601

ss=ssocket()
ss.sock.bind((host,port))
ss.sock.listen(5)
file_path=argv[1]
file_name=file_path.split("/")[-1]
while True:
	try:
		(cs_sock,client_adr)=ss.sock.accept()
		cs=ssocket(cs_sock)
		msg=cs.send(file_name)
		cs.send_file(file_path)
		cs.sock.close()
	except KeyboardInterrupt:
		cs.sock.close()
		ss.sock.close()
		print "Exiting server ..."
		exit(0)

ss.sock.close()
