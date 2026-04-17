import os 

tasks = {}

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task, status = line.strip().split(",")
            tasks[task] = True if status == "true" else False

while True:
    print("______add ur tasks____________")
    print("1. add task")
    print("2. view tasks")
    print("3. mark task as done")
    print("4. exit")

    choice = input("enter your choice:")

    if choice == "1":
        task = input("enter ur task:")
        tasks[task] = False
        print("ur task is added successfully")

    elif choice == "2":
        if not tasks:
            print("there is no task to show")
        else:
            print("ur task list:")
            for task, status in tasks.items():
                if status:
                    print(task, "this task is done")
                else:
                    print(task, "this task are not done")
    elif choice == "3":
        task = input("enter the task u want to make it as done:")
        if task in tasks:
            tasks[task] = True
            print("ur task is marked as done")
            if status != True:
                print(task,"this tasks are not done")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task,status in tasks.items():
                file.write(tasks + " " + str(status) + "\n")
                print("thanks for using our app")
                break
    else:        print("invalid input, try again")