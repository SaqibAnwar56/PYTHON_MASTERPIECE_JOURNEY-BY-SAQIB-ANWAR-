'''

7. Write a program to find out whether a given post is talking about “Saqib” or not. '''

post=input("Enter the post:")


if("Saqib".lower() in post.lower()):
    print("This post is talking about Saqib :")
else:
    print("This post is not talking about Saqib :")
