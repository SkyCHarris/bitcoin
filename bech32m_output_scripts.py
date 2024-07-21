from bitcoin.segwit_addr import *
from binascii import unhexlify


print(encode('bc', 0, unhexlify('2b626ed108ad00a944bb2922a309844611d25468')))
print(encode('bc', 0, unhexlify('648a32e50b6fb7c5233b228f60a6a2ca4158400268844c4bc295ed5e8c3d626f')))
print(encode('bc', 1, unhexlify('2ceefa5fa770ff24f87c5475d76eab519eda6176b11dbe1618fcf755bfac5311')))
print(encode('bc', 16, unhexlify('0000')))