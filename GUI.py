from tkinter import *
App = Tk()
App.title("Telephone-book Application")
App.geometry("640x240")

ViewAll = Button(App, text = "View All")
ViewAll.grid(row = 0, column = 2)

Update = Button(App, text = "Update")
Update.grid(row = 0, column = 1)

ID = Label(App, text ="ID")
ID.grid(row = 1, column = 0)
ID_text = Text(App, height = 1, width = 20)
ID_text.grid(row = 1, column = 1)

Name = Label(App, text = "Name")
Name.grid(row = 2, column = 0)
Name_text = Text(App, height = 1, width = 20)
Name_text.grid(row = 2, column = 1)

TelNumber = Label(App, text = "Tel Number")
TelNumber.grid(row = 3, column = 0)
TelNumber_text = Text(App, height = 1, width = 20)
TelNumber_text.grid(row = 3, column = 1)

LineID = Label(App, text = "Line ID")
LineID.grid(row = 4, column = 0)
LineID_text = Text(App, height = 1, width = 20)
LineID_text.grid(row = 4, column = 1)

Email = Label(App, text = "Email")
Email.grid(row = 5, column = 0)
Email_text = Text(App, height = 1, width = 20)
Email_text.grid(row = 5, column = 1)

List = Listbox(App, height = 10, width = 40)
List.grid(row = 1, column = 2, rowspan = 5, padx = 20, pady = 7)

Scrl = Scrollbar(App)
Scrl.grid(row = 1, column = 5, rowspan = 5)

List.configure(yscrollcommand = Scrl.set)
Scrl.configure(command = List.yview)

App.mainloop()
