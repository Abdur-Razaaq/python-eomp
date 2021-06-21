# creating test for currency convertor
# importing modules needed from tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from tkinter.ttk import Combobox
import requests

# initialising, sizing and configuring tkinter gui window
root = Tk()
root.title("Convert")
root.geometry("1000x700")
root.config(bg="yellow")

value = IntVar()

# Retrieving information from external JSON file
info = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
info_json = info.json()

conversion_rate = info_json['conversion_rates']

# Creating the FROM (Standard value is ZAR)
from_label = Label(root, text="From: ZAR")
from_label.config(bg="yellow", fg="dark blue", font="Roboto 25")
from_label.place(x=410, y=10)


# Conversion Label
con_label = Label(root, text="Result")
con_label.config(bg="yellow", fg="dark blue", font="roboto 20")
con_label.place(x=450, y=580)

# Winning Label
win_label = Label(root, text="Value:")
win_label.config(bg="Yellow", fg="dark blue", font="roboto 20")
win_label.place(x=380, y=68)

# Combobox
n = StringVar()
winnings = Combobox(root, width=21, textvariable=n)
# Adding combobox drop down list
winnings['values'] = ("20.00", "100.50", "2384.00", "8584.00", "10000000.00")
winnings.config(font="roboto 11")
# Placing combobox
winnings.place(x=480, y=75)

# Conversion of the data with the loop
convert = Label(root, text="To:")
convert.config(bg="yellow", fg="dark blue", font="roboto 23")
convert.place(x=470, y=120)

# creating currency list. configuring
con_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    con_list.insert(END, str(i))
    con_list.config(bg="Green", fg="White", font="roboto 20")
    con_list.place(x=340, y=180)


# Defining Currency Conversion
def test_convert_currency():
    playsound("move.mp3")
    num = float(winnings.get())
    print(info_json['conversion_rates'][con_list.get(ACTIVE)])
    ans = num * info_json['conversion_rates'][con_list.get(ACTIVE)]
    con_label['text'] = ans


# Currency Conversion Button
con_btn = Button(root, command=test_convert_currency, text="Convert", width=20)
con_btn.config(bg="Red", fg="white")
con_btn.place(x=410, y=650)


# exit function
def test_kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


# exit button
kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=test_kill)
kill_btn.place(x=900, y=630)

# ensures that window stays open until user exits it
root.mainloop()
