'''1. Write a program to find the greatest of four numbers entered by the user.'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("a is greatest among all and a =", a)
elif b >= a and b >= c and b >= d:
    print("b is greatest among all and b =", b)
elif c >= a and c >= b and c >= d:
    print("c is greatest among all and c =", c)
else:
    print("d is greatest among all and d =", d)
    