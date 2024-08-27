from  customtkinter  import * 
from  PIL import Image
from tkinter import ttk, messagebox
import database
##############Functionality
def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select an item to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        messagebox.showinfo("Success","Employee updated successfully")
        clear()
        treeview_data()
def delete_employee():
    database.delete(idEntry.get())
    clear()
    treeview_data()
   
def deleteall_employee():
    database.delete_all()
    clear()
    treeview_data()

def search_employee():
    if searchEntry.get=='':
        messagebox.showerror("Error","Please enter a value to search")
    elif searchBox.get()=="Search By":
        messagebox.showerror("Error","Please select a search option")

    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for row in searched_data:
            tree.insert('', 'end', values=row)
            
    


def row_selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        #print(row)
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.insert(0,row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])


def clear():
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.delete(0,END)
    genderBox.set(gender_options[0])
    salaryEntry.delete(0,END)


def treeview_data():
    tree.delete(*tree.get_children())
    employees=database.fetch_employees()
    
    for employee in employees:
        tree.insert("",END,values=employee)

def  add_employee():
    database.connect_database()
    #print(idEntry.get(),nameEntry.get(),phoneEntry.get(),salaryEntry.get())
    if idEntry.get=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()  
        



window=CTk()
window.title("Employee Managment System")
#window.resizable(False,False)
window.geometry("1100x680+100+250")
window.config(bg="#161c30")
logo=CTkImage(Image.open('bgg.png'),size=(930,158))
logolabel=CTkLabel(window,image=logo,text='' )
logolabel.grid(row=0,column=0,columnspan=2)

#######################leftframe
leftframe=CTkFrame(window,fg_color="#161c30")
leftframe.grid(row=1,column=0,padx=10,pady=10)


idLabel=CTkLabel(leftframe,text='Id ', font=('microsoft ui',18,'bold'),text_color='#fff')
idLabel.grid(row=0,column=0,padx=10,pady=10,sticky='w')
idEntry=CTkEntry(leftframe, font=('microsoft ui',15,'bold'),width=180)
idEntry.grid(row=0,column=1,padx=10,pady=10)

nameLabel=CTkLabel(leftframe,text='Name ', font=('microsoft ui',18,'bold'),text_color='#fff')
nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky='w')
nameEntry=CTkEntry(leftframe, font=('microsoft ui',15,'bold'),width=180)
nameEntry.grid(row=1,column=1,padx=10,pady=10)

phoneLabel=CTkLabel(leftframe,text='Phone No ', font=('microsoft ui',18,'bold'),text_color='#fff')
phoneLabel.grid(row=2,column=0,padx=10,pady=10,sticky='w')
phoneEntry=CTkEntry(leftframe, font=('microsoft ui',15,'bold'),width=180)
phoneEntry.grid(row=2 ,column=1,padx=10,pady=10)

roleLabel=CTkLabel(leftframe,text='Role ', font=('microsoft ui',18,'bold'),text_color='#fff')
roleLabel.grid(row=3,column=0,padx=10,pady=10,sticky='w')
role_options=['Web Developer','Data Scientist', 'Network Engineer','Devops developer','ui/ux Deginer']
roleBox=CTkEntry(leftframe, font=('microsoft ui',15,'bold'),width=180)
roleBox.grid(row=3,column=1,padx=10,pady=10)
#roleBox.set(role_options[0])

genderLabel=CTkLabel(leftframe,text='Role ', font=('microsoft ui',18,'bold'),text_color='#fff')
genderLabel.grid(row=4,column=0,padx=10,pady=10,sticky='w')
gender_options=['male','female']
genderBox=CTkComboBox(leftframe,values=gender_options,width=180, font=('microsoft ui',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1,padx=10,pady=10)
genderBox.set(gender_options[0])


salaryLabel=CTkLabel(leftframe,text='Salary ', font=('microsoft ui',18,'bold'),text_color='#fff')
salaryLabel.grid(row=5,column=0,padx=10,pady=10,sticky='w')
salaryEntry=CTkEntry(leftframe, font=('microsoft ui',15,'bold'),width=180)
salaryEntry.grid(row=5 ,column=1,padx=10,pady=10)



##############################right Frame
rightframe=CTkFrame(window,fg_color="#161c30")
rightframe.grid(row=1,column=1,padx=(10,20),pady=10)

search_options=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightframe,values=search_options, font=('microsoft ui',15,'bold'),state='readonly')
searchBox.grid(row=0,column=0,padx=5,pady=5)
searchBox.set(search_options[0])

searchEntry=CTkEntry(rightframe, font=('microsoft ui',15,'bold'))
searchEntry.grid(row=0 ,column=1,padx=5,pady=5)

searchButton=CTkButton(rightframe,text='Search', font=('microsoft ui',15,'bold'),width=100,command=search_employee)
searchButton.grid(row=0 ,column=2,padx=5,pady=5)

searchButton=CTkButton(rightframe,text='Show All', font=('microsoft ui',15,'bold'),width=100)
searchButton.grid(row=0 ,column=3,padx=5,pady=5)

tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('Id',anchor=CENTER,width=80)
tree.column('Name',anchor=CENTER,width=160)
tree.column('Phone',anchor=CENTER,width=160)
tree.column('Role',anchor=CENTER,width=160)
tree.column('Gender',anchor=CENTER,width=80)
tree.column('Salary',anchor=CENTER,width=100)
style=ttk.Style()



style.configure('Treeview.Heading',font=('Arial',14,'bold'))
style.configure('Treeview',font=('arial',11),rowheight=30,background='#161C30',foreground='#fff')


scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
tree.config(yscrollcommand=scrollbar.set)


####################################
buttonFrame=CTkFrame(window,fg_color="#161c30")
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),corner_radius=15,width=160)
newButton.grid(row=0,column=0,padx=5,pady=5)


newButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),corner_radius=15,width=160,command=add_employee)
newButton.grid(row=0,column=1,padx=5,pady=5)


updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),corner_radius=15,width=160,command=update_employee)
updateButton.grid(row=0,column=2,padx=5,pady=5)


deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),corner_radius=15,width=160,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=5,pady=5)


deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),corner_radius=15,width=160 ,command=deleteall_employee)
deleteallButton.grid(row=0,column=4,padx=5,pady=5)


tree.bind('<Double-Button-1>',row_selection)

treeview_data()
window.mainloop()
