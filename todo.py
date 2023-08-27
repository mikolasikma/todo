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

def loadListFromFile():
    f = open ("taskListFile.txt","r")
    data = f.read()
    listVar = data.split("\n")
    for index,item in enumerate(listVar):
        taskData = item.split("\t")
        try:
            tasks.append(createTask(taskData[1]))
            print("You've loaded a task from file with name ", taskData[1])
            if taskData[2] == "Done":
                markTaskAsDone(tasks[index])
        except IndexError:
            print("Load done")
    f.close

tasks = []
loadListFromFile()

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
        print("You've created a task with name ", taskName)
        printAllTasks()
    elif choice == '2':
        printAllTasks()
    elif choice == '3':
        printAllTasks()
        doneChoice = int(input("Enter which task you want to mark as done: "))
        try:
            markTaskAsDone(tasks[doneChoice - 1])
            print("You've marked task ", tasks[doneChoice - 1].name , " as done")
            printAllTasks()
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
        except ValueError:
            print("Please enter a valid number as your task choice")
    elif choice == '4':
        printAllTasks()
        deleteChoice = int(input("Enter which task you want to delete: "))
        try:
            print("You deleted a task with the name ", tasks[deleteChoice -1].name)
            deleteTask(deleteChoice - 1)
        except ValueError:
            print("Please enter a valid number as your task choice")
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
    elif choice == '5':
        break

f = open ("taskListFile.txt", "w")
for index,task in enumerate(tasks):
    if task.completed == True:
        completed = "Done"
    else:
        completed = "Not done"
    task_info = f"{index + 1}\t{task.name}\t{completed}\n"
    f.write(task_info)
f.close