import tkinter as tk
import os
import xss_detector
from PIL import ImageTk
from tkinter import *
from PIL import Image


window = tk.Tk()

canvas = tk.Canvas(window, height=1000, width=1000, bg="#000000")
canvas.pack(expand=YES, fill=BOTH)


frame = tk.Frame(window,bg="black")
frame.place(relwidth=0.9,relheight=0.9,relx=0, rely=0)

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = xss_detector.scan_xss(inp))

inputtxt = tk.Text(frame,
                   height = 1,
                   width = 50)

inputtxt.pack()

printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()




file="background.gif"

info = Image.open(file)




frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
def animation(count):
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    frame.after(50,lambda :animation(count))

gif_label = tk.Label(frame,image="")
gif_label.pack()





animation(count)






def main():
    window.mainloop()



    



main()

