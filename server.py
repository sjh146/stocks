import socket as sc
#192.168.45.16
print("1.소켓생성")
sock=sc.socket(sc.AF_INET,sc.SOCK_STREAM)

print("2.바인딩")
sock.bind(("",9700))

print("3.접속대기")
sock.listen()

print("4.접속수락")
c_sock, addr=sock.accept()

print("5.데이터수신")
read_data=c_sock.recv(1024)

print("수신:{}".format(read_data))

print("6.접속종료")
c_sock.close()
sock.close()