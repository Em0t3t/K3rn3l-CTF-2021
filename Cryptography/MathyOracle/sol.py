from Crypto.Util.number import getPrime
from pwn import *
# primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 

aa=[]
nn = []


r = remote("ctf.k3rn3l4rmy.com", 2234)

u = r.recvline()
print(u)
for _ in range(600):
    print("Luot {}:".format(_+1))
    u = r.recvline()
    print(u)
    u = r.recv()
    need_send = 0
    if(_<598):
        need_send = 1
    else:
        need_send = getPrime(256)
        nn.append(need_send)
    print("Luot {0} co gia tri la: {1}".format(_+1,need_send))
    
    r.sendline(str(need_send).encode())
    u = r.recv()
    r.sendline(str(need_send).encode())
    u = r.recvline()
    hh = u.decode()
    print(hh)
    so=0
    for kk in hh:
        if(kk>='0' and kk<='9'):
            so=so*10+int(kk)
    if(_>=598):
        aa.append(so)
    if(_==599):
        print(aa)
        print(nn)
    u = r.recvline()
    print(u)
# print(ans)
u = r.recv()
print(u)
