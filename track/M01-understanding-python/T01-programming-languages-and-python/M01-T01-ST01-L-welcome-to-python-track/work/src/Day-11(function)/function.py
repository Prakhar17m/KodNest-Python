def add():
    a =10
    b=20
    print(a+b)
add()

def square():
    n = 20
    print(n**2)
square()
#define larget of 3 numbers
def largest():
    x = 10
    y = 20
    z = 30
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)
largest()
# def to find number is even
def check_even():
    n =23
    if n%2==0:
        print("Number is even")
    else:
        print("Not even")
check_even()
# def greet
def greet():
    name = "Prakhar"
    print("Hello",name)
greet()




# function type based on the input and output  
# 1. with input and without output
def square(n):
    
    res = n**2
    print(res)
square(12)
def check_even(n):
    if n%2==0:
        print("n is even")
    else:
        print("n is odd")
check_even(237)
# 2. without input and with output
def square():
    n=12
    res = n**2
    return res
print(square())
def check_even():
    n = 236
    if n%2==0:
        return "n is even"
    else:
        return "n is odd"
print(check_even())
# 3. without input and without output
def square():
    n=12
    res = n**2
    print(res)
square()
def check_even():
    n = 76
    if n%2==0:
        print("n is even")
    else:
        print("n is odd")
check_even()
# 4. with input and with output
def square(n):
    return n**2
print(square(12))
def check_even(n):
    if n%2==0:
        return "n is even"
    else:
        return "n is odd"
check_even(237)
