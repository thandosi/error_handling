from tkinter import *
from tkinter import messagebox

# creating window


root = Tk()
root.title("Exception_handling")
root.geometry("500x350")
root.config(bg="purple")


my_label1 = Label(root, text="Please enter Amount in your account", font="12",)
my_label1.place(x=50, y=5)
my_entry1 = Entry(root,)
my_entry1.place(x=50, y=40)


# Error handling function
def check():
    funds = my_entry1.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("Feedback", "Please deposit more funds for this excursion.")
        else:
            messagebox.showinfo("Feedback", "Congratulations. You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Feedback", "Error,Please insert a number.")

# Creating a btn


button_verify = Button(root, text="Check qualification", borderwidth="5", bg="Purple", font=12, command=check)
button_verify.place(x=50, y=70)


def close():
    root.destroy()


exit_btn = Button(root, text="Close", bg="purple", fg="black", borderwidth="3", command=close)
exit_btn.place(x=90, y=150)


def clear():
    my_entry1.delete(0, END)


clear_btn = Button(root, text="clear", bg="purple", fg="black", borderwidth="3", command=clear)
clear_btn.place(x=200, y=150)

root.mainloop()
