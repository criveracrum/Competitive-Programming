

def solve(x,y, word, visited):
    global length,longest
   
    if (isWord(word)):
        found.append(word)
        print(word)
        if (len(word) > length):
            length=len(word)
            longest=word
        return True
    if (visited[x][y]==1):
        return False
    for i in range(max(0,x-1), min(4,x+2)):
        for j in range(max(0, y-1), min(4, y+2)):
            visited[i][j] = 1
            solve(x+i,y+j,(word+focus[i][j]), visited
            visited[i][j] = 0
              
##    elif(len(word)==8 or x==4 or y==4 or x<0 or x<0):
##        return False
##    if (x!=3): 
##        solve(x+1,y,word+focus[x][y])
##    if (y!=3):
##        solve(x,y+1,word+focus[x][y])
##    if(x!=3 and y!=3):    
##        solve(x+1,y+1,word+focus[x][y])
##    if(x!=3 and y>0):
##        solve(x+1,y-1,word+focus[x][y])
##    if(x!=0):
##        solve(x-1,y,word+focus[x][y])
##    if(y!=0):
##        solve(x,y-1,word+focus[x][y])
##    if (x!=0 and y!=0):
##        solve(x-1,y-1,word+focus[x][y])
##    if (x!=0 and y!=3):
##        solve(x-1,y+1,word+focus[x][y])
    
    return False


def isWord(string):
    if string in words:
        return True
    return False


value = int(input())

words = []

for i in range(value):
    tmp = input()
    words.append(tmp)
input()        
boardVal=int(input())
        
games =  []

for j in range(boardVal):
    tmp = []
    for k in range(4):
        tmp2 = input()
        tmp.append(list(tmp2))
    games.append(tmp)
    if (j!=boardVal-1):
        input()
    
points = [0,0,0,1,1,2,3,5,11]
longest = ''
length = 0
for l in range(boardVal):
    found = []
    visited = [[0 for x in range(4)] for y in range(4)]
    score = 0
    focus = games[l]
    longest = ''
    length = 0
    for x in range(4):
        for y in range(4):
            solve(x, y,"", visited)
    
    for word in found:
        score += points[len(word)]
        if (len(word) ==length and word < longest):
            longest=word
    
        
            
       
    
    print('{} {} {}'.format(score, str(longest), len(found)))
    
    
    


