import PySimpleGUI as sg 

def add_item():
    item = values["add_item"]
    tasks.append(item)
    window.FindElement('items').update(values=tasks)
    window.FindElement('add_item').update('')

def delete_item():
    delete_val= values['item'][0]
    tasks.remove(delete_val)
    window.FindElement("items").update(values=tasks)


tasks=[]
layout=[
    [sg.InputText("",size=(40,1),font=("Arial",18),key="add_item"),
    sg.Button("ADD",font=("Arial",18),key='add_save')],
    [sg.Listbox(values="",size=(40,10),font=("Arial",18),key="items"),
    sg.Button("DELETE",key='delete'),
    sg.Button("EDIT",key='edit')]
]

window=sg.Window("Todolist",layout)


while True: #hi
    event,values=window.Read()
    if event==sg.WINDOW_CLOSED:
        break
    if event=='add_save':
        add_item()
    elif event =='delete':
        delete_item()