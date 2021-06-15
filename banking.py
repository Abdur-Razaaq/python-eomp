from tkinter import *
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Banking")
root.geometry("1000x700")

banking_lbl_frm = LabelFrame(text="Banking Details")
banking_lbl_frm.config(font=" roboto 20", bg="sky blue")
banking_lbl_frm.pack(fill="both", expand="yes")

bank_label = Label(text="Select Your Bank: ")
bank_label.place(x=25, y=50)

root.mainloop()
