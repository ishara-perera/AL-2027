number = int(input("enter number of unit: "))

num1 = number * 5
num2 = number * 10

if number <= 64:
    print(f"{number}*{5}={num1}")
else:
    print(f"{number}*{10}={num2}")
    
