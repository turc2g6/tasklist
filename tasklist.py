tasks = ["сходить в магазин", "помыть полы", "прибраться в комнате"]


def show_actions():
    print("Вы находитесь в главном меню, выбeрите действие :")
    print("  1. показать список задач ")
    print("  2. добавить задачу ")
    print("  3. удалить задачу ")
    print("  4. отметить задачу выполненной ")
    print("  0. выйти из программы ")


def show_tasks():
    if not tasks:
        print("у вас пока нет задач ")
        return
    else:
        print("список задач:")
        counter = 1
        for task in tasks:
            print(f"{counter}. {task}")
            counter += 1


def add_task():
    title = input("введите название задачи :")
    tasks.append(title)
    print(f'задача "{title}" успешно добавлена в список задач ')


def deleted_task():
    show_tasks()
    number = int(input("введите номер удаляемой задачи:"))
    tasks.pop(number - 1)
    print("задача удалена ")


def check_task():
    show_tasks()
    number = int(input("Введите отмечаемую задачу: "))
    if "✅" in tasks[number - 1]:
        tasks[number - 1] = tasks[number - 1][:-1]
    else:
        tasks[number - 1] = tasks[number - 1] + "✅"


while True:
    show_actions()
    command = int(input("введите номер команды :"))
    if command == 0:
        print("программа остановлена")
        break
    elif command == 1:
        show_tasks()
    elif command == 2:
        add_task()
    elif command == 3:
        deleted_task()
    elif command == 4:
        check_task()
