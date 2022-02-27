S = 0

# num =3

# S |= (1<<num)
# S |= (1<<num)
# S ^= (1<<num)
S |= (1<<21) -1
print(bin(S & (1<<20)))
# S ^= (1<<4)
# print(bin(S))
# print(bin(S& (1<<2)) == bin(0))