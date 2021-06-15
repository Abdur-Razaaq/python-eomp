from tkinter import *
from datetime import datetime, date
from tkinter import messagebox
from playsound import playsound
import random
import re

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

player_id = random.randint(100000, 999999)
regex = '[A]@ .'
now = datetime.now()
today = date.today()


def validation():
    w = open("Details.txt", "a+")
    w.write(name_entry.get() + " " + " " + email_entry.get() + " " + " " + id_entry.get() + " " + " " +
            "Logged into App at: " + str(now) + "\n")
    w.close()

    id_num = id_entry.get()
    if len(id_entry.get()) > 13 or len(id_entry.get()) < 13:
        messagebox.showerror("ERROR!", "Must Consist of 13 Numbers")
    elif not id_num.isdigit():
        messagebox.showerror("ERROR!", "Please Enter a Number!")

    email = email_entry.get()
    if re.search(regex, email):
        pass
        # messagebox.showinfo("SUCCESS!", "Valid Email Address")
    else:
        pass
        # messagebox.showerror("ERROR!", "Invalid Email Address")

    year = id_num[:2]
    if year >= "22":
        year = "19" + year
    else:
        year = "20" + year
    month = id_num[2:4]
    day = id_num[4:6]
    dob = year, month, day
    age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
    if age >= 18:
        messagebox.showinfo("AGE", "You Qualify To Play")
        messagebox.showinfo("Play", "Lets Play!")
        root.destroy()
        import play
    else:
        messagebox.showerror("AGE", "Come Back When You Are Old Enough")
        root.destroy()


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

clear_button = Button(text="Clear", width=10, bg="#0357d8", fg="white", highlightthickness=0, command=clear)
clear_button.place(x=550, y=500)

kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
