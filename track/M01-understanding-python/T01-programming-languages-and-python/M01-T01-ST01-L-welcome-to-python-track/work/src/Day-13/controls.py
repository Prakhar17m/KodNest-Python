# topics - if-elif-else   ,  match statemnts, loops,   break,continue,pass 

# p1 - check n is positive
p1 = 10
if p1>0:
    print("positive")


# p2 - check if a person is eligibal to donate blood(age>=18)
age = 20
if age>=18:
    print("eligible to donate blood")
else:
    print("not eligible")

    
# p3 - check if the temperature is above 30c and print "hotday"
temp =36
if temp>30:
    print("hot day")
else:
    print("normal day")


# p4 - check whether a student has attended atleast 75% of the classes
attendence =87
if attendence >=75:
    print("eligible to give the exam")
else:
    print("try next year")

    
# p5 - check if teh number is even or odd
num = 24
if num % 2==0:
    print("even")
else:
    print("odd")

    
# p6 - check whether the person is eligible to apply a dl
age = 21
if age>=18:
    if age<=75:
        print("eligible for the dl")
    else:
        print("over age")
else:
    print("under age")
    
    
# p7 - check whether the given year is a leap year or not
def leap_year(year):
    if year %400==0:
        if year%100==0:
            return True
    return False
print(leap_year(2004))


# p8 - compare two numbers and print the greatr number
n1 = 10
n2 =20
if n1>n2:
    print(n1)
else:
    print(n2)
    

# p9 - assign grades based on marks
def grades(marks):
    if marks >=90 and marks<=100:
        print("A")
    elif marks >= 80 and marks<=89:
        print("B")
    elif marks>=70 and marks<=79:
        print("C")
    elif marks>=60 and marks<=69:
        print("D")
    else:
        print("Failed successfully")
print(grades(66))


# p10- categories electricity usages:
def electricity_usage(units):
    if units >500:
        print("High")
    elif units<=500 and units>=301:
        print("medium")
    elif units<=300 and units>=101:
        print("low")
    else:
        print("very low")
print(electricity_usage(399))


# p11 - scholarship eligibility:
def check(marks,income):
    if marks>=85 and income<300000:
        print("eligibe for the scholarship")
    else:
        print("sorry")
print(check(90,200000))


# p12 - user login:
def valid_user(username,password):
    if username=="admin" and password=="yogi":
        print("login successfull")
    else:
        print("failed successfully")
print(valid_user("admin","yogi"))


# p13 - display weekday using the numbers(1-7)
def display_weekday(n):
    match n:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("invalid number")
print(display_weekday(4))


# p14 - display season based on month .
def display_season(month):
    match month:
        case 12 |  1 | 2:
            print("Winter")
        case 3 | 4 | 5:
            print("Spring")
        case 6 |7 | 8 | 9 :
            print("Rainy season") 
        case 10 | 11:
            print("Autumn")
        case _:
            print("invalid month")
print(display_season(3))


# p15 - print n from 1 to 20
for i in range(1, 21):
    print(i)


# p16 - print multiplication table of a given number
def multiplication_table(n):
    for i in range(1,11):
        print(f"{i} x {n} = {i*n}")
multiplication_table(9)  


# p17 - print number from 10 to 1
n=10
while n>=1:
    print(n)
    n -=1


# p18 - find factorial of a number
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

# p19 - print number from 1 to 20 but stop at 15
for i in range(1, 21):
    if i==15:
        break
    print(i)


# p20 - search for a number in a list using the break
arr = [10,20,30,40,50]
for num in arr:
    if num==30:
        print("found")
        break


# p21 - print number form 1 to 20 , skip multiple of 3
for i in range(1, 21):
    if i %3==0:
        continue
    print(i)

# p22 - print odd numbers from 1 to 50
for i in range(1, 51):
    if i %2!=0:
        print(i)

# p23 - find the cube of a number
def find_cube(n):
    return pow(n,3)
print(find_cube(99))

# p24 - find the maximum of the two numbers
def find_max(a,b):
    if a>b:
        return a
    else:
        return b
print(find_max(10,1))

# p25 - create an empty function named display()
def display():
    pass
display()

# p26 - create an empty class named student
class student:
    pass
obj = student()
print(obj)