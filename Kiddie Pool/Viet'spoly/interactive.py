from pwn import * 

r = remote("ctf.k3rn3l4rmy.com",2236)

u = r.recvline()
u = r.recvline()
u = r.recvline()
u = r.recvline()
for _ in range(0,100):
    print("Luot {0}: ".format(_))
    u = r.recvline()
    leng = len(u)
    print(u)
    print(leng)
    u = r.recvline()
    mlenu = len(u)
    u = u[:mlenu-2]
    u=u.decode()
    print(u)
    ## leng = 71: res = (-1)*th//fo 
    ## leng = 52: res = (-1)*fi 
    ## else: res = (fi)^2 - 2*se

    u_updated = u.split()
    print(u_updated)
    #compute fi
    fi = 0
    sign_fi = 1
    if(u_updated[1]=='-'):
        sign_fi = -1 
    for _ in u_updated[2]:
        if(_=='x'):
            break 
        fi=fi*10 + int(_)
    fi = fi*sign_fi
    print(fi)

    #compute se
    se = 0
    sign_se = 1
    if(u_updated[3]=='-'):
        sign_se = -1 
    for _ in u_updated[4]:
        if(_=='x'):
            break 
        se=se*10 + int(_)
    se = se*sign_se
    print(se)

    #compute th
    th = 0
    sign_th = 1
    if(u_updated[-4]=='-'):
        sign_th = -1 
    for _ in u_updated[-3]:
        if(_=='x'):
            break 
        th=th*10 + int(_)
    th = th*sign_th
    print(th)

    #compute fo
    fo = 0
    sign_fo = 1
    if(u_updated[-2]=='-'):
        sign_fo= -1 
    for _ in u_updated[-1]:
        if(_=='x'):
            break 
        fo=fo*10 + int(_)
    fo = fo*sign_fo
    print(fo)
    answ_send = 0
    if(leng==71):
        answ_send = (-1)*th//fo 
    elif(leng==52):
        answ_send = (-1)*fi 
    else:
        answ_send = fi*fi-2*se 
    u = r.recv()
    print(u)
    print(answ_send)
    r.sendline(str(answ_send).encode())
    u = r.recvline()
r.interactive()


