import functions
import FreeSimpleGUI as sg
import time

sg.theme("LightBlue2")

clock=sg.Text("", key='clock')
label=sg.Text("Type a ToDo")
input_box=sg.InputText(tooltip="Enter ToDo", key='todo')
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos', enable_events=True, size=[45,10])
edit_btn=sg.Button("Edit")
cmpt_btn=sg.Button("Complete")
exit_btn=sg.Button("Exit")

window=sg.Window("Tari's ToDo",
                 layout=[[clock],
                         [label, input_box, add_button],
                         [list_box, edit_btn, cmpt_btn],
                         [exit_btn]],
                 font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                etodo=values['todos'][0]
                new_todo=values['todo']
                todos=functions.get_todos()
                index=todos.index(etodo)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an Item first", font=("Helvetica", 10))
        case 'todos':
            window['todo'].update(values['todos'])
        case "Complete":
            try:
                ctodo=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(ctodo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(values='')
            except IndexError:
                sg.Popup("Please select an Item first", font=("Helvetica", 10))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
