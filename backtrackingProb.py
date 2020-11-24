def solve(row, remaining, i):
    global n, forbidden

    if i==n:
        print(" ".join(row))
        return True
    
    for student in sorted(remaining):
        if i==0 or student not in forbidden[row[i-1]]:
            row[i] = student
            remaining.remove(student)
            if solve(row, remaining, i+1) == True:
                 return True
            remaining.add(student)
    return False

 




while True:
    try:
        n = int(input())
    except:
        break

    students, forbidden = set(), {}

    for i in range(n):
        name = input()
        students.add(name)
        forbidden[name]= set()
    ##students.sort()

    m = int(input())
    for i in range(m):
        n1, n2 = tuple(input().split())
        forbidden[n1].add(n2)
        forbidden[n2].add(n1)

    row = ["" for j in range(n)]
    if not solve(row, students, 0):
        print("You all need therapy.")
