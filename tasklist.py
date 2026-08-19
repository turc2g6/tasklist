tasks = []


def show_actions():
    print("You are in main menu, choose your action :")
    print("  1. show task list ")
    print("  2. add a task ")
    print("  3. delete a task ")
    print("  4. mark a task as completed ")
    print("  0. exit the program ")


def show_tasks():
    if not tasks:
        print("you don't have any tasks yet ")
        return
    else:
        print("task list:")
        counter = 1
        for task in tasks:
            print(f"{counter}. {task}")
            counter += 1


def add_task():
    title = input("enter the task name :")
    tasks.append(title)
    print(f'task "{title}" was successfully added to the task list')


def deleted_task():
    show_tasks()
    number = int(input("enter the number of the task you want to delete:"))
    tasks.pop(number - 1)
    print("task deleted ")


def check_task():
    show_tasks()
    number = int(input("enter the number of the task you want to mark: "))
    if "✅" in tasks[number - 1]:
        tasks[number - 1] = tasks[number - 1][:-1]
    else:
        tasks[number - 1] = tasks[number - 1] + "✅"


while True:
    show_actions()
    command = int(input("enter the command number :"))
    if command == 0:
        print("program stopped")
        break
    elif command == 1:
        show_tasks()
    elif command == 2:
        add_task()
    elif command == 3:
        deleted_task()
    elif command == 4:
        check_task()
