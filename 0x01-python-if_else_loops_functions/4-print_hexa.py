#!/usr/bin/python3
for i in range(0, 99):
    hex1 = i % 16
    if (i < 16):
        continue
    else:
        hex2 = (i//16) % 16
    if hex1 > 9:
        hex1 = chr(hex1 + 87)
    elif hex2 > 9:
        hex += chr(hex1 + 87)
    else:
        hex1 = hex1
        hex2 = hex2
    print("{} = 0x{}{}".format(i, hex2, hex1))
