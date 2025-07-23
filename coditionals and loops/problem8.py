#problem to find the factorial of given number
n=int(input("Enter the number: "))
i=1
fact=1
while(i<=n):
    fact*=i
    i+=1
print(fact)