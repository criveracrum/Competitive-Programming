
test = int(input())
for i in range(test):
    customers = int(input())
    length = []

    for i in range(customers):
        temp = input().split()
        total=0
        for j in temp[1:]:
            total += int(j)

        length.append(total)

    length.sort()

    
    total = length[0]
    for k in range(1,len(length)):
        length[k] += length[k-1]
        total += length[k]
    
    print(total/customers)
