import  functions
import FreeSimpleGUI as fg

label = fg.Text("Type a to-do")
text_box = fg.InputText(tooltip="Please input a todo", key= 'todo')
add_button = fg.Button("Add")
list_box = fg.Listbox(values=functions.get_todos(),key='todo_box',
                      enable_events=True, size=[44,10])
edit_button = fg.Button("Edit")
complete_button = fg.Button("Complete")
exit_button = fg.Button("Exit")

window = fg.Window("To do app",
                   layout=[[label],[text_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',12))
while True:
    event , value = window.read()
    print(event,value)
    print (event)
    print(value)
    # print(value['todo_box'])
    match event:
        case 'Add':
            todo_list = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todo_list.append(new_todo)
            functions.write_todo(todo_list)
            window['todo_box'].update(values=todo_list)
            window['todo'].update(value='')
        case 'Edit':
            todo_to_edit = value['todo_box'][0]
            new_todo = value['todo']+'\n'
            todo_list = functions.get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.write_todo(todo_list)
            window['todo_box'].update(values=todo_list)
            window['todo'].update(value='')
        case 'Complete':
            todo_to_complete = value['todo_box'][0]
            todo_list = functions.get_todos()
            todo_list.remove(todo_to_complete)
            functions.write_todo(todo_list)
            window['todo_box'].update(values=todo_list)
            window['todo'].update(value='')
        case 'Exit':
            break

        case 'todo_box':
            window['todo'].update(value=value['todo_box'][0].strip('\n'))

        case fg.WIN_CLOSED:
            break

window.close()