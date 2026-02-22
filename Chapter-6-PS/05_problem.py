"""
5. Write a program which finds out whether a given name is present in a list or not."""

l=["Saqib","Aaqib","Atif","Babar"]
name=input("Enter your name : ")
if(name in l):
    print("your name is in the list ! :",name)
else:
    print("your name is not in the list ! oops")