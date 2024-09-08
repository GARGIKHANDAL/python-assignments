n=int(input("enter three digit number= "))
if n<0:
    print("invalid case")
a=n%10
b=n//10
c=b%10
d=b//10
s=a**3 +c**3 +d**3
if s==n:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")