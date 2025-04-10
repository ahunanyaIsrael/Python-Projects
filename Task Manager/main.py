import os

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def displayMenue():
    # clearScreen()

    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")
    print("=======================")

def addTask(ls):
    title = input("Enter Task Title: ")
    ls.append({"title": title, "completed": False})
    print(f"Task {title} added Successfully")

def viewTasks(ls):
    
    if not ls:
        print("No task Found")
        return
    print("\n=== My Tasks  ====")

    for index, task in enumerate(ls):
        status = "✔ " if task["completed"] == True else " "
        print(f"{index + 1}. [{status}] {task["title"]}")
    print("==============================================\n")
 
def complete_task(ls):
    viewTasks(ls)
    if not ls:
        return
    try:
        task_number = int(input("Enter task number to mark as completed"))
        if task_number <1 or task_number > len(ls):
            print("invalid Task number")
            return
        
        task_to_completed = ls[task_number - 1 ]
        task_to_completed["completed"] = True
        print(f"Task '{task_to_completed["title"]}' marked as completed! ")
    except ValueError:
        print("Please enter a valid number")

def deleteTask(ls):
    viewTasks(ls)
    if not ls:
        return
    try:
        task_number = int(input("Enter task number  to delete: "))
        if task_number < 1 or task_number > len(ls):
            return
        delete_task = ls.pop(task_number -1)
        print(f"Task {delete_task["title"]} deletedd sunccesfully")
    except ValueError:
        print("please enter a valid number")

def main(TaskList):
    while True:  
        displayMenue()

        choice = input("Enter You choice (1-4): ")

        match choice:
            case "1":
                addTask(TaskList)
            case "2":
                viewTasks(TaskList)
            case "3":
                complete_task(TaskList)
            case "4":
                deleteTask(TaskList)
            case "0":
                break
            case _:
                print("Invalid Choice. Please Go with (0-4)")

    

TaskList = []

main(TaskList)

