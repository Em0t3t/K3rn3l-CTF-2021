u = b"x^10 - 47x^9 + 95x^8 - 66x^7 + 41x^6 + 85x^5 + 42x^4 + 17x^3 - 89x^2 - 32x^1 - 89x^0"
u=u.decode()

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
print(fi*sign_fi)

#compute se
se = 0
sign_se = 1
if(u_updated[3]=='-'):
    sign_se = -1 
for _ in u_updated[4]:
    if(_=='x'):
        break 
    se=se*10 + int(_)
print(se*sign_se)

#compute th
th = 0
sign_th = 1
if(u_updated[-4]=='-'):
    sign_th = -1 
for _ in u_updated[-3]:
    if(_=='x'):
        break 
    th=th*10 + int(_)
print(th*sign_th)

#compute fo
fo = 0
sign_fo = 1
if(u_updated[-2]=='-'):
    sign_fo= -1 
for _ in u_updated[-1]:
    if(_=='x'):
        break 
    fo=fo*10 + int(_)
print(fo*sign_fo)

