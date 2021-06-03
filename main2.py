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
            messagebox.showerror("feedback", "Please deposit more funds for this excursion.")
        else:
            messagebox.showinfo("feedback", "Congratulations. You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("feedback", "Error,Please insert a number.")

# Creating a btn


button_verify = Button(root, text="Check qualification", borderwidth="5", bg="Purple", font=12, command=check)
button_verify.place(x=50, y=70)


root.mainloop()
