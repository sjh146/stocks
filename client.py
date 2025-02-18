import socket as scc



print("1.소켓생성")
sock=scc.socket(scc.AF_INET,scc.SOCK_STREAM)

print("3.접속시도")
sock.connect(("192.168.45.16",9700))

print("5.데이터송신")
sock.sendall(bytes("hello socket","UTF-8"))

print("6.접속종료")
sock.close()