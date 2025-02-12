import  functions
import FreeSimpleGUI as fg

label = fg.Text("Type a to-do")
text_box = fg.InputText(tooltip="Please input a todo")
add_button = fg.Button("Add")

window = fg.Window("To do app",layout=[[label],[text_box,add_button]])
window.read()
window.close()