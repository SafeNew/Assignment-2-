from tkinter import *
App = Tk()
App.title("Telephone-book Application")
App.geometry("1300x240")

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
ID_text_box = Entry(App, width = 20, textvariable = ID_text)
ID_text_box.grid(row = 1, column = 1, columnspan = 2)

Name = Label(App, text = "Name")
Name.grid(row = 2, column = 0)
Name_text = StringVar()
Name_text_box = Entry(App, width = 20, textvariable = Name_text)
Name_text_box.grid(row = 2, column = 1, columnspan = 2)

TelNumber = Label(App, text = "Tel Number")
TelNumber.grid(row = 3, column = 0)
TelNumber_text = StringVar()
TelNumber_text_box = Entry(App, width = 20, textvariable = TelNumber_text)
TelNumber_text_box.grid(row = 3, column = 1, columnspan = 2)

LineID = Label(App, text = "Line ID")
LineID.grid(row = 4, column = 0)
LineID_text = StringVar()
LineID_text_box = Entry(App, width = 20, textvariable =LineID_text)
LineID_text_box.grid(row = 4, column = 1, columnspan = 2)

Email = Label(App, text = "Email")
Email.grid(row = 5, column = 0)
Email_text = StringVar()
Email_text_box = Entry(App, width = 20, textvariable = Email_text)
Email_text_box.grid(row = 5, column = 1, columnspan = 2)

List = Listbox(App, height = 10, width = 160)
List.grid(row = 1, column = 3, rowspan = 5, columnspan = 20, padx = 20, pady = 7)

Scrl = Scrollbar(App)
Scrl.grid(row = 1, column = 23, rowspan = 5, columnspan = 2)

List.configure(yscrollcommand = Scrl.set)
Scrl.configure(command = List.yview)
#List.bind('<<ListBoxSelect>>', get_select_row)

App.mainloop()
