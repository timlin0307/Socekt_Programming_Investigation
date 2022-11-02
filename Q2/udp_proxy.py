import socket
import random
import time

addr = '127.0.0.1'
port_self = 5406
port_destin = 5405

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((addr, port_self))

while True:
    # 32768 is max string length
    data, address_server = sock.recvfrom(32768)

    if len(data) > 0:
        print("Receive", data, "from client")
        # get string number
        index = int(str(data).replace('b', '')[7:len(str(data))-2])

        # number is even or odd
        if index % 2 == 0:  # if number is even
            prob1 = random.randint(0, 9999)
            # 90% can forward data successfully
            if prob1 > 999:
                sock.sendto(data, (addr, port_destin))
                print("Forward", data, "to server without loss")
            else:
                print("Forward nothing to server")
        else:  # if number is odd
            prob2 = random.randint(0, 9999)
            # 5% have 100ms delay
            if prob2 < 500:
                print("Forward", data, "to server with delay")
                time.sleep(0.1)
                sock.sendto(data, (addr, port_destin))
            else:
                print("Forward", data, "to server without delay")
                sock.sendto(data, (addr, port_destin))
