from tkinter import *
from PIL import Image, ImageTk
from playsound import playsound
from tkinter import messagebox


root = Tk()
root.title("Let's Play!")
root.geometry("1000x700")
root.config(bg="yellow")
image1 = ImageTk.PhotoImage(Image.open("lotto.png"))
image_label = Label(image=image1, bg='yellow', pady=10, padx=45)
image_label.place(x=220, y=1)



root.mainloop()
