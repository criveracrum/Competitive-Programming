from collections import Counter

def cost(a, b):
  com = Counter(a) & Counter(b)
  return sum(com.values())

def totalCost(row):
    res = 0
    for i in range(len(row)-1):
        res+=sum((Counter(row[i]) & Counter(row[i+1])).values())
    return res

def solve(used, k, r):
    if (k==r):
        return totalCost(used)

    res = 1000000
    
    for i in range(k, r+1):
       used[k], used[i] = used[i], used[k]
       res = min (res, solve(used, k+1, r))
       used[k], used[i] = used[i], used[k]
    return res

r = int(input())
routines = []

while (len(routines) < r):
    routines.append(input())

print(solve(routines, 0, r-1))

