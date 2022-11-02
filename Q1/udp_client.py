import socket

addr = '127.0.0.1'
port_self = 5407
port_destin = 5406

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((addr, port_self))

for i in range(10000):
    data = b'Hello %d' % (i+1)
    sock.sendto(data, (addr, port_destin))
    print("Send", data, "to proxy")

    while True:
        try:
            # 32768 is max string length
            data, address_server = sock.recvfrom(32768)

            # if data is not null
            if len(data) > 0:
                # get string number
                index = int(str(data).replace('b', '')[7:len(str(data))-2])

                if index == i+1:  # confirm Hello x = World x
                    print("Receive", data, "from server")
                    break

        except socket.timeout:
            sock.sendto(data, (addr, port_destin))
            print("Re-Send ", data, " to proxy")
