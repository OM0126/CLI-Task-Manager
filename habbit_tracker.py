import os 

tasks = {}


if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            task, status = line.strip().split(",")
            if status == "true":
                tasks[task] = True
            else:
                tasks[task] = False

while True:
    print("---____ ADD YOUR TASKS___----")
    print("1. add task")
    print("2. view tasks")
    print("3. mark task as done")
    print("4. exit")

    choice = input("enter ur choice: ")

    if choice == "1":
        task = input("enter your task: ")
        tasks[task] = False
        print("task added")

    elif choice == "2":
        if not tasks:
            print("no tasks")
        else:
            for task, status in tasks.items():
                if status == True:
                    print(task, "- done")
                else:
                    print(task, "- not done")

    elif choice == "3":
        task = input("enter task name: ")
        if task in tasks:
            tasks[task] = True
            print("marked as done")
        else:
            print("task not found")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task, status in tasks.items():
                file.write(task + "," + str(status).lower() + "\n")

        print("thanks")
        break

    else:
        print("invalid input")
