import socket

class ssocket:
	# Siddharth Socket

	def __init__(self,sock=None):
		self.CHUNK_SIZE=512
		if sock is None:
			self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		else:
			self.sock=sock

	def connect(self,host,port):
		self.sock.connect((host,port))
	
	def send(self,msg):
		msg_len=str(len(msg)).zfill(12) # can represent upto 1TB of data
		self.sock.send(msg_len)
		len_sent=0
		while len_sent!=len(msg):
			sent=self.sock.send(msg[len_sent:])
			if sent==0:
				raise RuntimeError("Socket Connection broken")
			len_sent+=sent
		return len(msg)

	def send_file(self,file_path):
		with open(file_path,"r+") as f:
			file_data=f.read(self.CHUNK_SIZE)
			position=0
			while file_data:
				position+=self.send(file_data)
				f.seek(position)
				file_data=f.read(self.CHUNK_SIZE)
			

	def recv(self):
		msg=""
		msg_len_str=self.sock.recv(12)
		if msg_len_str=="":
			return ""
		msg_len=int(msg_len_str)
		len_recv=0
		while len_recv!=msg_len:
			recv_msg=self.sock.recv(msg_len-len_recv)
			if recv_msg==0:
				raise RuntimeError("Socket Connection broken")
			len_recv+=len(recv_msg)
			msg=msg+recv_msg
		return msg

	def recv_file(self,file_path):
		with open(file_path,"w+") as f:
			file_data=self.recv()
			while file_data:
				f.write(file_data)
				file_data=self.recv()


