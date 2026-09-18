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
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file: #file will close by this method
                todos = file.readlines() # r reads the file

            todos.append(todo)

            with open('todos.txt','w') as file: #w means writing the file. Can also use 'a' which
            # appends the content without it being deleted

                # storing items in a txt file
                todos = file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n') #this removes the \n from the string
                row = f"{index + 1} - {item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Which item you completed?: "))
            todos.pop(number - 1)
            print("Item has been removed.")
        case "exit":
            break
print("Bye!")