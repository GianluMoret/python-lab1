print("Todo_Manager")
init = 0
list=[]
while init!=10:
    print("1. Insert a new task (a string of text);")
    print("2. Remove a task (by typing its content, exactly);")
    print("3. Show all the existing task;")
    print("4. Close the program")
    print("")
    print("Your choice:")
    choice=input()
    if int(choice) == 1:
        print("Enter the new task:")
        list.append(input())
        print("Task inserted.")
    elif int(choice) == 2:
        print("Enter the name of the task you want to remove:")
        string=input()
        list.remove(string)
    elif int(choice) == 3:
        print("These are all the task:")
        i = 0
        while i < len(list):
            print("-"+list[i])
            i=i+1
        print("End of the printing")
    else:
        print("closing the program")
        init=10
    print("")