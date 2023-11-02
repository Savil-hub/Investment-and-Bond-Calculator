import datetime

def today():
    return datetime.datetime.now().strftime("%d %b %Y")

def reg_user(user_list):
    while True:
        new_username = input("Enter a new username: ")

        if new_username in user_list:
            print(f"{new_username} already exists. Choose a different username.")
            continue

        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm the password: ")

        if new_password == confirm_password:
            # Store the user data securely, e.g., in a dictionary or database
            user_data = {'username': new_username, 'password': new_password}
            user_list.append(user_data)
            with open("user.txt", "a") as user_file:
                user_file.write(f"{new_username}, {new_password}\n")  # Save user data to 'users.txt'
            print("User registered successfully.")
            break
        else:
            print("Passwords do not match. User registration failed.")


# Shows all the tasks created, their title, description, how many there are, and the date created
def view_all_tasks():
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
    if tasks:
        print("All Tasks:")
        i = 1
        for task in tasks:
            assigned_to, task_title, task_description, due_date, current_date, status = task.strip().split(", ", 5)
            print(f"Task {i}:")
            print(f"Assigned to: {assigned_to}")
            print(f"Task Title: {task_title}")
            print(f"Description: {task_description}")
            print(f"Due Date: {due_date}")
            print(f"Created Date: {current_date}")
            print(f"Status: {status}\n")
            print("-" * 30)
            i += 1
    else:
        print("No tasks available.")

# Shows the tasks for the user, their title, description, how many there are, and the date created and if they are completed
def view_my_tasks(username):
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()

    user_tasks = []
    if tasks:
        print(f"Tasks for {username}:")
        i = 1
        for task in tasks:
            task_data = task.strip().split(", ")
            if len(task_data) != 6:
                print(f"Skipping invalid task data: {task_data}")
                continue
            assigned_to, task_title, task_description, due_date, current_date, status = task_data
            if assigned_to == username:
                user_tasks.append((i, task_data))
                print(f"Task {i}:")
                print(f"Assigned to: {assigned_to}")
                print(f"Task Title: {task_title}")
                print(f"Description: {task_description}")
                print(f"Due Date: {due_date}")
                print(f"Created Date: {current_date}")
                print(f"Status: {status}")
                print("-" * 30)
            i += 1
    else:
        print("No tasks available.")


    while True:
        task_number = input("Enter the task number to edit (or -1 to return to the main menu): ")

        if task_number == '-1':
            break

        if not task_number.isdigit():
            print("Invalid input. Please enter a valid task number.")
            continue

        task_number = int(task_number)

        if not (1 <= task_number <= len(user_tasks)):
            print("Invalid task number. Please enter a valid task number.")
            continue

        i, task_data = user_tasks[task_number - 1]
        assigned_to, task_title, task_description, due_date, current_date, status = task_data

        # Now, you can edit the specific fields as needed.
        print(f"Editing Task {i}:")
        print(f"1. Assigned to: {assigned_to}")
        print(f"2. Task Title: {task_title}")
        print(f"3. Description: {task_description}")
        print(f"4. Due Date: {due_date}")
        print(f"5. Status: {status}")

        edit_option = input("Enter the number of the field to edit (or 0 to return): ")

        if edit_option == '0':
            break

        if edit_option == '1':
            new_assigned_to = input("Enter the new assigned user: ")
            tasks[tasks.index(task)] = ', '.join([new_assigned_to, task_title, task_description, due_date, current_date, status])
            print("Assigned user updated successfully.")

def add_task(username):
    assigned_to = input("Enter the username to whom the task should be assigned: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (DD Mon YYYY): ")

    try:
        datetime.datetime.strptime(due_date, "%d %b %Y")
        current_date = today()
        with open("tasks.txt", "a") as task_file:
            task_file.write(f"{assigned_to}, {task_title}, {task_description}, {due_date}, {current_date}, No\n")
        print("Task added successfully.")
    except ValueError:
        print("Invalid date format. Please use DD Mon YYYY.")

def calculate_task_statistics():
    # Get the current date using the 'today' function
    current_date = today()

    # Open the 'tasks.txt' file to read task data
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()

    # Initialize variables to store task statistics
    total_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0

    # Iterate through tasks and calculate statistics
    for task in tasks:
        task_data = task.strip().split(", ")
        if len(task_data) != 6:
            print(f"Skipping invalid task data: {task_data}")
            continue

        due_date = task_data[3]

        total_tasks += 1
        if task_data[-1] == 'Yes':
            completed_tasks += 1
        if datetime.datetime.strptime(due_date, "%d %b %Y") < datetime.datetime.strptime(current_date, "%d %b %Y"):
            overdue_tasks += 1

    # Calculate various task statistics
    incomplete_tasks = total_tasks - completed_tasks  # Number of incomplete tasks
    percentage_incomplete = (incomplete_tasks / total_tasks) * 100  # Percentage of incomplete tasks
    percentage_overdue = (overdue_tasks / total_tasks) * 100  # Percentage of overdue tasks

    # Return the calculated statistics
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "incomplete_tasks": incomplete_tasks,
        "overdue_tasks": overdue_tasks,
        "percentage_incomplete": percentage_incomplete,
        "percentage_overdue": percentage_overdue,
        "percentage_completed": (completed_tasks / total_tasks) * 100,
    }


