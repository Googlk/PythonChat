import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '192.168.0.211'
port = 18702
ADDR = (ip,port)
s.bind((ADDR))
s.listen(10)
IPLISTS = ['182.92.103.85']
IPVERSION = '0.0.1'
while True:
    test,addrs = s.accept()
    if len(addrs) != 0:
        
        s.send(IPVERSION.encode('utf-8'))
