import socket

print("this is a sample socket run")

s = socket.socket()

print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))

s.send(request.encode())

result = s.recv(2048)

while len(result) > 0 :
    print(result)
    result = s.recv(2048)