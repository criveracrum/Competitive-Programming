def dfs(origin):
    global visited, graph
    visited.append(origin)
    for edge in graph[origin]:
        if edge not in visited:
            dfs(edge)
    dependency.append(origin)      
       
    



N = int(input())

graph = {}

for i in range(N):
    temp = input().split()
    rule = temp[0]
    rule = rule.strip(": ")
    if (rule not in graph):
        graph[rule] = []
    for j in temp[1:]:
        if j in graph:
            graph[j].append(rule)
        else:
            graph[j] = [rule]
        
if (N>0):
    changed = input()
    
    visited = []
    dependency = []
    if (changed in graph): 
        dfs(changed)
        if (dependency):
            dependency.reverse()
            for i in dependency:
                print(i)

    
