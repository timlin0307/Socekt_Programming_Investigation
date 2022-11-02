import socket
from ast import Bytes

addr = '127.0.0.1'
port_self = 5405
port_destin = 5407

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((addr, port_self))

while True:
    # 32768 is max string length
    data, address_client = sock.recvfrom(32768)

    if len(data) > 0:
        print("Receive", data, "from proxy")
        # get string number
        index = int(str(data).replace('b', '')[7:len(str(data))-2])

        sock.sendto(b'World %d' % index, (addr, port_destin))
        print("Send", data, "to client")
