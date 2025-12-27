import FreeSimpleGUI as sg
from time import strftime

import Functions

label_clock =sg.Text(key ='clock')
label = sg.Text("Enter a To-do")
intput_box = sg.InputText(key="todo", tooltip="Enter a todo")
button = sg.Button("Add")
list_box = sg.Listbox(values=Functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

sg.theme("DarkPurple")
window = sg.Window("My to-do App",
                   [[label_clock],[label],
                    [intput_box,button],
                   [list_box, edit_button, complete_button],
                   [exit_button]],
                   font=("Helvetica", 18))

while True:
    event, values = window.read(timeout=200)
    # window["clock"].update(value=strftime("%b %d %Y %H:%M:%S"))
    match event:
        case "Add":
            try:
                todos = Functions.get_todos()
                new_todo = values["todo"] +'\n'
                todos.append(new_todo)
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an Item first", font=("Helvetica", 18))
        case "Edit":
            try:
                new_todo=values['todo'] + '\n'
                todo_to_edit=values['todos'][0]
                todos=Functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                print("g")
                # sg.popup("Please select an Item first", font=("Helvetica", 18))
        case "Complete":
            todo_to_complete=values['todos'][0]
            todos=Functions.get_todos()
            todos.remove(todo_to_complete)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "todos":
            print(values)
            window["todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED | "Exit":
            break


window.close()