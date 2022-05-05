import tkinter as tk
import xss_detector
import sql_injection_detector
from PIL import ImageTk
from tkinter import *
from PIL import Image
import validators


window = tk.Tk()




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
        xss_weakness = xss_detector.scan_xss(inp)
        sql_weakness = sql_injection_detector.scan_sql_injection(inp)


        if xss_weakness and sql_weakness:
            lbl.config(text = "there is a weakness of xss and sql injection in the site",fg = "red")
        elif xss_weakness:
            lbl.config(text = "there is a weakness of xss in the site",fg = "red")
        elif sql_weakness:
            lbl.config(text = "there is a weakness of sql injection in the site",fg = "red")
        else:
            lbl.config(text = "the site is safe", fg = "green")

        


    else:
        lbl.config(fg = "yellow")
        lbl.config(text = "not a valid target")





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


window.configure(bg="black")
window.title("hektos")
window.iconbitmap('images/icon.ico')


def main():
    window.mainloop()


main()