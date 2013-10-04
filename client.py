from ssocket import ssocket
import os

server="localhost"
port=6601
ss=ssocket()
ss.connect(server,port)
file_name=ss.recv()
print file_name
ss.recv_file(file_name)
ss.sock.close()
