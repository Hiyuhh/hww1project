<!--[readme.md](https://github.com/Hiyuhh/hww1project/files/14751986/readme.md)[Uploading readme.md…]-->
# **To-Do List Application**

*The To-Do List application is a tool designed to help users manage their tasks.*   
*The purpose of the application is to help users achieve their goals more efficiently, stay productive, and keep them on track of what needs to be done in their personalized To-Do List.*

## User interaction

**Menu Preview (Command-Line):**  
*Users start by choosing the function they wish to use, by entering the number associated with the option.*
```
    Welcome to the To-Do List App! 📝✨
    
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
```
<br />
<br />

**1. Add a task:** *Is where users add tasks to the list. This can be done by typing them into the application, once a user adds a task to the (Add a task) function, it will redirect them to add another task, and will be displayed as such:*

```
What task would you like to add? (Back) Task Test
What task would you like to add? (Back) 
```
*When a user is done adding tasks and wishes to go back to the menu, they can achieve that by typing in 'back', as seen below:*

```
What task would you like to add? (Back) back
    Welcome to the To-Do List App! 📝✨
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
```
<br />
<br />

**2. View tasks:** *This is where users would frequently visit to view their tasks, observing which ones require completion and which are completed. The (View tasks) function is strictly for observation as there is no user input required. Once users are done viewing their tasks they can simply press 'enter' to go back to the menu, as seen below:*
```
Here are your tasks so far:
Task Test. ---> INCOMPLETE❌ 🙄
Task Test2. ---> COMPLETE✅ 🤩
Press enter to go back
```
<br />
<br />

**3. Mark a task as complete:** *This function is where users can mark their tasks as complete, by typing in the number associated with the task as seen below, by selecting '1' for the incomplete task:* 
```
Pick the task you completed: (Back)
1: Task Test ---> INCOMPLETE❌ 🙄
2: Task Test2 ---> COMPLETE✅ 🤩
1
Pick the task you completed: (Back)
1: Task Test ---> COMPLETE✅ 🤩
2: Task Test2 ---> COMPLETE✅ 🤩
```
*When a user is done marking their tasks and wishes to go back to the menu, they can achieve that by typing in 'back', as seen below:*
```
Pick the task you completed: (Back)
1: Task Test ---> COMPLETE✅ 🤩
2: Task Test2 ---> COMPLETE✅ 🤩
back
    Welcome to the To-Do List App! 📝✨
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
```
<br />
<br />

**4. Delete a task:** *If a user wants to delete a task for any reason, they can do that in this function. Once they decide on the task they wish to delete, they can simply, type in the number associated with the task, as seen below:*
```
Pick a task you want to delete: (Back)
1: Task Test
2: Task Test2
2
Pick a task you want to delete: (Back)
1: Task Test
```
*When a user is done deleting their tasks and wishes to go back to the menu, they can achieve that by typing in 'back', as seen below:*
```
Pick a task you want to delete: (Back)
1: Task Test
back
    Welcome to the To-Do List App! 📝✨
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
```
<br />
<br />

**5. Quit:** *When a user is done using the application and wishes to quit, they can achieve that by entering the number '5' in the menu screen, as seen below:* 
```
Welcome to the To-Do List App! 📝✨
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    5
    
>>
```

## Invalid Input

**Error Messages:** *If a user attempts to input or execute something that is not within the application's capabilities or requirements, the application would generate an error message for the user, as seen below:*
```
Invalid Input.. Try again! ༼ つ ◕_◕ ༽つ
```
**Possible Causes:** *The error message shown above could occur due to various reasons, such as marking a non-existent task as complete, deleting a non-existent task, creating a task with no input, or encountering a technical glitch.*

**Resolution:** *To resolve the issue, the user would need to review their input, ensure that it meets the application's capabilities, and correct any mistakes they may have inputted.*

## Authors

**This application was a group effort created by:**     

*Haya Mubaidin* https://github.com/Hiyuhh    
*Adam Cifelli* https://github.com/AdamC13    
*Savannah Lyles* https://github.com/Savvy325
