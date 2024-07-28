# Console program that asks the user to enter full name until a valid-ish input.

# user input
name = input("Enter your full name here:\n")

# declaring booleans because I need them later.
name_is_wrong = True
length_okay = False
spaces_okay = False

# while loop that continues until you enter the name properly. 
while name_is_wrong:

    # if nothing has been entered. Input command used instead of print to allow user to enter their name again.
    if len(name) == 0:
        name = input("You haven't entered anything. Please enter your full name.\n")
        length_okay = False

    # if less than 4 characters have been entered. Message edited from task description to allow the user to re-enter the input.
    elif len(name) < 4: 
        name = input("You have entered less than 4 characters. Please enter your name and surname.\n")
        length_okay = False

    # if too many letters have been entered
    elif len(name) > 25:
        name = input("You have entered more than 25 characters. Please enter only your full name.\n")
        length_okay = False
    
    # if condition has been met.
    else:
        length_okay = True

    # check for spaces in the name string. 
    x = 0
    for character in name:
        if character == " ":
            x = x + 1

    # if entered/re-entered string has no spaces
    if x < 1:
        name = input("You have entered words without any spaces. Please enter first name and last name.\n")
        spaces_okay = False

    # if the string has too many spaces
    elif x > 2: 
        name = input("You have entered too many spaces. Please enter first name and last name.\n")
        spaces_okay = False

    # condition for spaces has been met.
    else:
        spaces_okay = True

    # if both conditions are met, exit while loop.
    if length_okay:
        if spaces_okay:
            name_is_wrong = False


# Final output.
print("Thank you for entering your name.")
