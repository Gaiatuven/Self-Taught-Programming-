from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()

    try:
        if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos()
            todos.append(todo)

            write_todos(todos)

        elif user_action.startswith("show"):

            todos = get_todos()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item}'
                print(row)

        elif user_action.startswith("edit"):
            number = int(user_action[5:]) - 1

            todos = get_todos("todos.txt")

            if 0 <= number < len(todos):
                new_todo = input("Enter new Todo: ")
                todos[number] = new_todo + '\n'
                write_todos("todos.txt", todos)
            else:
                print("Invalid index")

        elif user_action.startswith("complete"):
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            if 0 < number <= len(todos):
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                write_todos("todos.txt", todos)
                message = f'Todo {todo_to_remove} was removed from the list'
                print(message)
            else:
                print("Invalid index")

        elif user_action.startswith("exit"):
            break
        else:
            print("Command not valid")

    except ValueError:
        print("Your command is not valid")
        continue

print("Thank you and goodbye")