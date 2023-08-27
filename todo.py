class Task:
    def __init__(self, name):
        self.name=name
        self.completed=False

def createTask(taskName):
    task=Task(taskName)
    return task

def printAllTasks():
    for index,task in enumerate(tasks):
        if task.completed:
            status = "Done"
        else:
            status = "Not done"
        print(index + 1 ,"\t - ", task.name, "\t - ", status)

def markTaskAsDone(taskId):
    taskId.completed = True

def deleteTask(taskId):
    del tasks[taskId]

tasks = []

tasks.append(createTask("Learn Java"))

print("This is a task to-do list!")

while True:
    print("Make your choice: ")
    print("1. Add a task")
    print("2. Print all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        taskName = input("Enter the task name: ")
        tasks.append(createTask(taskName))
    elif choice == '2':
        printAllTasks()
    elif choice == '3':
        printAllTasks()
        doneChoice = int(input("Enter which task you want to mark as done: "))
        try:
            markTaskAsDone(tasks[doneChoice - 1])
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
        except ValueError:
            print("Please enter a valid number as your task choice")
    elif choice == '4':
        printAllTasks()
        deleteChoice = int(input("Enter which task you want to delete: "))
        try:
            deleteTask(deleteChoice - 1)
        except ValueError:
            print("Please enter a valid number as your task choice")
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
    elif choice == '5':
        break