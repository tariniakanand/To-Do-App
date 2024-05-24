FILEPATH='todo.txt'
def get_todos(filepath='todo.txt'):
    """" Read the text file and return the todo list """
    with open(filepath, 'r') as file_lcl:
        todos_lcl = file_lcl.readlines()
    return todos_lcl


def write_todos(todos_arg, filepath="todo.txt"):
    """" Write todos in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

