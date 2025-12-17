FILEPATH = "Files/todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as readfile:
        readtodos = readfile.readlines()
    return readtodos

def write_todos(todo_args, filepath=FILEPATH):
    with open(filepath, 'w') as writefile:
        writefile.writelines(todo_args)
