# Terminal - Game with Math Functionality and logic

# Available Command
avail_cmd = print("List of Commands: " \
"1. Addition +/add" \
"2. Subtraction -/sub" \
"3. Multiplication */mult" \
"4. Division "/"/div")

# User Input for the game
user_input = input("Enter a command: ")
print(">")


integer_1 = int(input("Enter your First Number"))
integer_2 = int(input("Enter your Second Number:"))

if integer_2 != 0:
    integer_3 = int(input("Enter your other Number: "))
else:
    print("Yes/No")
    confirmation = input("Enter:")
    if confirmation.lower == "yes" or confirmation.lower == "y":
        