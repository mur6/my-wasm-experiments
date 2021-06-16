with open("main.wasm", "wb") as f:
    b1 = bytearray.fromhex('0061736d')
    b2 = bytearray.fromhex('01000000')
    b3 = bytearray.fromhex('0c00')
    print(b1 + b2 + b3)
    f.write(b1 + b2 + b3)
