"""Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique."""

d={}
name=input("Enter Friends name :")
lang=input("Enter languange name :")

d.update({name:lang})
name=input("Enter Friends name :")
lang=input("Enter languange name :")

d.update({name:lang})

name=input("Enter Friends name :")
lang=input("Enter languange name :")

d.update({name:lang})

name=input("Enter Friends name :")
lang=input("Enter languange name :")

d.update({name:lang})
print(d)