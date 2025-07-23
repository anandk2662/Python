# to find the greatest of four numbers
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))
d=int(input("enter number 4: "))
if(a>b and a>c and a>d):
    print("Greatest number is a :",a )
elif(b>c and b>d):
    print("Greatest number is b :",b)
elif(c>d):
    print("Greatest number is c:",c)
else:
    print("Greatest number is d:",d)
    
