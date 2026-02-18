Username = input("What name would you like to use to track your progress?")
Password = input("What password would you like to use to track your progress?")
print("Is this correct Username: " + Username + " Password: " + Password + " (yes or no)")
if input().lower() == "no":
    print("Please re-enter your username and password")
    Username = input("What name would you like to use to track your progress?")
    Password = input("What password would you like to use to track your progress?")
clubs = []
while True:
    club = input("What clubs are you in? Type done when finished")
    if club.lower() == "done" or " done":
        break
    else:
        clubs.append(club)
List_of_Usernames = []
List_of_Passwords = []
List_of_Usernames.append(Username)
List_of_Passwords.append(Password)
print("Your username and password have been saved, you can now use them to track your progress")
periods = []
periods.append(input("What is your first period?"))
periods.append(input("What is your second period?"))
periods.append(input("What is your third period?"))
periods.append(input("What is your fourth period?"))
periods.append(input("What is your fifth period?"))
periods.append(input("What is your sixth period?"))
periods.append(input("What is your seventh period?"))
periods.append(input("What is your eighth period?"))

print("Your periods have been saved, you can now use them to track your progress")
tasks = []
while True:
    action = input("Type add to enter a task, view to see tasks, delete to delete a task, edit to edit a task, due date to add a due date to a task,progress to log progress on a task or quit to exit: ").lower()
    if action == "add":
        task_class = input("Which class is this task for?")
        if task_class in periods:
            task_name = input("What is the task you want to track for " + task_class + "?")
            tasks.append(task_class + ": " + task_name)
            print("Your task has been saved")
        elif task_class in clubs:
            task_name = input("What is the task you want to track for " + task_class + "?")
            tasks.append(task_class + ": " + task_name)
            print("Your task has been saved")
        else:
            print("That class does not exist")
    elif action == "view":
        if len(tasks) == 0:
            print("No tasks saved")
        else:
            for task in tasks:
                print(task)
    elif action == "quit":
        break
    elif action == "delete":
        task_to_delete = input("Which task would you like to delete?")
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            print("Task deleted")
        else:
            print("That task does not exist")
    elif action == "edit":
        task_to_edit = input("Which task would you like to edit?")
        if task_to_edit in tasks:
            new_task_name = input("What is the new name for this task?")
            tasks[tasks.index(task_to_edit)] = new_task_name
            print("Task edited")
    elif action == "due date" or action == "due" or action == "date":
        task_to_edit = input("Which task would you like to add a due date to?")
        if task_to_edit in tasks:
            due_date = input("What is the due date for this task?")
            tasks[tasks.index(task_to_edit)] = task_to_edit + " Due: " + due_date
            print("Due date added")
    elif action == "progress":
        task_to_edit = input("Which task would you like to log progress on?")
        if task_to_edit in tasks:
            progress = input("What progress have you made on this task?")
            tasks[tasks.index(task_to_edit)] = task_to_edit + " Progress: " + progress
            print("Progress logged")
    
        else:
            print("That task does not exist")
    else:
        print("Invalid option")

