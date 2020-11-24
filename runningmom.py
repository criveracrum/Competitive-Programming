def dfs(city, clock):
    global visited, times, graph
    clock += 1
    visited.append(city)
    times[city]= {"pre" : clock, "post" : None}
    for edge in graph.get(city):
        if edge not in visited:
           clock = dfs(edge, clock)
    clock += 1
    times[city]["post"]= clock
    return clock


N = int(input())

graph = {}

for i in range(N):
    temp = input().split()
    origin = temp[0]
    dest = temp[1]
    if origin not in graph:
        graph[origin] = []
    if dest not in graph:
        graph[dest] = []
   
        
    graph.get(origin).append(dest)

tests = []
while True: 
    try:
        city = input()
        tests.append(city)
    except EOFError:
        break
    ##recommended from Discord

for i in tests:
    clock = 0
    visited = []
    times = {}
    dfs(i, clock)
    pre = times.get(i).get("pre")
    post= times.get(i).get("post")
    print(times)
    flag = False
    for time in times:
        if times[time]["post"] < post and (i in graph[time]):
            flag = True
    if (flag):
        print(i + " safe")
    else:
        print(i + " trapped")

   
    



    
