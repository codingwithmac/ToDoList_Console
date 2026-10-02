import functions

import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add") #Button("Add") is the instance of the sg object
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]], #these are rows
                   font=("Helvetica", 18))

while True:

    event, values = window.read(timeout=200) #adding timeout makes loop run every 10 milliseconds
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print("1- Event", event)
    #print("2 - Values", values)
    #print(3, values['todos'])
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_edit = values['todos'][0] #this gives 'only' the string
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case sg.WIN_CLOSED:
            break

        case "Exit":
            break
window.close()