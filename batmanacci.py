fib = [ 0, 1, 1]
def fibo(n):
    for i in range (3, n+1):
        tmp = fib[-1] + fib[-2]
        fib.append(tmp)
    
def solve(n, k):
    while (n > 2):
        tmp = fib[n-2]
        if (k > tmp):
            n -= 1
            k -= tmp
        else:
            n -= 2
    
    if (n==1): print('N')
    if (n==2): print('A')

value = input().split()
n=value[0]
k=value[1]
n=int(n)
k=int(k)
fibo(n)
solve(n, k)
