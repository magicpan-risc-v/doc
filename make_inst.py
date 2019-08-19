import struct

file_name = input('?')
fin = open(file_name, 'rb')
mem_out = open('mem.bin', 'wb')
ext_out = open('ext.bin', 'wb')

data = fin.read()
idx = 0
for byte in data:
    char = struct.pack("B", byte)
    if ((idx & 4) != 0):
        mem_out.write(char)
    else:
        ext_out.write(char)
    idx += 1

fin.close()
mem_out.close()
ext_out.close()
