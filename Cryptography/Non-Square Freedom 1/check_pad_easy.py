from Crypto.Util.number import *
P=3
def pad_easy(m):
    # m <<= (512//8)
    m<<=64
    m += (-(m % (P**2)) % P)
    return m
# print(pad_easy(5))
print(-(5%9)%3)

## Phan tich
# m1 = m*2^64
# m2 = -(m1%(P^2))%P
# m3 = m1+m2
#m3 = 2^64*m + [-(2^64*m%(P^2))%P]
#m3 = m1 + [-(m1%(P^2))%P]
# FLAG = b'aa'
# print(ord)
# u = int.from_bytes(FLAG,'big')
# print(u)
# print(long_to_bytes(24929)) => int.from_bytes(FLAG,'big') = long_to_bytes()

