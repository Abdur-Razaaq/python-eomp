from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

root = Tk()
root.title("Lotto Machine")
root.geometry("1000x700")
root.config(bg="yellow")
image1 = ImageTk.PhotoImage(Image.open("logo.png"))
image_label = Label(image=image1, bg='yellow', pady=0, padx=45)
image_label.place(x=240, y=55)


class Open:
    def __init__(self, window):
        self.start_btn = Button(window, text="It's Lotto Time", bg="red", width=30, fg="white", highlightthickness=0,
                                command=self.start)
        self.start_btn.place(x=380, y=500)
        self.kill_btn = Button(window, text="Exit", bg="#0357d8", fg="white", highlightthickness=0, command=self.kill)
        self.kill_btn.place(x=900, y=630)

    def start(self):
        playsound("click.mp3")
        root.destroy()
        import login

    def kill(self):
        playsound("exit.mp3")
        message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
        if message == "yes":
            root.destroy()


obj = Open(root)
root.mainloop()
