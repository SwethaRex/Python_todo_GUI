import FreeSimpleGUI as sg

import Functions

label =sg.Text("Enter a To-do")
intput_box = sg.InputText(key="todo", tooltip="Enter todo")
button =sg.Button("Add")

window = sg.Window("My to-do App",
                   [[label, intput_box],[button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values["todo"] +'\n'
            Functions.write_todos(new_todo)
        case sg.WIN_CLOSED:
            break


window.close()