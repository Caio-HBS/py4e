import socket

rawurl = input('Say what URL you want to connect to: ')
hostname = rawurl.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = 'GET rawurl HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
