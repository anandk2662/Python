#program to input marks from user and tell whether he passed or failed
marks1=int(input("marks of subject 1:"))
marks2=int(input("marks of subject 2:"))
marks3=int(input("marks of subject 3:"))

if(marks1>=33 and marks2>=33 and marks3>=33 and (marks1+marks2+marks3)/3>=40 ):
    print("student has passed")
else:
    print("student has failed") 