import  functions
import FreeSimpleGUI as fg

label = fg.Text("Type a to-do")
text_box = fg.InputText(tooltip="Please input a todo", key= 'todo')
add_button = fg.Button("Add")

window = fg.Window("To do app",
                   layout=[[label],[text_box,add_button]],
                   font=('Times New Roman',20))
while True:
    event , value = window.read()
    print (event)
    print(value)
    match event:
        case 'Add':
            todo_list = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todo_list.append(new_todo)
            functions.write_todo(todo_list)
        case fg.WIN_CLOSED:
            break

window.close()