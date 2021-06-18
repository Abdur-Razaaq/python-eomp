from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox
import random


root = Tk()
root.title("Let's Play!")
root.geometry("1000x700")
root.config(bg="yellow")
image1 = ImageTk.PhotoImage(Image.open("lotto.png"))
image_label = Label(image=image1, bg='yellow', pady=0, padx=45)
image_label.place(x=240, y=-55)


def play():
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    draw = numbers[:6]

    lot1["state"] = "normal"
    lot1.delete(0, END)
    lot1.insert(0, draw[0])
    lot1["state"] = "readonly"

    lot2["state"] = "normal"
    lot2.delete(0, END)
    lot2.insert(0, draw[1])
    lot2["state"] = "readonly"

    lot3["state"] = "normal"
    lot3.delete(0, END)
    lot3.insert(0, draw[2])
    lot3["state"] = "readonly"

    lot4["state"] = "normal"
    lot4.delete(0, END)
    lot4.insert(0, draw[3])
    lot4["state"] = "readonly"

    lot5["state"] = "normal"
    lot5.delete(0, END)
    lot5.insert(0, draw[4])
    lot5["state"] = "readonly"

    lot6["state"] = "normal"
    lot6.delete(0, END)
    lot6.insert(0, draw[5])
    lot6["state"] = "readonly"

    row1 = [int(spin1.get()), int(spin2.get()), int(spin3.get()), int(spin4.get()), int(spin5.get()), int(spin6.get())]
    row2 = draw
    compare = (set(row1).intersection(row2))
    results = len(compare)
    messagebox.showinfo("RESULTS", "You Got " + str(results) + " Winning Ball(s)")

    if results <= 1:
        messagebox.showinfo("Unlucky", "You Have Won R0.00")
    elif results == 2:
        messagebox.showinfo("LUCKY", "You Have Won R20.00")
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import banking
    elif results == 3:
        messagebox.showinfo("LUCKY", "You Have Won R100.50")
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import banking
    elif results == 4:
        messagebox.showinfo("LUCKY", "You Have Won R2384.00")
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import banking
    elif results == 5:
        messagebox.showinfo("LUCKY", "You Have Won R8584.00")
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import banking
    else:
        messagebox.showinfo("JACKPOT", "YOU HAVE WON THE JACKPOT")
        messagebox.showinfo("JACKPOT", "You Have Won R10 000 000")
        messagebox.askquestion("LUCKY", "Would You Like To Claim?")
        if "yes":
            root.destroy()
            import banking


def claim():
    message = messagebox.askquestion("Claim", "Are You Sure You Are Finished Playing?")
    if message == "yes":
        root.destroy()
        import banking


def clear():  # Clears all user changed values
    spin1.delete(0, END)
    spin2.delete(0, END)
    spin3.delete(0, END)
    spin4.delete(0, END)
    spin5.delete(0, END)
    spin6.delete(0, END)

    # Clears Generated numbers
    lot1['state'] = "normal"
    lot1.delete(0, END)
    lot1['state'] = "readonly"
    lot2['state'] = "normal"
    lot2.delete(0, END)
    lot2['state'] = "readonly"
    lot3['state'] = "normal"
    lot3.delete(0, END)
    lot3['state'] = "readonly"
    lot4['state'] = "normal"
    lot4.delete(0, END)
    lot4['state'] = "readonly"
    lot5['state'] = "normal"
    lot5.delete(0, END)
    lot5['state'] = "readonly"
    lot6['state'] = "normal"
    lot6.delete(0, END)
    lot6['state'] = "readonly"


play_lbl = Label(text="Select Your Lucky Numbers")
play_lbl.config(bg="Yellow", fg="Dark Blue", font="roboto 22 bold underline")
play_lbl.place(x=270, y=180)

spin1 = Spinbox(from_=1, to=49, width=2, state="normal")
spin1.config(bg="White", fg="#696517", font="roboto 22", highlightthickness=0)
spin1.place(x=80, y=280)

spin2 = Spinbox(from_=1, to=49, width=2, state="normal")
spin2.config(bg="White", fg="Green", font="roboto 22", highlightthickness=0)
spin2.place(x=230, y=280)

spin3 = Spinbox(from_=1, to=49, width=2, state="normal")
spin3.config(bg="White", fg="#b500b2", font="roboto 22", highlightthickness=0)
spin3.place(x=380, y=280)

spin4 = Spinbox(from_=1, to=49, width=2, state="normal")
spin4.config(bg="White", fg="#ff2929", font="roboto 22", highlightthickness=0)
spin4.place(x=530, y=280)

spin5 = Spinbox(from_=1, to=49, width=2, state="normal")
spin5.config(bg="White", fg="#005a16", font="roboto 22", highlightthickness=0)
spin5.place(x=680, y=280)

spin6 = Spinbox(from_=1, to=49, width=2, state="normal")
spin6.config(bg="White", fg="Dark Blue", font="roboto 22", highlightthickness=0)
spin6.place(x=830, y=280)

results_lbl = Label(text="Results:")
results_lbl.config(bg="Yellow", fg="Dark Blue", font="roboto 22 bold underline")
results_lbl.place(x=430, y=355)

lot1 = Entry(width=3, state="readonly")
lot1.config(bg="White", fg="#696517", font="roboto 22", highlightthickness=0)
lot1.place(x=80, y=450)

lot2 = Entry(width=3, state="readonly")
lot2.config(bg="White", fg="Green", font="roboto 22", highlightthickness=0)
lot2.place(x=230, y=450)

lot3 = Entry(width=3, state="readonly")
lot3.config(bg="White", fg="#b500b2", font="roboto 22", highlightthickness=0)
lot3.place(x=380, y=450)

lot4 = Entry(width=3, state="readonly")
lot4.config(bg="White", fg="#ff2929", font="roboto 22", highlightthickness=0)
lot4.place(x=530, y=450)

lot5 = Entry(width=3, state="readonly")
lot5.config(bg="White", fg="#005a16", font="roboto 22", highlightthickness=0)
lot5.place(x=680, y=450)

lot6 = Entry(width=3, state="readonly")
lot6.config(bg="White", fg="Dark Blue", font="roboto 22", highlightthickness=0)
lot6.place(x=830, y=450)

# Buttons

play_btn = Button(text="Play", width=10, command=play)
play_btn.config(bg="red", fg="white", font="roboto", highlightthickness=0)
play_btn.place(x=350, y=550)

clear_btn = Button(text="Clear", width=10)
clear_btn.config(bg="red", fg="white", font="roboto", highlightthickness=0, command=clear)
clear_btn.place(x=350, y=600)

claim_btn = Button(text="Claim Winnings", width=10, command=claim)
claim_btn.config(bg="green", fg="white", font="roboto", highlightthickness=0)
claim_btn.place(x=350, y=650)


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
