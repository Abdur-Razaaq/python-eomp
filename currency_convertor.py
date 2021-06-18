from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.title("Convert")
root.geometry("1000x700")
root.config(bg="yellow")


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
