from tkinter import *
import rsaidnumber
from datetime import date, datetime
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.title("Registration")
root.geometry("1000x700")
root.config(bg="yellow")


title_label = Label(text="YOUR DETAILS", bg="yellow", fg="dark green")
title_label.config(font="roboto 25 underline bold")
title_label.place(x=370, y=10)

# Labels and Text Entries
name_label = Label(text="Enter Your Fullname:", bg="yellow", fg="dark green")
name_label.config(font="roboto 12 bold")
name_label.place(x=100, y=100)

name_entry = Entry(width=20)
name_entry.config(bg="White", fg="Dark Blue", font=10)
name_entry.place(x=700, y=100)

id_label = Label(text="Enter Your ID Number: ", bg="yellow", fg="dark green")
id_label.config(font="roboto 12 bold")
id_label.place(x=100, y=200)

id_entry = Entry(width=20)
id_entry.config(bg="White", fg="Dark Blue", font=10)
id_entry.place(x=700, y=200)

email_label = Label(text="Enter Your Email Address: ", bg="yellow", fg="Dark Green")
email_label.config(font="roboto 12 bold")
email_label.place(x=100, y=300)

email_entry = Entry(width=20)
email_entry.config(bg="White", fg="Dark Blue", font=10)
email_entry.place(x=700, y=300)


def validation():
    root.destroy()
    import play


def clear():  # Clears all user changed values
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    email_entry.delete(0, END)


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


validate_button = Button(text="Validate", width=10, bg="red", fg="white", highlightthickness=0, command=validation)
validate_button.place(x=350, y=500)

clear_button = Button(text="Clear", width=10, bg="red", fg="white", highlightthickness=0, command=clear)
clear_button.place(x=550, y=500)

kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
