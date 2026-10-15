a, b, c = 1, 2, 3
print(a+b+c)
# variables declaration rules
"""
1. it should contain [a-z][A-Z][0-9]
2. it should not be the keyword
3. it should not start with the numbers
4. it can contain the (_) symbol

"""

# comments---single line
# multi line--for documentation---""" comments   """


# data type casting
x  = 10
name = "aman"
print(name,x)
print(name+str(x))


# data types example
# primitive -- int,float, complex, none, str
# non primitive -- list, dict, set, tuple
print(type(x))

# int
a = 10
print(type(a),a)
#float
x = 10.11
print(type(x),x)
# string
b = "yoooooo"
print(type(b),b)
# boolean
c = True
print(type(c),c)
# none
d = None
print(type(d),d)
# complex
e  = i = 1+2j
print(type(e),e)

# list
l =  [10,20,30]
print(type(l),l)

# tuple
t = (10,20,30)
print(type(t),t)

# set
s = {10,20,50}
print(type(s),s)

# dictionary
di = {a:10, b:20}
print(type(di), di)




# user input
name = input("enter: ")
age = int(input("enter:"))
print(f"My name is {name} and my age is {age}")

# add two numbers
n1 = float(input())
n2 = int(input())
print(n1+n2) 
print(type(n1+n2)) 
 # result will be float

