x = float(input("Enter distance to travell : "))
y = input("Enter time of travelling : ")
if x < 20 and y=="Day":
    print("Total expense : ", 33.58 + (x * 37.89))
elif x < 20 and y=="Night":
    print("Total expense : ", 33.58 + (x * 43.17))
elif 20 <= x < 100 and y== "Day" or y=="Night":
    print("Total expense : ", x * 4.32)
elif x>= 100 and y=="Day" or y=="Night":
    print("Total expense : ", x * 2.88 )