def generate_task_overview():
    # Calculate task statistics using the 'calculate_task_statistics' function
    result = calculate_task_statistics()

    # Check if the result is a dictionary and contains the necessary keys
    if isinstance(result, dict) and 'total_tasks' in result and 'completed_tasks' in result and 'incomplete_tasks' in result and 'overdue_tasks' in result and 'percentage_incomplete' in result and 'percentage_overdue' in result:
        total_tasks = result['total_tasks']
        completed_tasks = result['completed_tasks']
        incomplete_tasks = result['incomplete_tasks']
        overdue_tasks = result['overdue_tasks']
        percentage_incomplete = result['percentage_incomplete']
        percentage_overdue = result['percentage_overdue']

        # Create a formatted task overview report
        task_overview = f"Total number of tasks: {total_tasks}\n"
        task_overview += f"Total number of completed tasks: {completed_tasks}\n"
        task_overview += f"Total number of incomplete tasks: {incomplete_tasks}\n"
        task_overview += f"Total number of overdue tasks: {overdue_tasks}\n"
        task_overview += f"Percentage of incomplete tasks: {round(percentage_incomplete, 2)}%\n"
        task_overview += f"Percentage of overdue tasks: {round(percentage_overdue, 2)}%\n"

        # Write the task overview report to 'task_overview.txt' file
        with open("task_overview.txt", "w") as task_file:
            task_file.write(task_overview)
        print("Task overview report generated successfully")
    else:
        print("Error: 'calculate_task_statistics' did not return the expected dictionary structure.")

def generate_user_overview():
    # Read user data from a list (e.g., user_data_list)
    user_data_list = [
        {"username": "user1", "tasks_assigned": 5, "completed_tasks": 3, "overdue_tasks": 1},
        {"username": "user2", "tasks_assigned": 8, "completed_tasks": 6, "overdue_tasks": 0},
        # Add more user data as needed
    ]

    # Create a formatted user overview report
    user_overview = "User Overview:\n"
    for user_data in user_data_list:
        username = user_data["username"]
        tasks_assigned = user_data["tasks_assigned"]
        completed_tasks = user_data["completed_tasks"]
        overdue_tasks = user_data["overdue_tasks"]

        percentage_completed = (completed_tasks / tasks_assigned) * 100
        percentage_overdue = (overdue_tasks / tasks_assigned) * 100

        user_overview += f"User: {username}\n"
        user_overview += f"Tasks Assigned: {tasks_assigned}\n"
        user_overview += f"Completed Tasks: {completed_tasks}\n"
        user_overview += f"Overdue Tasks: {overdue_tasks}\n"
        user_overview += f"Percentage Completed: {round(percentage_completed, 2)}%\n"
        user_overview += f"Percentage Overdue: {round(percentage_overdue, 2)}%\n"
        user_overview += "-" * 30 + "\n"

    # Write the user overview report to 'user_overview.txt' file
    with open("user_overview.txt", "w") as user_file:
        user_file.write(user_overview)
        print("User overview report generated successfully.")

def display_statistics(task_statistics):
    # Extract task statistics from the dictionary
    total_tasks = task_statistics["total_tasks"]
    completed_tasks = task_statistics["completed_tasks"]
    incomplete_tasks = task_statistics["incomplete_tasks"]
    overdue_tasks = task_statistics["overdue_tasks"]
    percentage_incomplete = task_statistics["percentage_incomplete"]
    percentage_overdue = task_statistics["percentage_overdue"]
    percentage_completed = task_statistics["percentage_completed"]

    # Display statistics
    print("System Statistics:")
    print(f"Total number of tasks: {total_tasks}")
    print(f"Total number of completed tasks: {completed_tasks}")
    print(f"Total number of incomplete tasks: {incomplete_tasks}")
    print(f"Total number of overdue tasks: {overdue_tasks}")
    print(f"Percentage of completed tasks: {round(percentage_completed, 2)}%")
    print(f"Percentage of incomplete tasks: {round(percentage_incomplete, 2)}%")
    print(f"Percentage of overdue tasks: {round(percentage_overdue, 2)}%")
