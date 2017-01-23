import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
connection, addr = s.accept()
while True:
	data = connection.recv(1024)
	if len(data) > 1024 or data == "close" or not data:
		connection.close()
		break
	else:
		connection.send(data)
		print data