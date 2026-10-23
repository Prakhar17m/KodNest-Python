def printn(n):
    if n==0:
        return             # 5 4 3 2 1
    print(n)
    printn(n-1)
print(printn(5))




def fact(n):
    if n==0 or n==1:
        return 1
    return n* fact(n-1)
factorials =[]
for i in range(6):
    factorials.append(fact(i))
print(factorials)



def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
fibonacci_series =[]
for i in range(6):
    fibonacci_series.append(fibo(i))
print(fibonacci_series)