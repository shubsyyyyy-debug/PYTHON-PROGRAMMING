# 1. Check if a number is greater than 10 and less than 50
x=int(input("enter no."))
if 10<x<50:
    print("yes")
else:
    print("no")



# 2. Print True if age is greater than or equal to 18
age = 18
x=int(input("enter age"))
if x>=18:
    print("true")
else:
    print("false")


# 3. Print result of x and y
x = True
y = False
print(x and y)


# 4. Check if either 5 > 10 or 2 < 8
print(5 > 10 or 2 < 8)


# 5. Check if a number is not divisible by 3
x=int(input("enter no."))
if x%3==0:
    print("div by 3")
else:
    print("not div by 3")


# 6. Check password and length
password = "admin123"

if password == "admin123" and len(password) >= 6:
    print("Access Granted")
else:
    print("Access Denied")


# 7. Check if both numbers are positive
x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
if x>=0 and y >=0:
    print("yes")
else:
    print("no")


# 8. Use not with 5 != 10
print(not (5 != 10))