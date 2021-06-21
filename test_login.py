# test file for login
# importing modules needed from tkinter
from tkinter import *
from datetime import datetime, date
from tkinter import messagebox
from playsound import playsound
import random
import email_validator
import re

# initialising, sizing and configuring tkinter gui window
root = Tk()
root.title("Registration")
root.geometry("1000x700")
root.config(bg="yellow")

# Title Label. Placing and configuring
title_label = Label(text="YOUR DETAILS", bg="yellow", fg="dark green")
title_label.config(font="roboto 25 underline bold")
title_label.place(x=370, y=10)

# name Label. Placing and configuring
name_label = Label(text="Enter Your Fullname:", bg="yellow", fg="dark green")
name_label.config(font="roboto 12 bold")
name_label.place(x=100, y=100)

# name entry. Placing and configuring
name_entry = Entry(width=20)
name_entry.config(bg="White", fg="Dark Blue", font=10)
name_entry.place(x=700, y=100)

# id Label. Placing and configuring
id_label = Label(text="Enter Your ID Number: ", bg="yellow", fg="dark green")
id_label.config(font="roboto 12 bold")
id_label.place(x=100, y=200)

# id entry. Placing and configuring
id_entry = Entry(width=20)
id_entry.config(bg="White", fg="Dark Blue", font=10)
id_entry.place(x=700, y=200)

# email Label. Placing and configuring
email_label = Label(text="Enter Your Email Address: ", bg="yellow", fg="Dark Green")
email_label.config(font="roboto 12 bold")
email_label.place(x=100, y=300)

# email entry. Placing and configuring
email_entry = Entry(width=20)
email_entry.config(bg="White", fg="Dark Blue", font=10)
email_entry.place(x=700, y=300)

# Creating player id
player_id = random.randint(100000, 999999)

# creating regex for email verification
regex = "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"

# creating now and today for date and time
now = datetime.now()
today = date.today()


def test_validation():  # creating function for entry verification
    try:
        id_num = id_entry.get()  # making id entry id_num
        # Ensuring that id number is 13 numbers as per standard
        if len(id_entry.get()) > 13 or len(id_entry.get()) < 13:
            messagebox.showerror("ERROR!", "Must Consist of 13 Numbers")  # Error trapping
        elif not id_num.isdigit():  # ensuring that id entry contains digits only
            messagebox.showerror("ERROR!", "Please Enter a Number!")  # Error trapping

        email = email_entry.get()  # making email entry email
        if re.search(regex, email):  # using regex to verify email
            messagebox.showinfo("SUCCESS!", "Valid Email Address")  # Error trapping
        else:
            messagebox.showerror("ERROR!", "Invalid Email Address")  # Error trapping
            root.destroy()
            import test_main

        # extracting birthdate from id number
        year = id_num[:2]
        if year >= "22":
            year = "19" + year
        else:
            year = "20" + year
        month = id_num[2:4]
        day = id_num[4:6]
        dob = year, month, day
        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))

        if age >= 18:  # lets user play if they are over 18
            messagebox.showinfo("AGE", "You Qualify To Play")
            messagebox.showinfo("Play", "Lets Play!")
            w = open("Details.txt", "a+")  # writes all entered info on a text file
            w.write("\n" + "Name: " + name_entry.get() + "\n" + "Email Address: " + email_entry.get() + "\n" + "ID Number: "
                    + id_entry.get() + "\n" + "Logged into App at: " + str(now) + "\n" + "Player ID: " + str(player_id)
                    + "\n" + "DOB: " + str(dob) + "\n")
            w.close()
        else:  # returns to main menu if user is underage
            messagebox.showerror("AGE", "Come Back When You Are Old Enough")
            root.destroy()
            import test_main
    finally:  # opens next window if requirements are met
        root.destroy()
        import test_play


def test_clear():  # Clears all user changed values
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    email_entry.delete(0, END)


def test_kill():  # function that closes  window
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


# creating and placing validate button
validate_button = Button(text="Validate", width=10, bg="red", fg="white", highlightthickness=0, command=test_validation)
validate_button.place(x=350, y=500)

# creating and placing clear button
clear_button = Button(text="Clear", width=10, bg="#0357d8", fg="white", highlightthickness=0, command=test_clear)
clear_button.place(x=550, y=500)

# creating and placing exit button
kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=test_kill)
kill_btn.place(x=900, y=630)

# ensuring that window stay open until closed by user
root.mainloop()
