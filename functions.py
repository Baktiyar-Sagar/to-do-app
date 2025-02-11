FILEPATH = "files/todo.txt"
def get_todos(filepath=FILEPATH):
    """Read a txt file and return to-do items in the list"""
    with open(filepath, 'r') as file_local:
      todo_list_local = file_local.readlines()  # Reading every line in the text file and store all the available values it into a list variable name "todo_list"
      return todo_list_local

def write_todo(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:  # writing the file
        todolist_local = file_local.writelines(todo_arg)  # writing or storing all the value of the todo_list (list) variable in to todo.txt file
        return todolist_local

def print_list(todo_list_local):
    for index_local, todo_local in enumerate(todo_list_local):
        print(f"No {index_local + 1} item: {todo_local.strip("\n").title()}")

print("Outside the __main__ :"+__name__)

if __name__ == "__main__":
    print("inside the __name__ in functions")
    print(get_todos())