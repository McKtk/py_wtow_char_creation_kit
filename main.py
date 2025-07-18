from tkinter import *

def encode(x):
    return (' '.join(format(ch, 'b') for ch in bytearray(x, encoding='utf8')))

def decode(x):
    return (''.join(chr(int(b, 2)) for b in x.split()))

def Read_origins():
    Origin = []
    with open("./origin.bin", "rb") as f:
        lines = f.read().decode('utf-8')
        decoded = decode(lines)
        print(decoded)
        for line in decoded.splitlines():
            Origin.append(line)
            
    return Origin

print(Read_origins())
