FILEPATH = "App_1/todos.txt" #revert to todos.txt when uploading web app

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return
    a list of todo items

    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the todo items list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg) 