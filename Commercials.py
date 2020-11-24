
def solve(a):
    global P, listeners, costs, res
    subMax = [0]*N
    subMax[0] = costs[0]##correct use of memoization
    for i in range(1,N):
        subMax[i] = max((costs[i]), (costs[i] + subMax[i-1]))
        if (subMax[i]>res):
            res = subMax[i]
    return res

    


value = input().split()
N = int(value[0])
P = int(value[1])

listeners = [N]
listeners[:N]=input().split()
costs = [-1]*N
res = 0
for i in range(N):
    listeners[i]=int(listeners[i])
    costs[i] = int(listeners[i])-P
res = costs[0]
solve(costs)
##print(costs)
print(res)
