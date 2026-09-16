import json
from datetime import datetime


def load_file():
    with open("tasklist.json",'r',encoding='utf-8')as file:
        tasklist=json.load(file)
        
        return tasklist
    
def save_file(tasklist):
    with open("tasklist.json",'w',encoding='utf-8')as file:
      json.dump(tasklist,file,indent=4,ensure_ascii=False)

def show_actions():
    print("You are in main menu, choose your action :")
    print("  1. show task list ")
    print("  2. add a task ")
    print("  3. delete a task ")
    print("  4. mark a task as completed ")
    print("  0. exit the program ")


def show_tasks():
    tasks=load_file()
    if not tasks:
        print("you don't have any tasks yet ")
        return
    else:
        print("task list:")
        counter = 1
        for task in tasks:
            title=task['title']
            description=task["description"]
            if not description:
                description="no description"
            dead_line=task["dead_line"]
            if dead_line=="None":
                dead_line='no deadline'
            created_at=task["created_at"]
            is_done=task["is_done"]
            if is_done:
                is_done="✅"
            else:
                is_done="❌"
            print(f"{counter}. {is_done} {title} \n   description: {description}\n   deadline: {dead_line}\n   created at: {created_at}")
            counter += 1


def add_task():
    tasks=load_file()
    title = input("enter the task name :")
    description=input('enter the task description (optional):')
    while True:
        dead_line=input('enter the task deadline in format YYYY-MM-DD (optional):')
        if dead_line=="":
            dead_line=None
            break
        try:
            dead_line=datetime.strptime(dead_line,'%Y-%m-%d').date()
            break
        except ValueError:
            print("wrong date format,must be YYYY-MM-DD ")
    tasks.append({
        'title':title,
        'description':description,
        'dead_line':str(dead_line),
        'is_done':False,
        'created_at':str(datetime.now().date())
    })
    save_file(tasks)
    print(f'task "{title}" was successfully added to the task list')


def deleted_task():
    tasks=load_file()
    show_tasks()
    number = int(input("enter the number of the task you want to delete:"))
    if number<=0 or number>len(tasks):
        print("no task with this number")
        return
    tasks.pop(number - 1)
    save_file(tasks)
    print("task deleted ")


def mark_task():
    tasks=load_file()
    show_tasks()
    number = int(input("enter the number of the task you want to mark: "))
    if number<=0 or number>len(tasks):
        print("no task with this number")
        return
    tasks[number - 1]["is_done"]= not tasks[number - 1]["is_done"]
    save_file(tasks)
    print("task marked")

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
        mark_task()
