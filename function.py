FILEPATH = 'todos.txt'

def get_todo(filepath = FILEPATH):
    with open(filepath, 'r') as f:
        todos_local = f.readlines()

    return todos_local

def write_todo(todo_arg, filepath = FILEPATH):
    with open(filepath, 'w') as f:
        f.writelines(todo_arg)

