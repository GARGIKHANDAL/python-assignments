a = int(input("x1 : "))
b = int(input("y1 : "))
c = int(input("x2 : "))
d = int(input("y2 : "))
e = int(input("x3 : "))
f = int(input("y3 : "))
s1 = ((c-a)**2 + (d-b)**2)**0.5
s2 = ((e-c)**2 + (e-d)**2)**0.5
s3 = ((e-a)**2 + (e-b)**2)**0.5
s = (s1 + s2 + s3)/2
a = [(s*(s-s1)*(s-s2)*(s-s3))]**0.5
print("Area = ",a)