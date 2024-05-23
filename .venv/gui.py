import functions
import FreeSimpleGUI as sg

label=sg.Text("Type a ToDo")
input_box=sg.InputText(tooltip="Enter ToDo")
add_button=sg.Button("Add")
window=sg.Window("Tari's ToDo", layout=[[label], [input_box, add_button]])
window.read()
window.close()
