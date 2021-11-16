from os import system


def find_inverse(m, b):
    A = {1: 1, 2: 0, 3: m}
    B = {1: 0, 2: 1, 3: b}
    T = {1: 0, 2: 0, 3: 0}
    Q = 0
    while True:
        if B[3] == 0:
            return A[3]  # no inverses
        if B[3] == 1:
            return B[2]  # B2 = b^-1 mod m
        Q = A[3] // B[3]
        T[1] = (A[1] - (Q * B[1]))
        T[2] = (A[2] - (Q * B[2]))
        T[3] = (A[3] - (Q * B[3]))
        A = B.copy()
        B = T.copy()


eqs = []

for i in range(int(input("Number Of Equivalent Equations : "))):
    try:
        system("cls")
    except:
        system("clear")
    print(f"Input Equations In This Form -> a{i+1}(mod n{i+1})")
    eqs.append(
        {
            "a": int(input(f"a{i+1} : ")),
            "n": int(input(f"n{i+1} : "))
        })


# Multiply all n's
N = 1
for i in eqs:
    N *= i['n']


# Sum all
sum = 0
for i in eqs:
    sum += (i['a'] * (N//i['n']) * find_inverse(m=i['n'], b=N/i['n']))


# To be sure N is positive
while sum < 0:
    sum += N

try:
    system("cls")
except:
    system("clear")
print("X :", sum)
for eq in eqs:
    print(f"{sum} ≡ {eq['a']}(mod {eq['n']})", end=" | ")
    print(sum % i['n'] == i['a'])