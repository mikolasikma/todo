import datetime

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False
        self.due_date = None

def createTask(taskName):
    task=Task(taskName)
    return task

def printAllTasks():
    global tasks
    tasksSorted = sorted(tasks, key=lambda x: x.completed)
    for index,task in enumerate(tasksSorted):
        if task.completed:
            status = "Done"
        else:
            status = "Not done"
        if task.due_date:
            print(index + 1 ,"\t - ", task.name, "\t - ", status , "\t due ", task.due_date.strftime("%x"))
        else:
            print(index + 1 ,"\t - ", task.name, "\t - ", status)
        if index + 1 < len(tasksSorted) and task.completed != tasksSorted[index + 1].completed:
            print ("----------------------")
        
        tasks = tasksSorted

def markTaskAsDone(taskId):
    taskId.completed = True

def markTaskAsNotDone(taskId):
    taskId.completed = False

def deleteTask(taskId):
    del tasks[taskId]

def addDueDate(taskId):
    print("Adding a due date for task ",tasks[taskId].name)
    currentDate = datetime.datetime.now()

    while True:
        try:
            year = 0
            while year < currentDate.year:
                year = int(input("Specify a year for the due date: "))
            month = 0
            while month < 1 or month > 12 or (year == currentDate.year and month < currentDate.month):
                month = int(input("Specify a month for the due date[1 - 12]: "))
            day = 0
            while day < 1 or day > 31:
                day = int(input("Specify a day for the due date[1 - 31]: "))
            tasks[taskId].due_date = datetime.datetime(year, month, day)
            print("You've successfully added the date ", tasks[taskId].due_date.strftime("%x"), "to task ", tasks[taskId].name)
            break
        except ValueError:
            print("Date is not valid, please try again")

def deleteDueDate(taskId):
    tasks[taskId].due_date = None
    print("You've removed due date from task ", tasks[taskId].name)
    
def loadListFromFile():
    f = open ("data/taskListFile.txt","r")
    data = f.read()
    listVar = data.split("\n")
    for index,item in enumerate(listVar):
        taskData = item.split("\t")
        try:
            tasks.append(createTask(taskData[1]))
            print("You've loaded a task from file with name ", taskData[1])
            if taskData[2] == "Done":
                markTaskAsDone(tasks[index])
            if taskData[3] != 'None':
                due_date_components = taskData[3].split("/")
                if len(due_date_components) == 3:
                    try:
                        print("The task day is: ",due_date_components[0], "The task month is: ", due_date_components[1], "The task year is: ",due_date_components[2])
                        tasks[index].due_date = datetime.datetime(int(due_date_components[0]),int(due_date_components[1]),int(due_date_components[2]))
                    except ValueError:
                        print("Invalid date components in the file")
        except IndexError:
            print("Load done")
    f.close

def saveListIntoFile():
    f = open ("data/taskListFile.txt", "w")
    for index,task in enumerate(tasks):
        if task.completed == True:
            completed = "Done"
        else:
            completed = "Not done"
        if task.due_date is not None:
            due_date_str = task.due_date.strftime("%x")
        else:
            due_date_str = ""
        task_info = f"{index + 1}\t{task.name}\t{completed}\t{due_date_str}\n"
        f.write(task_info)
    f.close


tasks = []
loadListFromFile()

print("This is a task to-do list!")

while True:
    print("Make your choice: ")
    print("1. Add a task")
    print("2. Print all tasks")
    print("3. Mark a task as done")
    print("4. Mark a task as not done")
    print("5. Delete a task")
    print("6. Add a due date for a task")
    print("7. Delete a due date from a task")
    print("8. Save and quit")

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
        notDoneChoice = int(input("Enter which task you want to mark as not done: "))
        try:
            markTaskAsNotDone(tasks[notDoneChoice - 1])
            print("You've marked task ", tasks[notDoneChoice - 1].name , " as not done")
            printAllTasks()
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
        except ValueError:
            print("Please enter a valid number as your task choice")
    elif choice == '5':
        printAllTasks()
        deleteChoice = int(input("Enter which task you want to delete: "))
        try:
            print("You deleted a task with the name ", tasks[deleteChoice -1].name)
            deleteTask(deleteChoice - 1)
        except ValueError:
            print("Please enter a valid number as your task choice")
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
    elif choice == '6':
        printAllTasks()
        dueDateChoice = int(input("Enter the task ID to which you want to add a due date: "))
        try:
            addDueDate(dueDateChoice - 1)
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
    elif choice == '7':
        printAllTasks()
        dueDateDeleteChoice = int(input("Enter which task's due date you want to delete: "))
        try:
            deleteDueDate(dueDateDeleteChoice - 1)
        except IndexError:
            print("Invalid task ID provided, please choose from the list")
    elif choice == '8':
        saveListIntoFile()
        break