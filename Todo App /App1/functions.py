FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = [line.strip('\n') for line in file_local]
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    todos_string = '\n'.join(todos_arg)  # Convert the list to a single string
    with open(filepath, 'w') as file:
        file.write(todos_string)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
