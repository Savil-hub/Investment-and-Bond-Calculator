#=====importing libraries===========
# Import the required functions from methods.py
from methods import reg_user, view_all_tasks, view_my_tasks, add_task, calculate_task_statistics, display_statistics, generate_task_overview

user_names = []
pass_words = []

# Read user data from "user.txt" and populate user_names and pass_words lists
with open("user.txt", "r") as user_file:
    for line in user_file:
        temp = line.strip().split(', ')
        user_names.append(temp[0])
        pass_words.append(temp[1])

login = False

while not login:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin":
        # Check if the username is "admin"
        print("Admin login successful.")
        while True:
            # Admin menu options
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()

            if menu == 'r':
                reg_user(user_names)  # Fixed the function call, remove pass_words argument
            elif menu == 'a':
                add_task(username)
            elif menu == 'va':
                view_all_tasks()
            elif menu == 'vm':
                view_my_tasks(username)
            elif menu == 'gr':
                generate_task_overview()
            elif menu == 'ds':
                task_statistics = calculate_task_statistics()
                display_statistics(task_statistics)
            elif menu == 'e':
                print('Goodbye!!!')
                exit()
            else:
                print("Invalid input. Please try again.")
    elif username in user_names and password == pass_words[user_names.index(username)]:
        print("Regular user login successful.")
        while True:
            # Regular user menu options
            menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

            if menu == 'a':
                add_task(username)
            elif menu == 'va':
                view_all_tasks()
            elif menu == 'vm':
                view_my_tasks(username)
            elif menu == 'e':
                print('Goodbye!!!')
                exit()
            else:
                print("Invalid input. Please try again.")
    else:
        print("Invalid username or password. Please try again.")