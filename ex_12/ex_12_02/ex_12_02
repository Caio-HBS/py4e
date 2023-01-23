import socket
count = 0


rawurl = input('Say what URL you want to connect to: ')
if len(rawurl) < 1:
    rawurl = 'http://www.google.com'
hostname = rawurl.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = 'GET rawurl HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while count < 3000:
    data = mysock.recv(512)
    words = data.decode().rstrip()
    print(words)
    for letters in words:
        letters = words.split()
        count = count + 1
    if len(data) >= 1:
        break
mysock.close()
print(count)