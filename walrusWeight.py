
def solve():
    T=[[0 for x in range(1000+1)] for y in range(values+1)]

  
    for j in range(values+1):
        for k in range (1000+1):
            ##print(j , " ", k)
            if (j==0 or k==0):
                T[j][k] = 0
            elif  weights[j-1]<=k:
                T[j][k] = max(weights[j-1]+T[j-1][k-weights[j-1]], T[j-1][k])
            else:
                T[j][k] = T[j-1][k]

    return print(T[values][1000])

  

values = int(input())

weights = []
for i in range(values):
    weights.append(  int(input()))
solve()


