def get_todos(filepath):
    with open(filepath, "r") as readfile:
        readtodos = readfile.readlines()
    return readtodos

def write_todos(filepath, todo_args):
    with open(filepath, 'w') as writefile:
        writefile.writelines(todo_args)
