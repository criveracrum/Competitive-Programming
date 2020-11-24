def solve(i, row, remaining):
    global  sets, n
    
    if i==n:
            sets.append(row)
            
            return True
    
    for x in sorted(remaining):
        if (i==0 or feasible(x, row)):
            print("feasible")
            row[i] = x
            remaining.remove(x)
            if (solve(i+1, row, remaining)==True):
                return True
            remaining.add(x)
            
    return False   
       
def feasible(num, row):
    if num in conflicts:
        for i in row:
            if num in conflicts and (conflicts[num]==i):
                    print(conflicts[num])
                    return False        
    return True





            
value = input().split()
n = value[0]
k = value[1]
n=int(n)
k=int(k)

conflicts = {}
if k>0:
    while (len(conflicts) <= k):
        n1, n2=tuple(input().split())
        conflicts[n1]=set()
        conflicts[n2]=set()
        conflicts[n1].add(n2)
        conflicts[n2].add(n1)
values = []
for i in range(0,n+1):
    values.append(i)

row = [[] for j in range(n)] 
sets = []
solve(0, row, values)

print(len(sets))
print(sets)
