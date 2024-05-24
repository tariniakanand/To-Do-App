import functions
import FreeSimpleGUI as sg

label=sg.Text("Type a ToDo")
input_box=sg.InputText(tooltip="Enter ToDo", key='todo')
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos', enable_events=True, size=[45,10])
edit_btn=sg.Button("Edit")

window=sg.Window("Tari's ToDo",
                 layout=[[label, input_box, add_button],
                         [list_box, edit_btn]],
                 font=('Helvetica', 10))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            etodo=values['todos'][0]
            new_todo=values['todo']
            todos=functions.get_todos()
            index=todos.index(etodo)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(values['todos'])

        case sg.WIN_CLOSED:
            break



window.close()
