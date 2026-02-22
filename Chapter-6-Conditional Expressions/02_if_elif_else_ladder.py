'''if elif else ladder'''

a=int(input("Enter your age:"))

if(a>=18):
    print("'you are able to give vote!'")

    # SPACE IS CALLED INDENT
elif(a<0):
    print("'Entering an invalid age!'")
elif a==0:
    print("U are Entering zero invalid age!")
else:
    print("'Below age not able to give vote!'")

print("End of Condition::") # dont part of any condition
