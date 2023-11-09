# writing
with open("binary", 'bw') as binary_file:
    binary_file.write(bytes(range(17)))

# reading
with open("binary", 'br') as binary_file:
    for b in binary_file:
        print(b)

a = 65534       #FF FE
b = 65535       #FF FF
c = 65536       # 00 01 00 00
d = 2998392     # 02 2D C0 1e

with open("binary2", 'bw') as binary_file:
    # to_bytes(number of bytes, edian)
    binary_file.write(a.to_bytes(2, 'big'))
    binary_file.write(b.to_bytes(2, 'big'))
    binary_file.write(c.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'big'))
    binary_file.write(d.to_bytes(4, 'little'))

with open("binary2", 'br') as binary_file:
    e = int.from_bytes(binary_file.read(2), 'big')
    print(e)
    f = int.from_bytes(binary_file.read(2), 'big')
    print(f)
    g = int.from_bytes(binary_file.read(4), 'big')
    print(g)
    h = int.from_bytes(binary_file.read(4), 'big')
    print(h)
    i = int.from_bytes(binary_file.read(4), 'little')
    print(i)
