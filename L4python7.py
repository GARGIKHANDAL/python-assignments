x = float(input("Enter your budget : "))
y = input("Enter season of travelling : ")
if x <= 100 and y == "Summer":
    print("Place = Bulgaria") 
    print("Money spend = ", (40*x)/100)
elif x<= 100 and y == "Winter":
    print("Place = Bulgaria") 
    print("Money spend = ", (70*x)/100)
elif 100 < x <= 1000 and y== "Summer":
    print("Place = Balkans")
    print("Money spend = ", (40*x)/100)
elif 100< x <= 1000 and y=="Winter":
    print("Place = Balkans")
    print("Money spend = ", (80*x)/100)
elif x>=1000 and y =="Summer" or y=="Winter":
    print("Place = Europe")
    print("Money spend = ", (90*x)/100)

    