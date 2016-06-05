import socket

print ('Server is listening on 0.0.0.0:6789')
print ('Connection address: 192.168.0.10')
print ('client connected, id: 46487286447564')

TCP_IP = '127.0.0.1'
TCP_PORT = 6789
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Initialization complete, server is listening on port 6789')
print ('Connection address:', addr)
print ('client connected, id: 46487286447564')
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()