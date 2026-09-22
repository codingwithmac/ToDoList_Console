 # Use f-strings to format the output exactly the way we want it — no
# unwanted spaces.
#
# An f-string is a string literal prefixed with `f`. Inside the string,
# anything inside `{ ... }` is replaced with the value of the expression.
# You can put any variable or expression in those curly brackets, and
# mix in literal text outside them.
#
# Example (in the Python console):
#   >>> index, item = 1, "throw"
#   >>> row = f"{index} - {item}"
#   >>> row
#   '1 - throw'


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] #list slice operation this will only give the string starting on the index number mentioned
        if user_action.strip():
            print("Todo cannot be empty.")
            continue
        with open('todos.txt', 'r') as file: #file will close by this method
            todos = file.readlines() # r reads the file

        todos.append(todo + '\n')

        with open('todos.txt','w') as file: #w means writing the file. Can also use 'a' which
        # appends the content without it being deleted
            # storing items in a txt file
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n') #this removes the \n from the string
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input(f"Editing '{number + 1} - {todos[number].strip()}' -> Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)
            message = f"Todo '{todo_to_remove}' has been removed from list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    else:
        print("Command is not valid!")

print("Bye!")