from tkinter import *
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Banking")
root.geometry("1000x700")

banking_lbl_frm = LabelFrame(text="Banking Details")
banking_lbl_frm.config(font=" roboto 25", bg="Yellow", fg="maroon")
banking_lbl_frm.pack(fill="both", expand="yes")

bank_label = Label(text="Select Your Bank: ")
bank_label.config(bg="Yellow", font="roboto 20")
bank_label.place(x=25, y=100)

options = ["FNB", "Standard Bank", "Capitec", "ABSA"]
variable = StringVar(root)
variable.set("Select Bank")
bank_menu = OptionMenu(root, variable, "FNB", "Standard Bank", "Capitec", "ABSA")
bank_menu.config(bg="Red", fg="white", font="roboto", highlightthickness=0)
bank_menu.place(x=600, y=100)

AccH_lbl = Label(text="Account Holder: ")
AccH_lbl.config(bg="Yellow", font="roboto 20")
AccH_lbl.place(x=25, y=250)

AccH_entry = Entry(width=20)
AccH_entry.config(bg="White", fg="Dark Blue", font="roboto", highlightthickness=0)
AccH_entry.place(x=600, y=250)

AccN_label = Label(text="Account Number: ")
AccN_label.config(bg="Yellow", font="roboto 20")
AccN_label.place(x=25, y=400)

AccN_entry = Entry(width=20)
AccN_entry.config(bg="White", fg="Dark Blue", font="roboto", highlightthickness=0)
AccN_entry.place(x=600, y=400)


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
