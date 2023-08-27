from pathlib import Path
import os
import login
import signup
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import localdb as ldb

current_path = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH_RELATIVE = 'assets/frame2'
full_path = os.path.join(current_path, ASSETS_PATH_RELATIVE)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(full_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x400")
window.configure(bg = "#FFFFFF")
window.title('ChatAPP')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    262.0,
    400.0,
    fill="#5C82F2",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    131.0,
    200.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    131.0,
    199.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    431.0,
    31.0,
    image=image_image_3
)

name = ldb.name()

canvas.create_text(
    400.0,
    329.0,
    anchor="nw",
    text=name,
    fill="#1E1E1E",
    font=("Poppins Medium", 15 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    131.0,
    366.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open(1),
    relief="flat"
)
button_1.place(
    x=330.0,
    y=89.0,
    width=201.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open(2),
    relief="flat"
)
button_2.place(
    x=330.0,
    y=165.0,
    width=200.0,
    height=49.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("CHAT APP"),
    relief="flat"
)
button_3.place(
    x=331.0,
    y=240.0,
    width=200.0,
    height=49.0
)


def open(x):
    if x == 1:
        window.destroy()
        login.GUILOGIN()
    else:
        window.destroy()
        signup.GUISIGNUP()    
        


window.resizable(False, False)
window.mainloop()
