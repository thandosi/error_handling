# Thandokazi Nkohla

# Importing tkinter
from tkinter import *
from tkinter import messagebox

# creating a window
root = Tk()
root.title("Exception_handling")
root.geometry("500x350")
root.config(bg="purple")


# Creating labels

my_label1 = Label(root, text="Please enter your details", font="12",)
my_label1.place(x=150, y=5)
my_label2 = Label(root, text="Username", font="12",)
my_label2.place(x=200, y=70)
my_label3 = Label(root, text="Password", font="12",)
my_label3.place(x=200, y=135)
# Creating entries

my_entry1 = Entry(root,)
my_entry1.place(x=150, y=100)
my_entry2 = Entry(root,)
my_entry2.place(x=150, y=165)


# function to get the passwords and usernames
def login():
    username = {"thando": "084516", "Zwai": "0000", "ayoob": "9090", "sive": "9080", "tyler": "9999"}

    if username.get(my_entry1.get()):
        if username[my_entry1.get()] == my_entry2.get():
            messagebox.showinfo("feedback", "Access Granted")
            root.destroy()
            import main2
        else:
            messagebox.showerror("feedback", "Access Denied")

# Creating buttons


button_login = Button(root, text="Login", borderwidth="10", bg="Purple", font=12, command=login)
button_login.place(x=183, y=200)

root.mainloop()



