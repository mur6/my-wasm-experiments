import leb128

def conv_leb128(num):
    leb128_byte_array = leb128.u.encode(num)
    return ",".join(f"{b:02x}" for b in leb128_byte_array)

def main():
    for i in range(300):
        h = '{:02x}'.format(i)
        q = conv_leb128(i)
        print(f"{i:03}\t0x{i:04x}\tLEB128=[{q}]")

if __name__ == "__main__":
    main()
