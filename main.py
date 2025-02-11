# from functions import get_todos,write_todo, print_list
import functions
import time

now = time.strftime(" %d %b,%Y ; Time:%H:%M:%S")
print("It is:", now)
while True :
    user_action = input("\ntodo list: 1.Add , 2.Show , 3.Edit, 4.Complete, 5.Exit :")
    user_action = user_action.strip().lower()  # strip() will ignore the space and will not consider space as a string

    if  user_action.startswith("add") :
        todo_list = functions.get_todos()
        todo = user_action[int(len('add')+1):]+'\n'  # Taking input for add to-do in the list
        todo_list.append(todo)    # adding all the to-do in to a list variable name todo_list
        functions.write_todo(todo_list)  # Calling function: file writing (customized) function

    elif  user_action.startswith("show") :
        todo_list = functions.get_todos()
            # Using list comprehension
        # new_todo =[todo.strip("\n") for todo in todo_list]
        # for index, todo in enumerate(new_todo):
        #     todo= todo.title() # stripe is for
        #     print(f"No {index+1} item: {todo} ")
        functions.print_list(todo_list) # Calling faction: to-do list printing (customized) function

    elif user_action.startswith("edit") :
        try:
            todo_list = functions.get_todos()  # Calling function: file opening (customized) function
            for index, todo in enumerate(todo_list):
                print(f"No {index + 1} item: {todo.strip("\n").title()} ")
            index_todo = int(user_action[int(len("edit") + 1):])

            todo_list[index_todo-1] = input("Enter New todo:")+ '\n'

            functions.write_todo(todo_list)  # Calling function: file writing (customized) function

            print("\nNew todo list is Updated !!!!!\n")

            print("---------New List of Todo_____________")
            functions.print_list(todo_list) # Calling faction: to-do list printing (customized) function
        except IndexError:
            print("\nThis is an invalid command !! Their is no item with that number")
            continue


        except ValueError:
            print("\nThis is an invalid command !! There should a number ")
            continue

    elif user_action.startswith("complete") :
        try:
            todo_list = functions.get_todos()  # Calling function: file opening (customized) function

            if not todo_list:
                print("\nThere is no todo list !!!")
            else:
               number=int( user_action[int(len('complete')+1):])
               index = number-1
               completed_todo = todo_list[index].strip('\n')
               todo_list.pop(index)
               message= f"\nTO-DO:{completed_todo} is completed"
               print(message)
               functions.write_todo(todo_list)  # Calling function: file writing (customized) function

            print(f"\n!!! Upgraded list after completion of a todo !!!!")
            todo_list = functions.get_todos()  # Calling faction: file opening (customized) function
            functions.print_list(todo_list)   # Calling faction: to-do list printing (customized) function

        except IndexError:
            print("\nThis is an invalid command !! Their is no item with that number")
            continue
        except ValueError:
            print("\nThis is an invalid command !! There should a number ")
            continue

    elif user_action.startswith("exit") :
        break

    else :
        print(" !!!!!! This command doesnt exist !!!!!!!")