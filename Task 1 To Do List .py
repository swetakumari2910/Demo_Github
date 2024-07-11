import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Eroor', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values(?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end',task)

def delete_tasks():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Tasks selected.cannot Deleted.')

def delete_all_tasks():
    messaage_box = messagebox.askyesno('Delete ALL','Are you sure?')
    if message_box == True:
        while(len(task) !=0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def vclose():
    print(tasks)
    guiwindow.destroy()

def retrieve_datase():
    while(len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiwindow = tk.Tk()
    guiwindow.title("To-Do List Manager - ARUN")
    guiwindow.geometry("500x450+750+250")
    guiwindow.resizable(0,0)
    guiwindow.configure(bg = "#FAE8D7")

    the_connection = sql.connect('listofTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')


    tasks = []

    header_frame = tk.Frame(guiwindow,bg = "dark orange")
    functions_frame = tk.Frame(guiwindow, bg = "dark orange")
    listbox_frame = tk.Frame(guiwindow, bg = "dark orange")

    header_frame.pack(fill = "both")
    functions_frame.pack(side = "left", expand = True, fill = "both")
    listbox_frame.pack(side = "left", expand = True, fill = "both")

    header_label = ttk.Label(
        header_frame,
        text = "To-Do list",
        font = ("Alice", "30", "bold"),
        background = "dark orange",
        foreground = "#FFFFFF"
    )
    header_label.pack(padx = 10, pady = 10)

    task_label = ttk.Label(
        functions_frame,
        text = "Enter the Task:",
        font = ("Alice", "11", "bold"),
        background = "dark orange",
        foreground = "#FFFFFF"
    )
    task_label.place(x = 30, y = 40)

    task_field = ttk.Entry(
        functions_frame,
        font = ("Consolas", "12"),
        width = 18,
        background = "dark orange",
        foreground = "#A52A2A"
    ) 
    task_field.place(x = 30, y = 80)

    add_button = ttk.Button(
        functions_frame,
        text = "Add Task",
        width = 24,
        command = add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text = "Delete Task",
        width = 24,
        command = delete_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text = "Exit",
        width = 24,
        command = vclose
    )
    add_button.place(x = 30, y = 120)
    del_button.place(x = 30, y = 160)
    exit_button.place(x = 30, y = 200)

    task_listbox = tk.Listbox(
        listbox_frame,
        width = 26,
        height = 13,
        selectmode = 'SINGLE',
        background = "#FFFFFF",
        foreground = "#000000",
        selectbackground = "#cd853f",
        selectforeground = "#FFFFFF"
    )
    task_listbox.place(x = 10, y = 20)

    retrieve_datase()
    list_update()
    guiwindow.mainloop()
    the_connection.commit()
    the_cursor.close()


            
