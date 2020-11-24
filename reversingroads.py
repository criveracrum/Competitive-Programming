def dfs(origin):
    global visited, edges
    visited.append(origin)
    if (origin in edges):
        for edge in edges[origin]:
            if edge not in visited:
                dfs(edge)
    stack.append(origin)

def revDFS(origin):
    global visited, revEdges
    visited.append(origin)
    if (origin in revEdges):
        for edge in revEdges[origin]:
            if edge not in visited:
                revDFS(edge)
count = 0   
while True: 
    try:
        count +=1
        temp = input().split()
        m = int(temp[0])
        n = int(temp[1])

        edges = {}
        revEdges = {}
        visited = []
        stack = []
        for i in range(n):
            road = input().split()
            if (int(road[0]) not in edges):
                edges[int(road[0])] = []
            edges[int(road[0])] .append(int(road[1]))
            if (int(road[1]) not in revEdges):
                revEdges[int(road[1])] = []
            revEdges[int(road[1])] .append( int(road[0]))
        for i in range(n):
            if i not in visited and i in edges:
                dfs(i)
        copy = stack.copy()
        if (len(copy)>0):
            end = copy[0]
          
        visited.clear()
        counter = 0
        
        while(stack):
            tmp = stack.pop()
            if tmp not in visited and tmp in revEdges:
                counter += 1
                revDFS(tmp)
      
        if (counter==1):
            flag = True
            for each in copy:
                if each not in edges:
                    res = "invalid"
                    print("Case {}: {}".format(count, res))
                    flag = False
                    break
            if (flag):    
                res = "valid"
                print("Case {}: {}".format(count, res))
            continue
        if (counter > 1):
            for i in edges:
                if (end in edges[i]):
                    res = "{} {}".format(i, end)
                    break
            print("Case {}: {}".format(count, res))
            continue
        
        
       
     
    except EOFError:
        break
    ##recommended from Discord


