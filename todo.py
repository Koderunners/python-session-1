import json 

todoList = []

try:
    with open ('todofile', 'r') as todofile:
        todoList = json.load(todofile)
except FileNotFoundError:
    pass 

def display():
    for index, todo in enumerate(todoList):
        print(
            index+1, "\t",
            "[*]" if todo["done"] else "[ ]",
            todo["task"]
        )

while True:
    # print Menu
    print("Menu:")
    print("1. Create Todo")
    print("2. View Todo List")
    print("3. Mark Todo as Complete")
    print("4. Delete Todo")
    print("0. Exit")

    option = input("Enter the option number: ")

    if option == "1":   # create
        todo = {"done":False, "task" :input("Enter task: ")}
        todoList.append(todo)
    elif option == "2": # Display
        display()
        pass
    elif option == "3": # Mark as Complete
        index = int(input("Enter index of completed todo: "))
        todoList[index-1]["done"] = True
        display() 
        pass
    elif option == "4": # Delete
        display()
        index = int(input("Index to delete: "))
        index -= 1
        todoList.pop (index)
        # todoList[index:index+1] = []
        pass
    elif option == "0": # exit
        break
    else:
        print("No such option")


with open ('todofile', 'w') as todofile:
    json.dump(todoList, todofile)
        
        