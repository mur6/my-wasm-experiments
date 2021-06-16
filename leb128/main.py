import io
import leb128

# unsigned leb128
assert leb128.u.encode(624485) == bytearray([0xe5, 0x8e, 0x26])
assert leb128.u.decode(bytearray([0xe5, 0x8e, 0x26])) == 624485
assert leb128.u.decode_reader(io.BytesIO(bytearray([0xe5, 0x8e, 0x26]))) == (624485, 3)

# signed leb128
assert leb128.i.encode(-123456) == bytearray([0xc0, 0xbb, 0x78])
assert leb128.i.decode(bytearray([0xc0, 0xbb, 0x78])) == -123456
assert leb128.i.decode_reader(io.BytesIO(bytearray([0xc0, 0xbb, 0x78]))) == (-123456, 3)

print("unsigned leb128")
print(leb128.u.encode(12))
