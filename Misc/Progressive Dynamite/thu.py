Nmax = 5
u = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
for i in range(Nmax-2,-1,-1):
    u[Nmax-1][i] += u[Nmax-1][i+1]
    u[i][Nmax-1] += u[i+1][Nmax-1]
for i in range(Nmax-2,-1,-1):
    for j in range(Nmax-2,-1,-1):
        u[i][j]+=min(u[i+1][j],u[i][j+1])
print(u[0][0])