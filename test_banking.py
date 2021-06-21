# creating test for banking
# importing modules needed from tkinter
from tkinter import *
from playsound import playsound
from tkinter import messagebox
from tkinter.ttk import Combobox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# initialising, sizing and configuring tkinter gui window
root = Tk()
root.title("Banking")
root.geometry("1000x700")


# crating function
def test_bank():  # creates function that verifies entries and sends email
    acc_name = AccH_entry.get()
    acc_number = AccN_entry.get()
    bank_type = bank_select.get()

    w = open("Details.txt", "a+")
    w.write("\n" + "Account Holder: " + acc_name + "\n" + "Account Number: " + acc_number + "\n" + "Bank: "
            + bank_type)
    w.close()

    if not acc_name.isalpha():
        messagebox.showerror("Account Holder", "Please Enter Valid Characters")

    elif not acc_number.isdigit() and len(acc_number) > 11 or len(acc_number) < 11:
        messagebox.showerror("Account Number", "Please Enter Valid Account Number")

    else:
        file_to_read = "Details.txt"
        file = open(file_to_read, "r")
        list_file = file.readlines()

        email_list = str(list_file)

        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email_list)
        email = emails[-1]

        sender_email_address = "lottoARJ@gmail.com"
        receiver_email_address = str(emails[-1])
        password = "lottotime"
        subject = "Congratulations!"
        msg = MIMEMultipart()
        msg['From'] = sender_email_address
        msg['To'] = receiver_email_address
        msg['Subject'] = subject
        txt = "You have won the lottery! \n"
        txt = txt + "You Will Be Informed Of Further Details"
        msg.attach(MIMEText(txt, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(sender_email_address, password)
        print(receiver_email_address)

        s.sendmail(sender_email_address, receiver_email_address, text)

        s.quit()

        messagebox.showinfo("EMAIL", "An Email Has Been Sent As Confirmation")
        msg_box = messagebox.askquestion("Convert", "Do You Want To Convert Your Winnings to Another Currency")
        if msg_box == "yes":
            playsound("move.mp3")
            root.destroy()
            import test_currency_convertor
        else:
            playsound("move.mp3")
            e_msg = messagebox.showinfo("GoodBye!", "Thank You For Playing!")
            if e_msg == "ok":
                root.destroy()


# banking label frame
banking_lbl_frm = LabelFrame(text="Banking Details")
banking_lbl_frm.config(font=" roboto 25", bg="Yellow", fg="maroon")
banking_lbl_frm.pack(fill="both", expand="yes")

# bank label
bank_label = Label(text="Select Your Bank: ")
bank_label.config(bg="Yellow", font="roboto 20")
bank_label.place(x=25, y=100)

# Combobox creation
n = StringVar()
bank_select = Combobox(root, width=21, textvariable=n)
# Adding combobox drop down list
bank_select['values'] = ("Standard Bank", "First National Bank", "Capitec", "ABSA")
bank_select.config(font="roboto 11")
# Placing combobox
bank_select.place(x=600, y=100)

# account holder label
AccH_lbl = Label(text="Account Holder: ")
AccH_lbl.config(bg="Yellow", font="roboto 20")
AccH_lbl.place(x=25, y=250)

# account holder entry
AccH_entry = Entry(width=20)
AccH_entry.config(bg="White", fg="Dark Blue", font="roboto", highlightthickness=0)
AccH_entry.place(x=600, y=250)

# account number label
AccN_label = Label(text="Account Number: ")
AccN_label.config(bg="Yellow", font="roboto 20")
AccN_label.place(x=25, y=400)

# account number entry
AccN_entry = Entry(width=20)
AccN_entry.config(bg="White", fg="Dark Blue", font="roboto", highlightthickness=0)
AccN_entry.place(x=600, y=400)

# transfer button
transfer_btn = Button(text="Transfer Cash", width=10, command=test_bank)
transfer_btn.config(bg="red", fg="white", highlightthickness=0)
transfer_btn.place(x=600, y=600)


# function for exit button
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
