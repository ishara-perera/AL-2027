user_input = input("Please a positive integer: ")

# not work for symbols
# not work for float

if user_input == '':
    print("You haven't enetered anything!")
    
elif user_input.isalpha():
    print("Please enter only numbers, not letters!")
else:
    num = int(user_input) # input() - let the user to input data from keybaord (type: string - a sequence of characters) 'Rayani@123'
    if num > 0:
        for i in range(1,13):
            print(f"{num} × {i} = {num*i}") # repetitve task
    else:
        print("Enter a positive number!")