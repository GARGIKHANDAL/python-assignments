n=int(input("enter five digit number= "))
if n<0:
    print("invalid case")
a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
f=d//10
g=f%10
h=f//10
s=a*10000+c*1000+e*100+g*10+h
print("sum= ",s)
if s==n:
    print("number is palindrome")
else:
    print("number is not palindrome")