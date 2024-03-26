# Project Requirements
# 1. User Interface (UI):  # 2. To-Do List Features:  # 3. User Interaction:  # 4. Error Handling:
# 5. Code Organization:  # 6. Testing and Debugging:  # 7. Documentation:  # 8. Optional Features (Bonus):
# 9. GitHub Repository:

tasks = [] # List of tasks
def cli(): # Command Line Interface
    user_input = input("""
    Welcome to the To-Do List App! 📝✨
    
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
                       
    """)
    try:
        if int(user_input) == 1:   # 1. Add a task
            add_task() 
        elif int(user_input) == 2: # 2. View tasks
            view_task()
        elif int(user_input) == 3: # 3. Mark a task as complete
            mark_complete()
        elif int(user_input) == 4: # 4. Delete a task
            delete_task()
        elif int(user_input) == 5: # 5. Quit
            quit()
        else: # Error Handling when the user inputs an invalid number
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ") 
        cli() # back to the cli function (main menu)
    except (ValueError, OverflowError): # Error Handling when the user inputs a string or overflow 
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        cli() # back to the cli function (main menu)

def add_task(): 
    task = input("\nWhat task would you like to add? (Back) ") # Adding a task
    if task.lower() == "back": # Back to the main menu
        cli() # back to the cli function (main menu)
    elif task.isspace() == True: # Error Handling for spaces
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        add_task() # back to the add_task function
    elif task == "": # Error Handling for empty input
        print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        add_task() # back to the add_task function
    else: # Adding the task to the list
        tasks.append([task, False]) # Adding the task to the list
        add_task() # back to the add_task function 

def view_task(): 
    print(f"\nHere are your tasks so far:\n ") # Viewing the tasks
    for task in tasks: # Looping through the tasks
        if task[1] == True: # If the task is complete
            print(f"{task[0]}. ---> COMPLETE✅ 🤩") 
        elif task[1] == False: # If the task is incomplete
            print(f"{task[0]}. ---> INCOMPLETE❌ 🙄")
    input("\nPress enter to go back  ") # Going back to the main menu
    cli() 

def mark_complete():
    print("\nPick the task you completed: (Back)\n") # Marking the task as complete
    for i in range(len(tasks)): # Looping through the tasks
        if tasks[i][1] == True: # If the task is complete
            print(f"{i+1}: {tasks[i][0]} ---> COMPLETE✅ 🤩") # Displaying completed tasks
        if tasks[i][1] == False: # If the task is incomplete
            print(f"{i+1}: {tasks[i][0]} ---> INCOMPLETE❌ 🙄") # Displaying incompleted tasks         
    user_input = input() 
    if user_input.lower() == "back": # Going back to the main menu
        cli() 
    else: # If the user inputs a number
        try: 
            tasks[int(user_input)-1][1] = True # input the task number and mark it as complete
        except (IndexError, ValueError, OverflowError): # Error Handling for overflow, out of range and invalid input
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        finally: 
            mark_complete() # back to the mark_complete function
            
def delete_task():
    print("\nPick a task you want to delete: (Back)\n") # Deleting a task
    for i in range(len(tasks)): # Looping through the tasks
        print(f"{i+1}: {tasks[i][0]}") # Displaying the tasks
    user_input = input()
    if user_input.lower() == "back": # Going back to the main menu
        cli()
    else: # If the user inputs a number
        try:
            tasks.pop(int(user_input)-1) # input the task number and delete it
        except (ValueError, IndexError, OverflowError): # Error Handling for overflow, out of range and invalid input
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        finally: # back to the delete_task function
            delete_task()
cli() # Starting the CLI (Command Line Interface)

