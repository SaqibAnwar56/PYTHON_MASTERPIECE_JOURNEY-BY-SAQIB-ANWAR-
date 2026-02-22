

a=int(input("Enter your age:"))

'''If statement 1'''
if a%2==0:
    print("A is even no")
    '''End of if statement no 1'''

    '''If statement 2'''
if(a>=18):
    print("'you are able to give vote!'")

    # SPACE IS CALLED INDENT
elif(a<0):
    print("'Entering an invalid age!'")
elif a==0:
    print("U are Entering zero invalid age!")
else:
    print("'Below age not able to give vote!'")

    '''End of if statement no 2'''

print("End of Condition::") # dont part of any condition


"""IMPORTANT NOTES:
1. There can be any number of elif statements.
2. Last else is executed only if all the conditions inside elifs fail"""
 