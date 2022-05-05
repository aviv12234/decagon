import tkinter as tk
import os
import xss_detector
from PIL import ImageTk
from tkinter import *
from PIL import Image
import validators


window = tk.Tk()

window.configure(bg="black")
window.title("hektos")


file="images/background.gif"

info = Image.open(file)




frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
def animation(count):
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 2
    if count == frames:
        count = 0
    window.after(50,lambda :animation(count))

gif_label = tk.Label(window,image="",highlightthickness=0.1, highlightbackground="#00F0F0")
gif_label.pack()





animation(count)


def printInput():
    inp = inputtxt.get(1.0, "end-1c")

    valid=validators.url(inp)

    if valid:
        secure = xss_detector.scan_xss(inp)
        if secure == "True":
            lbl.config(fg = "green")
        elif secure == "False":
            lbl.config(fg = "red")


    else:
        lbl.config(fg = "yellow")
        lbl.config(text = "not a valid target")



    lbl.config(text = secure)

inputtxt = tk.Text(window,
                   height = 1,
                   width = 50,
                   bg = "black",
                   fg = "yellow",
                   insertbackground='red'
                   )

inputtxt.pack()

printButton = tk.Button(window,
                        text = "SCAN",
                        bg = "black",
                        fg = "yellow",
                        highlightbackground="#000000",
                        command = printInput)
printButton.pack()

lbl = tk.Label(window, text = "", bg = "black", fg = "red")
lbl.pack()











def main():
    window.mainloop()



    



main()

