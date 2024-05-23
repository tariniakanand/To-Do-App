import functions
import time

txt="""
Welcome to Tari's Todo Manager!
Lets get productive together!!
"""
print(txt)

now=time.strftime("%b %d, %y, %H:%M:%S")
print("It is", now, '\n')

while True:
    user_action = input("Enter add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todo=todo.title()

        todos=functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos=functions.get_todos()

        for index, item in enumerate(todos):
            item = item.title()
            item=item.strip('\n')
            print(f"{index + 1}.{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos=functions.get_todos()

            todos[number] = input("Enter the todo: ") + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid Command")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos=functions.get_todos()

            todo_rem=todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos)

            msg=f"The todo {todo_rem} was removed from the list"
            print(msg)

        except IndexError:
            print("There is no task with that number")
            continue

        except ValueError:
            print("Enter the number of todo to complete after the command")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Command Invalid")

print("\nHave a nice Day!")