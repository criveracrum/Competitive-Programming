def dfs(city, dest):
    global visited, graph, flag
    visited.append(city)
    if (city == dest):
        print( visited )
        flag = True
        return
    for edge in graph[city]:
        if edge not in visited:
            dfs(edge, dest)
       
    



N = int(input())

graph = {}

for i in range(N):
    temp = input().split()
    origin = temp[0]
    graph[origin] = []
    for j in temp[1:]:
        graph[origin].append(j)
        if (j not in graph):
            graph[j] = []
        if (origin not in graph[j]):
            graph[j].append(origin)

temp2 = input().split()
origin = temp2[0]

dest = temp2[1]
visited = []
flag = False
dfs(origin, dest)
dfs(dest, origin)
if (not flag):
    print ("no route found")
