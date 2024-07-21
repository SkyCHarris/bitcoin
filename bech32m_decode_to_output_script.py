from bitcoin.segwit_addr import *
from binascii import unhexlify

_ = decode("bc", "bc1q9d3xa5gg45q2j39m9y32xzvygcgay4rgc6aaee")
print(_[0], bytes(_[1]).hex())

_ = decode("bc", "bc1p9nh05ha8wrljf7ru236awm4t2x0d5ctkkywmu9sclnm4t0av2vgs4k3au7")
print(_[0], bytes(_[1]).hex())