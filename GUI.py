from tkinter import *
from tkinter import messagebox 
#Back-End
import json
profile = json.load(open("profile.json", "r"))
def ViewAllCommand():
    List.delete(0, END)
    for i in profile.keys():
        List.insert(END, profile[i])
def SearchCommand():
    name_text = Search_text_box.get()
    notFound = True
    for i in profile.keys():
        if name_text == "":
            messagebox.showerror(title="No Text Enter", message="Please Enter Text")
            break
        elif name_text == profile[i]["NAME"][:len(name_text)]:
            List.delete(0, END)
            List.insert(END, profile[i])
            notFound = False
        if notFound and i == "p4":
            List.delete(0, END)
            messagebox.showerror(title="", message="Not found")
def get_selected_row(event):
    global selected_tuple
    Index = List.curselection()[0]
    selected_tuple = List.get(Index)
    print(selected_tuple)
    return(selected_tuple)
#Front End
App = Tk()
App.title("Telephone-book Application")
App.geometry("620x240")

ViewAll = Button(App, text = "View All", command = ViewAllCommand)
ViewAll.grid(row = 0, column = 2)

Update = Button(App, text = "Update")
Update.grid(row = 0, column = 1)

Search = Button(App, text = "Search", command = SearchCommand)
Search.grid(row = 0, column = 3)
Search_text= StringVar()
Search_text_box = Entry(App, width = 30, textvariable = Search_text)
Search_text_box.grid(row = 0, column = 4)

ID = Label(App, text ="ID")
ID.grid(row = 1, column = 0)
ID_text = StringVar()
ID_text_box = Entry(App, width = 30, textvariable = ID_text)
ID_text_box.grid(row = 1, column = 1, columnspan = 2)

Name = Label(App, text = "Name")
Name.grid(row = 2, column = 0)
Name_text = StringVar()
Name_text_box = Entry(App, width = 30, textvariable = Name_text)
Name_text_box.grid(row = 2, column = 1, columnspan = 2)

TelNumber = Label(App, text = "Tel Number")
TelNumber.grid(row = 3, column = 0)
TelNumber_text = StringVar()
TelNumber_text_box = Entry(App, width = 30, textvariable = TelNumber_text)
TelNumber_text_box.grid(row = 3, column = 1, columnspan = 2)

LineID = Label(App, text = "Line ID")
LineID.grid(row = 4, column = 0)
LineID_text = StringVar()
LineID_text_box = Entry(App, width = 30, textvariable =LineID_text)
LineID_text_box.grid(row = 4, column = 1, columnspan = 2)

Email = Label(App, text = "Email")
Email.grid(row = 5, column = 0)
Email_text = StringVar()
Email_text_box = Entry(App, width = 30, textvariable = Email_text)
Email_text_box.grid(row = 5, column = 1, columnspan = 2)

List = Listbox(App, height = 10, width = 50)
List.grid(row = 1, column = 3, rowspan = 5, columnspan = 3, padx = 20, pady = 7)

Scrly = Scrollbar(App, orient = VERTICAL, command = List.yview)
Scrly.grid(row = 1, column = 23, rowspan = 5, columnspan = 2)

Scrlx = Scrollbar(App, orient = HORIZONTAL, command = List.xview)
Scrlx.grid (row = 6, column = 3, columnspan = 3)

List.configure(yscrollcommand = Scrly.set)
List.configure(xscrollcommand = Scrlx.set)
List.bind('<<ListboxSelect>>', get_selected_row)

App.mainloop()
