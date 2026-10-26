
# 1. how can you make a local variable into global
c =30
def add():
    global a
    a =10
    b=20
    print(a+b)
    print(c)
add()
print(a)
print(c)


#2. what happens when we use local and global variable with same name
x =100
def fun():
    x =50 
    print(x)   # inside function it will priorties the loca variable
fun()
print(x) # outside the function it will priorties the global variable


# 3. what happens when we try to change the globale variable using the local variable
x= 10
def fun():
    print(x)
    x =20
fun()      # this will show us the unbound error
print(x)





### function overloading--- in the function have the same name but with the different parameters
# in python it is not supported but we can achieve this using the default paramerters and the *args
# 1. using the default variables
def fun(a,b=0,c=200):
    print(a+b+c)
fun(10)
fun(10,20)
fun(10,20,30) # 60

# 2. using the *args---it use the variable length of arguments
def addi(*args):
    total =0
    for num in args:
        total += num
    print(total)
addi()
addi(10,20,40,2000000)
addi(40,45)




### what is keyword arguments---kwargs
# --0---n arguments can be passed -->dict
# ** kwargs are used to pass the variable length of key arguments to the function
def fun(**kwargs):
    print(kwargs)
fun(a=10,b=20,c=30)        

def solve(**kwargs):
    print(kwargs.get('age'))
    print(kwargs.get('name'))

solve(name="Prakhar",age="21")





