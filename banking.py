from tkinter import *
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Banking")
root.geometry("1000x700")


def bank():
    acc_number = AccN_entry.get()
    acc_name = AccH_entry.get()

    if not acc_name.isalpha():
        messagebox.showerror("Account Holder", "Please Enter Valid Characters")

    elif not acc_number.isdigit():
        messagebox.showerror("Account Number", "Please Enter Valid Numbers")

    else:
        root.destroy()


def go_convert():
    root.destroy()
    import currency_convertor


banking_lbl_frm = LabelFrame(text="Banking Details")
banking_lbl_frm.config(font=" roboto 25", bg="Yellow", fg="maroon")
banking_lbl_frm.pack(fill="both", expand="yes")

bank_label = Label(text="Select Your Bank: ")
bank_label.config(bg="Yellow", font="roboto 20")
bank_label.place(x=25, y=100)

variable = StringVar(root)
variable.set("Select Bank")
bank_menu = OptionMenu(root, variable, "First National Bank", "Standard Bank", "Capitec", "ABSA")
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

transfer_btn = Button(text="Transfer Cash", width=10, command=bank)
transfer_btn.place(x=600, y=600)


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

convert_btn = Button(text="Convert", bg="#0357d8", fg="white", highlightthickness=0, command=go_convert)
convert_btn.place(x=750, y=630)

root.mainloop()
