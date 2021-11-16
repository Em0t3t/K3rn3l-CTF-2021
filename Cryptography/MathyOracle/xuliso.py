import random
u = b'f(N+l,k) = 5\n'
hh = u.decode()
so=0
for _ in hh:
    if(_>='0' and _<='9'):
        so=so*10+int(_)
print(so)
N = random.getrandbits(512)
print(N)