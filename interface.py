import tkinter as tk
from detectors import scan_xss, scan_sql_injection
from tkinter import *
from PIL import Image
import validators
import datetime
import utils.general


window = tk.Tk()


gif_label = tk.Label(window, image="", highlightthickness=0.1,
                     highlightbackground="#00F0F0")
gif_label.pack()

gif_file = "images/background.gif"

info = Image.open(gif_file)
frames = info.n_frames

images_list = [tk.PhotoImage(
    file=gif_file, format=f"gif -index {i}") for i in range(frames)]

header = ['Date', 'Url', 'Xss', 'Sql_injection']

count = 0


def animation(count):
    image = images_list[count]

    gif_label.configure(image=image)
    count += 2
    if count == frames:
        count = 0
    window.after(50, lambda: animation(count))


animation(count)


data_file = 'Url_Data.csv'


def has_header(filename):
    with open(filename) as file_obj:

        txt_file = file_obj.read().split(',')

        for tab in range(len(header)):
            if txt_file[tab].strip() != header[tab]:

                return False
    return True


def printInput():
    inp = inputtxt.get(1.0, "end-1c")

    valid = validators.url(inp)

    if valid:

        try:
            xss_weakness, sql_weakness = utils.general.find_url(data_file, inp)
        except:
            sql_weakness = scan_sql_injection(inp)
            xss_weakness = scan_xss(inp)

            data_add = [str(datetime.datetime.now()), inp,
                        scan_xss(inp), scan_sql_injection(inp)]
            header = ['Date', 'Url', 'Xss', 'Sql_injection']

            data = open(data_file, 'a', newline="")

            if not has_header(data_file):
                for header in header:
                    data.write(str(header)+', ')

            data.write('\n')
            for variable in data_add:
                data.write(str(variable)+', ')

            data.close()

        if xss_weakness and sql_weakness:

            lbl.config(
                text="there is a weakness of xss and sql injection in the site", fg="red")
        elif xss_weakness:
            lbl.config(text="there is a weakness of xss in the site", fg="red")
        elif sql_weakness:
            lbl.config(
                text="there is a weakness of sql injection in the site", fg="red")
        else:
            lbl.config(text="the site is safe", fg="green")
            utils.general.open_url(inp)

    else:
        lbl.config(text="not a valid target", fg="yellow")


inputtxt = tk.Text(window,
                   height=1,
                   width=50,
                   bg="black",
                   fg="yellow",
                   insertbackground='red'
                   )

inputtxt.pack()


printButton = tk.Button(window,
                        text="SCAN",
                        bg="black",
                        fg="yellow",
                        highlightbackground="#000000",
                        command=printInput)

printButton.pack()


lbl = tk.Label(window,  text="", bg="black", fg="red")
lbl.pack()


window.configure(bg="black")
window.title("hektos")
window.iconbitmap('images/icon.ico')


window.mainloop()
