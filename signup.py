def GUISIGNUP():
    import database as db
    from pathlib import Path
    import os

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    import tkinter as tk

    current_path = os.path.dirname(os.path.abspath(__file__))
    ASSETS_PATH_RELATIVE = 'assets/frame0'
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
        430.0,
        108.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        430.0,
        187.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        430.0,
        267.0,
        image=image_image_4
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        430.5,
        117.5,
        image=entry_image_1
    )
    name = Entry(
        bd=0,
        bg="#A699E9",
        fg="#000716",
        highlightthickness=0
    )
    name.place(
        x=304.0,
        y=103.0,
        width=253.0,
        height=27.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        430.5,
        196.5,
        image=entry_image_2
    )
    gmail = Entry(
        bd=0,
        bg="#A699E9",
        fg="#000716",
        highlightthickness=0
    )
    gmail.place(
        x=304.0,
        y=182.0,
        width=253.0,
        height=27.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        430.5,
        276.5,
        image=entry_image_3
    )
    password = Entry(
        bd=0,
        bg="#A699E9",
        fg="#000716",
        highlightthickness=0
    )
    password.place(
        x=304.0,
        y=262.0,
        width=253.0,
        height=27.0
    )

    canvas.create_text(
        17.0,
        145.0,
        anchor="nw",
        text="Welcome",
        fill="#FFFFFF",
        font=("Poppins Medium", 40 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        431.0,
        31.0,
        image=image_image_5
    )

    canvas.create_text(
        17.0,
        191.0,
        anchor="nw",
        text="ChatAPP",
        fill="#FFFFFF",
        font=("Poppins Medium", 30 * -1)
    )

    canvas.create_text(
        304.0,
        82.0,
        anchor="nw",
        text="Name",
        fill="#FFFFFF",
        font=("Poppins Light", 15 * -1)
    )

    canvas.create_text(
        304.0,
        161.0,
        anchor="nw",
        text="Gmail",
        fill="#FFFFFF",
        font=("Poppins Light", 15 * -1)
    )

    canvas.create_text(
        304.0,
        240.0,
        anchor="nw",
        text="Password",
        fill="#FFFFFF",
        font=("Poppins Light", 15 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: getData(),
        relief="flat"
    )
    button_1.place(
        x=331.0,
        y=328.0,
        width=200.0,
        height=49.0
    )

    def getData():
        Name = name.get() #Obtenemos nuestra información
        Gmail = gmail.get() #Obtenemos nuestra información
        Password = password.get() #Obtenemos nuestra información
        
        #Borramos los campos de la informacion 
        #Comenzamos a verificar la información
        name.delete(0, tk.END)
        gmail.delete(0, tk.END)
        password.delete(0, tk.END)
        
        #Si estan vacios los campos pedimos que rellene la infomación
        if Name == '' or Gmail == '' or Password == '':
            name.insert(tk.END,'Fill in all the fields')
        else:
            if '@' in Gmail: #Si nuestro correo contiene un @ seguimos
                Gmail = Gmail.lower()#pasamos el correo a minusculas
                if len(Password) < 5:
                    password.insert(tk.END, 'Min 5 characters')#Si no pasa el filtro marcamos error    
                else:
                    x = db.verifyGmail(Gmail)
                    if x:
                        db.add(Name, Gmail, Password)
                    else:
                        gmail.insert(tk.END, 'That email is in use')    
            else:
                gmail.insert(tk.END, 'Invalid email')#Si no pasa el filtro marcamos error          
                


    window.resizable(False, False)
    window.mainloop()

