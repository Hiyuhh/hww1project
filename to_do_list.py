# Project Requirements
# 1. User Interface (UI):  # 2. To-Do List Features:  # 3. User Interaction:  # 4. Error Handling:
# 5. Code Organization:  # 6. Testing and Debugging:  # 7. Documentation:  # 8. Optional Features (Bonus):
# 9. GitHub Repository:

# tasks = []
tasks = [["This is a task", False], ["Another task", True]]
def cli():
    user_input = input("""
    Welcome to the To-Do List App!
    
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
                       
    """)
    try:
        if int(user_input) == 1:
            add_task()
        elif int(user_input) == 2:
            view_task()
        elif int(user_input) == 3:
            mark_complete()
        elif int(user_input) == 4:
            delete_task()
        elif int(user_input) == 5:
            quit()
        else:
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        cli()
    except (ValueError, OverflowError):
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        cli()

def add_task():
    task = input("\nWhat task would you like to add? (Back) ")
    if task.lower() == "back":
        cli()
    if task == "":
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        add_task()
    else:
        tasks.append([task, False])
        add_task()

def view_task():
    print(f"\nHere are your tasks so far:\n ")
    for task in tasks:
        if task[1] == True:
            print(f"{task[0]}. ---> COMPLETE 🤩")
        elif task[1] == False:
            print(f"{task[0]}. ---> INCOMPLETE 🙄")
    input("\nPress enter to go back  ")
    cli()

def mark_complete():
    print("\nPick the task you completed: (Back)\n")
    for i in range(len(tasks)):
        if tasks[i][1] == True:
            print(f"{i+1}: {tasks[i][0]} ---> COMPLETE 🤩")
        if tasks[i][1] == False:
            print(f"{i+1}: {tasks[i][0]} ---> INCOMPLETE 🙄")            
    user_input = input()
    if user_input.lower() == "back":
        cli()
    else:
        try:
            tasks[int(user_input)-1][1] = True
            mark_complete()
        except (IndexError, ValueError, OverflowError):
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
            mark_complete()
            
def delete_task():
    try:
        print("\nPick a task you want to delete: (Back)\n")
        for i in range(len(tasks)):
            print(f"{i+1}: {tasks[i][0]}")
        user_input = input()
        if user_input.lower() == "back":
            cli()
        else:
            tasks.pop(int(user_input)-1)
            delete_task()
    except (ValueError, IndexError, OverflowError):
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        delete_task()
cli()

