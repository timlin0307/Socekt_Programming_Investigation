import socket
import random
import time

addr = '127.0.0.1'
port_self = 5406
port_destin = 5405

sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind((addr, port_self))

while True:
    # 32768 is max string length
    data, address_server = sock_recv.recvfrom(32768)

    if len(data) > 0:
        print("Receive", data, "from client")
        sock_send.sendto(data, (addr, port_destin))
        print("Forward", data, "to server")
