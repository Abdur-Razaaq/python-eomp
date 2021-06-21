# test file for main
# importing modules needed from tkinter
from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox

# initialising, sizing and configuring tkinter gui window
root = Tk()
root.title("Lotto Machine")
root.geometry("1000x700")
root.config(bg="yellow")

# adding images
image1 = ImageTk.PhotoImage(Image.open("logo.png"))
image_label = Label(image=image1, bg='yellow', pady=0, padx=45)
image_label.place(x=240, y=55)


# Creating an object called open
class Open:
    def __init__(self, window):  # initialising the object
        # creating, placing and configuring start button
        self.start_btn = Button(window, text="It's Lotto Time", bg="red", width=30, fg="white", highlightthickness=0,
                                command=self.test_start)
        self.start_btn.place(x=380, y=500)
        # creating, placing and configuring exit button
        self.kill_btn = Button(window, text="Exit", bg="#0357d8", fg="white", highlightthickness=0,
                               command=self.test_kill)
        self.kill_btn.place(x=900, y=630)

    def test_start(self):  # creating function for start button
        playsound("click.mp3")
        root.destroy()
        import test_login

    def test_kill(self):  # creating function for kill button
        playsound("exit.mp3")
        message = messagebox.askquestion("Exit Application", "Are You Sure You Want To Exit?")
        if message == "yes":
            root.destroy()


# ensures that everything in the object is displayed on the tkinter gui, root
obj = Open(root)
# ensuring that window stay open until closed by user
root.mainloop()
