#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime

# functions:

# register a user
def register_user():
    print("You have chosen to register a new user:")
    # get user inputs
    username1 = input("Enter the username for the new user:\n")
    password1 = input("Enter the password for the new user:\n")
    password_check = input("Please re-enter the password to confirm registration:\n")
    # if password confirmed successfully
    if password1 == password_check:
        # open user.txt file to append new information to it. 
        with open('user.txt', 'a') as file:
            # start with a newline or the information will be written right after the previous password. 
            file.write(f"\n{username1}, {password1}")
        # success message
        print(f"User {username1} registered successfully!")
    else:
        # error message.
        print("User registration unsuccessful.")

# function to display tasks properly
def display_task(task):
    # display information as required:
    print(f"\nTask: \t\t\t {task[1]}")
    print(f"Assigned to: \t\t {task[0]}")
    print(f"Date assigned: \t\t {task[3]}")
    print(f"Due date: \t\t {task[4]}")
    print(f"Task complete? \t\t {task[5].rstrip()}") # rstrip used to remove newline.
    print("Task description:")
    print(f"   {task[2]}")

# validate the date
def vali_date(date_string):
    date_wrong = True
    date_format = "%d %b %Y"
    while date_wrong:
        try:
            # check if string entered matches date format. If it does, exit loop.
            date_check = datetime.strptime(date_string, date_format)
            date_wrong =  False
        except:
            # request new string to match date format. 
            date_string = input("Incorrect format. Please enter date in 01 Jan 2024 format. \n")
            date_wrong = True 
    # return validated date
    return date_string

# function to add a task
def add_task():
    print("You have chosen to add a new task:")
    # get user inputs
    user = input("Enter the username of the person to whom the task is assigned:\n")
    title = input("Enter the title of the task:\n")
    description = input("Enter a short description of the task:\n")
    due_date = vali_date(input("Enter the due date for the task in DD Month YYYY format (e.g. 01 Jan 2024):\n"))
    # get today's date, and format it same as other dates in the tasks file.
    date_added = datetime.now().strftime("%d %b %Y")
    # open file in append mode to add data to the file
    with open('tasks.txt', 'a') as tasks:
        tasks.write(f"\n{user}, {title}, {description}, {date_added}, {due_date}, No")
    # success message
    print("New task added successfully!")

# function to make sure all linebreaks are the same length
def linebreak():
    print("_____________________________________________________________")

# function to view tasks
def view_all_tasks():
    print("Here are all assigned tasks:\n")
    # open file in read-only format
    with open('tasks.txt', 'r') as task_list:
        # loop instructions for every task
        for task in task_list:
            # display a line
            linebreak()
            # split the string into a usable list
            task = task.split(", ")
            # display information as required:
            display_task(task)
        # display line at the end of all tasks.
        linebreak()

# function to view specific tasks
def view_my_tasks():
    print("Here are the details of the tasks assigned to you:")
    # open file in read only format 
    with open('tasks.txt', 'r') as tasks:
        # loop through tasks
        for task in tasks:
            # turn task into usable list
            task = task.split(", ")
            # if person the task is assigned to is same as the username used to login, print task details in requirred format
            if task[0] == username:
                linebreak()
                display_task(task)
        linebreak()

# function to display user count and task count.
def display_statistics():
    # open user file. count users.
    with open('user.txt', 'r') as users:
        user_no = 0
        for line in users:
            user_no += 1
    # open task file. Count tasks.
    with open('tasks.txt', 'r') as tasks:
        task_no = 0
        for task in tasks:
            task_no += 1
    # print users and tasks. 
    print(f"Total number of users: \t {user_no}.")
    print(f"Total number of tasks: \t {task_no}.")

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

# boolean controls for while loops
login_needed = True
logged_in = False

# logging in
while login_needed:
    # user input 
    username = input("Enter your username:\n")
    password = input("Enter your password:\n")
    # open text file with usernames and passwords in read-only format
    with open('user.txt', 'r') as users:
        for line in users:
            # format line into a usable list. rstrip() to remove the '\n' character from the password
            line = line.rstrip().split(", ")
            # if username matches first item in the list
            if line[0] == username:
                # if password matches second item in the same list
                if line[1] == password:
                    # login successful
                    print(f"You have successfullly logged in, {username}!")
                    # toggle boolean values
                    logged_in = True
                    login_needed = False
        # login-unsuccessful message. 
        if login_needed:
            print("Your username or password is incorrect. Please try again.")


while logged_in:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    
    if username == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
d - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''')

    # register a user. Only admin can register a user. Anyone else will not see the option in their menu, and will see an error message on pressing 'r.'
    if menu == 'r':        
        if username == "admin":
            register_user()            
        # error message if you pressed r but were not logged in as admin.
        else:
            print("You have made entered an invalid input. Please try again.")

    # add a task. 
    elif menu == 'a':
        add_task()    

    # view all tasks
    elif menu == 'va':            
        view_all_tasks()
        
    # view my tasks
    elif menu == 'vm':
       view_my_tasks()

    #### There's probably a way to do va and vm with the same function but I'm not sure what that is.

    # display statistics. only visible to admin.
    elif menu == 'd':
        # if username is admin
        if username == "admin":
            display_statistics()
       # error message if you chose d but did not login as admin.
        else:
            print("You have made entered an invalid input. Please try again")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")