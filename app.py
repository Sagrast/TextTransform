import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from ttkthemes import themed_tk as tttk
from frames import Toolbar


class TextTransform(tttk.ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_theme('black')
        self.title('Utilidades')
        self.geometry('+500+80')
        self.resizable(width=False, height=False)
        self.configure(background='black')

        # icono ventana
        icon_image = Image.open('./Assets/sunset.jpg')
        icon_window = ImageTk.PhotoImage(icon_image)
        self.iconphoto(True, icon_window)

        # Estilos de Mainframe

        mainframe_style = ttk.Style()
        mainframe_style.configure('mainframe.TFrame',
                                  fieldbackground="black")

        # Frame principal
        mainframe = ttk.Frame(self, style='mainframe.TFrame')
        mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

        # Estilos de botones
        estilos_botones = ttk.Style()
        estilos_botones.configure('botones.TButton',
                                  font=("TkFixedFont", 9),
                                  relief='groove',
                                  anchor='center'
                                  )
        estilos_botones.map('botones.TButton', background=[
                            ('active', 'grey')], foreground=[('active', 'blue')])

        # Estilos reset.
        estilos_botones = ttk.Style()
        estilos_botones.configure('reset.TButton',
                                  font=("Ubuntu", 12),
                                  relief='sunken',
                                  foreground="black",
                                  anchor='center')
        estilos_botones.map('reset.TButton', background=[
                            ('active', '#050236')], foreground=[('active', 'red')])

        # Estilos paneles
       
        toolbar = Toolbar(mainframe, icon_image)
        toolbar.grid(column=0, row=0, sticky=(N, S))
        toolbar.columnconfigure(0, weight=1)
        # Renegade
        frames = [PhotoImage(file='./Assets/mini_renegade.gif',
                             format='gif -index %i' % (i)) for i in range(7)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == 7:
                ind = 0
            renegade.configure(image=frame)
            themes_bar.after(100, update, ind)

        themes_bar = Label(mainframe)
        themes_bar.configure(anchor='center')
        themes_bar.grid(column=0, row=10, sticky=(N, E))
        renegade = Label(themes_bar, image=frames[0])
        themes_bar.after(0, update, 0)
        # Temas

        dark_theme = ttk.Button(
            themes_bar, text="Tema Oscuro", command=lambda: theme('dark'))
        light_theme = ttk.Button(
            themes_bar, text="Tema Claro", command=lambda: theme('light'))

        # Posicionamiento
        dark_theme.grid(column=0, row=0, sticky=(W))
        light_theme.grid(column=1, row=0, sticky=(E))
        renegade.grid(column=3, row=0, sticky=(W))
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=1, pady=1)            

        def theme(value):
            if value == 'dark':
                self.set_theme('black')
            else:
                self.set_theme('blue')
            # Estilos de botones
                estilos_botones = ttk.Style()
                estilos_botones.configure('botones.TButton',
                                          font=("TkFixedFont", 8),
                                          relief='groove',
                                          anchor='center'
                                          )
                estilos_botones.map('botones.TButton', background=[
                                    ('active', '#050236')], foreground=[('active', 'blue')])

                # Estilos reset.
                estilos_botones = ttk.Style()
                estilos_botones.configure('reset.TButton',
                                          font=("Ubuntu", 12),
                                          relief='sunken',
                                          foreground="black",
                                          anchor='center')
                estilos_botones.map('reset.TButton', background=[
                                    ('active', '#050236')], foreground=[('active', 'red')])
           

app = TextTransform()
app.mainloop()
