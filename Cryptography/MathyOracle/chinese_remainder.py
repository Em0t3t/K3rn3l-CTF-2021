# modular inverse
def inverse_mod(a,b):
    x = a
    y = b
    oldolds = 1
    olds = 0
    oldoldt = 0
    oldt = 1
    while y != 0:
        q = x // y
        r = x % y
        x = y
        y = r
        s = oldolds - q * olds
        t = oldoldt - q * oldt
        oldolds = olds
        oldoldt = oldt
        olds = s
        oldt = t
    return oldolds
# The chinese remainder theorem
def chi_rem_thm(mn,an):
    m = 1
    Mn = []
    yn = []
    for k in range(0, len(mn)):
         m  = m * mn[k]
    
    for  k in range (0, len(mn)):
        Mk = m / mn[k]
        Mn.append(Mk)
        yk = inverse_mod(Mn[k],mn[k]) % mn[k]
        yn.append(yk)
    x = 0
    for  k in range (0, len(yn)):
        x = x + an[k] * Mn[k] * yn[k]
    while x >= m:
        x = x - m
    return x
  # test
x = chi_rem_thm([1,2],[4,3])
print(x)