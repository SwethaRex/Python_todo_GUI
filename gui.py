import FreeSimpleGUI as sg

label =sg.Text("Enter a To-do")
intput_box = sg.InputText(tooltip="Enter todo")
button =sg.Button("Add")

window = sg.Window("My to-do App", [[label, intput_box],[button]])
window.read()
window.close()