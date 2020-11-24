m = int(input())
ops = {'+': '+', '//': '/', '*': '*', '-':'-'}
##opStr = {'+', '/', '*', '-'}
valueDic = {}
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            expr = f'4 {op1} 4 {op2} 4 {op3} 4'
            valueDic[eval(expr)] = "4 {0} 4 {1} 4 {2} 4 = {3}".format(
                ops[op1], ops[op2], ops[op3],eval(expr))
            

for val in range(m):
    check=int(input())
    if ((check in valueDic) ):
        print(valueDic[check])
    else:
        print("no solution")
                
