from time import strftime

import  functions
import time
import FreeSimpleGUI as fg

fg.theme("Black")
clock = fg.Text('',key='clock')
label = fg.Text("Type a to-do")
text_box = fg.InputText(tooltip="Please input a todo", key= 'todo')
add_button = fg.Button("Add",size=10)
list_box = fg.Listbox(values=functions.get_todos(),key='todo_box',
                      enable_events=True, size=[44,10])
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")
exit_button = fg.Button("Exit",size=10)

window = fg.Window("To do app",
                   layout=[ [clock],
                           [label],[text_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',12))
while True:
    event , value = window.read(timeout=200)

    window['clock'].update(value=time.strftime("%b %d, %Y | %H:%M:%S"))
    match event:
        case 'Add':
            todo_list = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todo_list.append(new_todo)
            functions.write_todo(todo_list)
            window['todo_box'].update(values=todo_list)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = value['todo_box'][0]
                new_todo = value['todo']+'\n'
                todo_list = functions.get_todos()
                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo
                functions.write_todo(todo_list)
                window['todo_box'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                fg.popup("Please select an to-do before clicking Edit",title='Error',font='10',text_color='Brown',button_justification='centered')
        case 'Complete':
            try:
                todo_to_complete = value['todo_box'][0]
                todo_list = functions.get_todos()
                todo_list.remove(todo_to_complete)
                functions.write_todo(todo_list)
                window['todo_box'].update(values=todo_list)
                window['todo'].update(value='')
            except IndexError:
                fg.popup("Please select an to-do before clicking Complete",title='Error',font='10',text_color='Brown',button_justification='centered')
        case 'Exit':
            break

        case 'todo_box':
            window['todo'].update(value=value['todo_box'][0].strip('\n'))

        case fg.WIN_CLOSED:
            break

window.close()