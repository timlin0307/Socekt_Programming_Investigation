import socket

addr = '127.0.0.1'
port_self = 5405
port_destin = 5407

sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind((addr, port_self))

while True:
    # 32768 is max string length
    data, address_client = sock_recv.recvfrom(32768)

    if len(data) > 0:
        print("Receive", data, "from proxy")
        # get string number
        index = int(str(data).replace('b', '')[7:len(str(data))-2])

        sock_send.sendto(b'World %d' % index, (addr, port_destin))
        print("Send", data, "to client")
