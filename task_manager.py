#=====importing libraries===========
import datetime

# Create an empty dictionary to store usernames and passwords
user_credentials = {}

#====Login Section====
# Read user credentials from "user.txt"
with open("user.txt", "r") as user_file:
    for line in user_file:
        username, password = line.strip().split(', ')
        user_credentials[username] = password

while True:
    username = input("Enter your username: ")

    if username in user_credentials:
        password = input("Enter your password: ")
        if password == user_credentials[username]:
            is_admin = (username == "admin")

            while True:
                menu = input(f'''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
{"r - register a user" if is_admin else ""}
{"s - view statistics" if is_admin else ""}
: ''').lower()

                if is_admin:
                    if menu == 'r':
                        new_username = input("Enter a new username: ")
                        if new_username in user_credentials:
                            print("Username already exists. Choose a different username.")
                        else:
                            new_password = input("Enter a new password: ")
                            confirm_password = input("Confirm the password: ")
                            if new_password == confirm_password:
                                user_credentials[new_username] = new_password
                                with open("user.txt", "a") as user_file:
                                    user_file.write(f"\n{new_username}, {new_password}\n")
                                print("User registered successfully.")
                            else:
                                print("Passwords do not match. User registration failed.")
                            continue

                    elif menu == 's':
                        num_users = len(user_credentials)
                        with open("tasks.txt", "r") as task_file:
                            tasks = task_file.readlines()
                        num_tasks = len(tasks)
                        print(f"Number of registered users: {num_users}")
                        print(f"Number of tasks: {num_tasks}")

                if menu == 'a':
                    assigned_to = username if username != "admin" else input("Enter the username of the person the task is assigned to: ")
                    task_title = input("Enter the title of the task: ")
                    task_description = input("Enter the description of the task: ")
                    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

                    # Ensure date format is consistent
                    try:
                        datetime.datetime.strptime(due_date, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        continue

                    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    with open("tasks.txt", "a") as task_file:
                        task_file.write(f"{assigned_to}, {task_title}, {task_description}, {due_date}, {current_date}, No\n")
                    print("Task added successfully.")

                elif menu == 'va':
                    with open("tasks.txt", "r") as task_file:
                        tasks = task_file.readlines()
                    if tasks:  # Check if there are tasks available
                        print("All Tasks:")
                        for task in tasks:
                            task_data = task.strip().split(", ")
                            if len(task_data) == 6:
                                assigned_to, task_title, task_description, due_date, current_date, status = task_data
                                print(f"Assigned to: {assigned_to}")
                                print(f"Task Title: {task_title}")
                                print(f"Description: {task_description}")
                                print(f"Due Date: {due_date}")
                                print(f"Created Date: {current_date}")
                                print(f"Status: {status}\n")
                                print("-" * 30)
                            else:
                                print(f"Invalid task format: {task}")
                    else:
                        print("No tasks available.")

                elif menu == 'vm':
                    with open("tasks.txt", "r") as task_file:
                        tasks = task_file.readlines()
                    user_tasks = []
                    if tasks:
                        for task in tasks:
                            task_data = task.strip().split(", ")
                            if len(task_data) == 6:
                                assigned_to, task_title, task_description, due_date, current_date, status = task_data
                                if assigned_to == username:
                                    task_dict = {
                                        "Assigned to": assigned_to,
                                        "Task Title": task_title,
                                        "Description": task_description,
                                        "Due Date": due_date,
                                        "Created Date": current_date,
                                        "Status": status
                                    }
                                    user_tasks.append(task_dict)

                        if user_tasks: # Check if there are tasks available for the user
                            print(f"Tasks for {username}:")
                            for task in user_tasks:
                                print("Task Details:")
                                for field, value in task.items():
                                    print(f"{field}: {value}")
                                print("-" * 30)
                        else:
                            print(f"No tasks available for {username}.")

                elif menu == 'e':
                    print('Goodbye!!!')
                    break
                else:
                    print("Invalid input. Please try again.")

        else:
            print("Incorrect password. Access denied.")
    else:
        print("Username not found. Access denied.")