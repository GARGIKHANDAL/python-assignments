a = input("Enter shape : ")
if a=="square":
    b = float(input("Enter length of side ;"))
    print("area = ", b*b)
elif a=="rectangle":
    c = float(input("Enter length : "))
    d = float(input("Enter width :"))
    print("area = ", c*d)
elif a=="circle":
    e = float(input("Enter radius of circle : "))
    f = 3.14*e**2
    print("area = ", f)
elif a=="triangle":
    g = float(input("Enter height : "))
    h = float(input("Enter base length : "))
    i = (g*h)/2
    print("area = ", i)