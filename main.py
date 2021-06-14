from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Lotto Machine")
root.geometry("1000x700")
root.config(bg="yellow")
image1 = ImageTk.PhotoImage(Image.open("logo.png"))
image_label = Label(image=image1, bg='yellow', pady=45, padx=45)
image_label.place(x=220, y=30)


def start():
    playsound("click.mp3")
    root.destroy()
    import login


def kill():
    playsound("exit.mp3")
    message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
    if message == "yes":
        root.destroy()


start_btn = Button(text="Let's Play", bg="red", width=30, fg="white", highlightthickness=0, command=start)
start_btn.place(x=380, y=500)

kill_btn = Button(text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=kill)
kill_btn.place(x=900, y=630)

root.mainloop()
