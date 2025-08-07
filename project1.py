listTasks = []
count = 0
#this is just a thing i dont fully understand
#but maybe one day it will fit into my brain
def addTask(inputprompt):
    global count
    taskData = {}
    count += 1
    taskData["id"] = count
    taskData["status"] = "todo"
    taskData["description"] = inputprompt
    taskData["createdAt"] = "when it was made"
    taskData["updatedAt"] = taskData["createdAt"]
    listTasks.append(taskData)
def changeTask(x, inputprompt):
    for items in listTasks:
        if items == x:
            print("hi!")
    listTasks[x] = inputprompt
def removeTask(inputprompt):
    for items in listTasks:
        if items["id"] == inputprompt:
            listTasks.remove(items)
        else:
            print("your crazy thats not real")
def main():
    userInput = ""
    while True:
        for tasks in listTasks:
            print(f"{tasks}\n")
        option = input("wat you doin'? ")
        if option == "add":
            userInput = input("Enter something: ")
            addTask(userInput)
        elif option == "change":
            place = input("which place?")
            userInput = input("Enter something: ")
            changeTask(place, userInput)
        elif option == "delete":
            userInput = input("Enter something: ")
            removeTask(userInput)
        else:
            print("Lame")
if __name__ == "__main__":
    main()