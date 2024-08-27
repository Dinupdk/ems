from customtkinter import * 
from tkinter import *
from tkinter import messagebox

from  PIL import Image


###############Functionality
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Dinesh' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login Successful')
        root.destroy()
        import ems as ems
    else:
        messagebox.showerror('Error','Invalid Username or Password')
    pass

root=CTk()
root.geometry("940x640")
root.resizable(0,0)
root.title("Login Page")
imagee=CTkImage(Image.open('login.jpg'),size=(930,620))
imagelabel=CTkLabel(root,image=imagee,text=' ')
imagelabel.place(x=5,y=10)

li=CTkLabel(root,text="____________________",bg_color="#dbdbdb",text_color='black',font=('Goudy Old Style',28,'bold'))
li.place(x=340,y=95)
hdd=CTkLabel(root,text='Employee Managment System',bg_color="#dbdbdb",text_color='black',font=('Goudy Old Style',20,'bold'))
hdd.place(x=360,y=90)


usernameEntry=CTkEntry(root,placeholder_text='Enter Your UserName',width=250,bg_color="#dbdbdb",text_color='black',fg_color="#dbdbdb",border_width=1,border_color='dodgerblue3',font=('microsoft ui',18))
usernameEntry.place(x=360,y=150)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=250,bg_color="#dbdbdb",text_color='black',fg_color="#dbdbdb",border_width=1,border_color='dodgerblue3',font=('microsoft ui',18),show='*')
passwordEntry.place(x=360,y=190)

loginButton=CTkButton(root,text='Login',cursor='hand2',text_color='#000000',font=('Goudy Old Style',20,'bold'),command=login)
loginButton.place(x=390,y=230)


root.mainloop()