#set a variable to store the lowest number
lowest_num = None
#using while loop, input numbers continuously
while True:
    user_input = input("Enter a number: ")
#create a function that identifies which is the lowest number
    try:
        num = float(user_input)
        if lowest_num is None or num < lowest_num:
            lowest_num = num
    except ValueError:
#break if it is an invalid number
        break

#print the lowest number
if lowest_num is not None:
    print(f"The lowest number is {lowest_num}")
else:
    print("Invalid input")