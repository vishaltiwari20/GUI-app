from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Login Page')
root.iconbitmap('favicon.ico')
root.geometry('400x500')
root.configure(background='#0096DC')

img = Image.open('flipkart-logo.png')
resized_img = img.resize((75,75))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(15,10))

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text='Enter your email : ', fg='white', bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))

email_entry = Entry(root, width=50)
email_entry.pack(ipady=6,pady=(1,14))

password_label = Label(root, text='Enter your password : ', fg='white', bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',14))

password_entry = Entry(root, width=50)
password_entry.pack(ipady=6,pady=(1,14))

def handle_login():
    email = email_entry.get()
    password = password_entry.get()
    # print(f"Your email is {email} and your password is {password}")
    if email == 'vishaltiwari1820@gmail.com' and password == 'vishal@123':
        messagebox.showinfo('Thanks', 'Login Sucessfull')
    else:
        messagebox.showinfo('Error', 'Login Error')

login_btn = Button(root, text='Sign in', fg='white', bg='#f58311', width=20, height=2, command=handle_login)
login_btn.pack(pady=(40,30))
login_btn.config(font=('verdana', 13))

root.mainloop()