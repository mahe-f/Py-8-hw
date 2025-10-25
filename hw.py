#reversed number

n=int(input("Enter a number: "))
reverse=0
while n!=0:
    c=n%10
    reverse=reverse*10+c
    n=n//10
print("reversed order : ",reverse)
