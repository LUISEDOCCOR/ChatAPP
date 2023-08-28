from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import localdb as ldb


current_path = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH_RELATIVE = 'assets/frame3'
full_path = os.path.join(current_path, ASSETS_PATH_RELATIVE)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(full_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x400")
window.configure(bg = "#FFFFFF")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    80.0,
    82.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    80.0,
    278.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    379.0,
    198.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    80.0,
    42.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    64.0,
    213.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    64.0,
    213.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    337.0,
    351.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    378.0,
    37.0,
    image=image_image_8
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=489.0,
    y=331.0,
    width=55.0,
    height=38.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=60.0,
    y=242.0,
    width=39.0,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=60.0,
    y=242.0,
    width=39.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=111.0,
    y=195.0,
    width=29.0,
    height=36.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    379.0,
    191.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=231.0,
    y=65.0,
    width=296.0,
    height=250.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    337.0,
    351.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=211.0,
    y=340.0,
    width=252.0,
    height=21.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    64.0,
    308.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    64.0,
    308.0,
    image=image_image_10
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=60.0,
    y=337.0,
    width=39.0,
    height=35.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=60.0,
    y=337.0,
    width=39.0,
    height=35.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=111.0,
    y=290.0,
    width=29.0,
    height=36.0
)
button_image_5 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_5.place(
    x=504.0,
    y=20.0,
    width=39.0,
    height=35.0
)
#Get Data
Name, Gmail = ldb.data()


#Primer contacto
canvas.create_text(
    26.0,
    298.0,
    anchor="nw",
    text="1",
    fill="#1E1E1E",
    font=("Poppins Regular", 10 * -1)
)

#Segundo contacto
canvas.create_text(
    26.0,
    203.0,
    anchor="nw",
    text="2",
    fill="#1E1E1E",
    font=("Poppins Regular", 10 * -1)
)

#Nombre del usuario actual
canvas.create_text(
    16.0,
    109.0,
    anchor="nw",
    text=Name,
    fill="#1E1E1E",
    font=("Poppins Regular", 12 * -1)
)

#correo del usuario
canvas.create_text(
    16.0,
    82.0,
    anchor="nw",
    text=Gmail,
    fill="#1E1E1E",
    font=("Poppins Regular", 15 * -1)
)

#nombre de la persona co la que se esta en chat
canvas.create_text(
    334.0,
    27.0,
    anchor="nw",
    text="4",
    fill="#1E1E1E",
    font=("Poppins Regular", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
