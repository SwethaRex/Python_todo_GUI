FILEPATH

from Functions import *
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now )
while True:
    user_action = input("Type add, show, edit, complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]+'\n'
        todos = get_todos("Files/todos.txt")

        todos.append(todo)
        write_todos("Files/todos.txt", todos)
    elif user_action.startswith('show'):
        todos = get_todos("Files/todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item}")

    elif user_action.startswith('edit'):

        try:
            number= int(user_action[5:])
            print(number)
            number = number -1
            todos = get_todos("Files/todos.txt")
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo+'\n'
            write_todos("Files/todos.txt", todos)
        except ValueError:
            print("your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos("Files/todos.txt")
            todoToRemove = todos[number-1].strip('\n')
            todos.pop(number-1)
            write_todos("Files/todos.txt", todos)
            print(f"Todo {todoToRemove} has been removed")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("You entered an invalid option")
print("Bye!")
