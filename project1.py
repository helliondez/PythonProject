from datetime import datetime
listTasks = []
count = 0

def addTask(inputprompt):
    global count
    now = datetime.now()
    taskData = {}
    count += 1
    taskData["id"] = count
    taskData["status"] = "todo"
    taskData["description"] = inputprompt
    taskData["createdAt"] = now.strftime("%b %d %Y %I:%M%p")
    taskData["updatedAt"] = taskData["createdAt"]
    listTasks.append(taskData)

def changeTask(x, inputprompt):
    now = datetime.now()
    found = False
    for itemWithTonsOfKeysForTheUserCreatedTask in listTasks:
        if itemWithTonsOfKeysForTheUserCreatedTask["id"] == int(x):
            itemWithTonsOfKeysForTheUserCreatedTask["description"] = inputprompt
            itemWithTonsOfKeysForTheUserCreatedTask["updatedAt"] = now.strftime("%b %d %Y %I:%M%p")
            found = True
    if not found:
        print("task not found to change.")

def removeTask(inputprompt):
    found = False
    for itemWithTonsOfKeysForTheUserCreatedTask in listTasks:
        if itemWithTonsOfKeysForTheUserCreatedTask["id"] == int(inputprompt):
            listTasks.remove(itemWithTonsOfKeysForTheUserCreatedTask)
            found = True
    if not found:
        print("task not found to delete.")

def markTask(place, taskStatus):
    if taskStatus == "done":
        for itemWithTonsOfKeysForTheUserCreatedTask in listTasks:
            if itemWithTonsOfKeysForTheUserCreatedTask["id"] == int(place):
                itemWithTonsOfKeysForTheUserCreatedTask["status"] = taskStatus
    elif taskStatus == "in-progress":
        for itemWithTonsOfKeysForTheUserCreatedTask in listTasks:
            if itemWithTonsOfKeysForTheUserCreatedTask["id"] == int(place):
                itemWithTonsOfKeysForTheUserCreatedTask["status"] = taskStatus

def main():
    userInput = ""
    
    while True:

        option = input("What option? ")

        if option == "add":
            userInput = input("add your task: ")
            addTask(userInput)

        elif option == "change":
            place = input("which task? ")
            userInput = input(f"changing your task at {place}: ")
            changeTask(place, userInput)

        elif option == "delete":
            userInput = input("which task to delete?: ")
            removeTask(userInput)
        
        elif option == "mark task":
            place = input("Which task? ")
            userInput = input("change to either done or in-progress")
            markTask(place, userInput)

        elif option == "list":
            for task in listTasks:
                print(f"{task}\n")

        elif option == "list done":
            for task in listTasks:
                if task["status"] == "done":
                    print(f"{task}\n")

        elif option == "list todo":
            for task in listTasks:
                if task["status"] == "todo":
                    print(f"{task}\n")

        elif option == "list in-progress":
            for task in listTasks:
                if task["status"] == "in-progress":
                    print(f"{task}\n")

        else:
            print("Lame")

if __name__ == "__main__":
    main()