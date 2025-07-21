def encode(x):
    return (' '.join(format(ch, 'b') for ch in bytearray(x, encoding='utf8')))

table: list = ["a","b","c","d","e","f"]

def create_bin(table):
    table = [bytes(item, "utf8") for item in table]
    with open("./bin/tab.bin", "wb") as f:
        lines = f.write(encode(table))
        print(lines)

create_bin(table)