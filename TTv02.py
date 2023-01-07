from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from DAO.dao import *
from PIL import Image, ImageTk
from tkinter import scrolledtext


#Root
root = Tk()
root.title('Utils V2')
root.geometry('+500+80')
root.resizable(width=False, height=False)
root.configure(background='black')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#icono ventana
icon_image = Image.open('./Assets/sunset.jpg')
icon_window = ImageTk.PhotoImage(icon_image)
root.iconphoto(True,icon_window)

#img
#img = icon_image.resize((150,150)) #resize image
icon = ImageTk.PhotoImage(icon_image) #convert image



#Estilos de Mainframe

mainframe_style = ttk.Style()
mainframe_style.configure('mainframe.TFrame',
                          background="black",
                          fieldbackground="black")
mainframe_style.theme_use('default')

#Frame principal
mainframe = ttk.Frame(root,style='mainframe.TFrame')
avatar = ttk.Label(mainframe, image=icon)
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))

#Estilos de botones
estilos_botones = ttk.Style()
estilos_botones.configure('botones.TButton', 
                          font="TkFixedFont 12",
                          relief='groove', 
                          background="#00044A",
                          foreground="white")
estilos_botones.map('botones.TButton',background=[('active', '#050236')])
#Estilos reset.
estilos_botones = ttk.Style()
estilos_botones.configure('reset.TButton',
                          font="Ubuntu 12",
                          relief='sunken', 
                          background="#00044A",
                          foreground="white")
estilos_botones.map('reset.TButton',background=[('active', '#050236')],foreground=[('active','red')])

#Creación de botones de herramientas
reset_button = ttk.Button(mainframe,text="Reset",style='reset.TButton')
inline_sql = ttk.Button(mainframe,text='Inline Integer',style='botones.TButton',command=lambda: in_line(input_text_box,output_text_box))
inline_str = ttk.Button(mainframe,text='Inline String',style='botones.TButton', command=lambda: convert_str(input_text_box,output_text_box))
inline_mocas = ttk.Button(mainframe,text='Inline MOCAS (TODO)',style='botones.TButton')


#Posicionamiento de botones.
avatar.grid(column=0,row=0,sticky=(W,N,E,S))
reset_button.grid(column=0,row=1,sticky=(W,N,E,S))
inline_sql.grid(column=0, row=2,sticky=(W,N,E,S))
inline_str.grid(column=0, row=3,sticky=(W,N,E,S))
inline_mocas.grid(column=0, row=4,sticky=(W,N,E,S))

#Creación de cajas de texto.
#Input
input_name_box = Label(mainframe)
input_name_box.configure(background="#00044A",
                         foreground="white",
                         text='Entrada',
                         anchor="center",
                         font='TkHeadingFont 15',
                         )
input_text_box = scrolledtext.ScrolledText(mainframe)
input_text_box.configure(background="#00044A",foreground="white",state="normal")
#output
output_name_box = Label(mainframe)
output_name_box.configure(background="#00044A",
                          foreground="white",
                          text='Salida',
                          anchor="center",
                          font='TkHeadingFont 15'
                          )
output_text_box = scrolledtext.ScrolledText(mainframe)
output_text_box.configure(background="#00044A",foreground="white",state="disabled")



#posicionamiento de cajas de texto.
input_name_box.grid(column=1,row=4,columnspan=4,sticky=(W,N,E,S),ipady=10)
input_text_box.grid(column=1,row=0,columnspan=4,rowspan=4,sticky=(W,N,E,S))
output_name_box.grid(column=1,row=10,columnspan=4,sticky=(W,N,E,S),ipady=10)
output_text_box.grid(column=1,row=5,columnspan=4,rowspan=4,sticky=(W,N,E,S))


for child in mainframe.winfo_children():
    child.grid_configure(padx=3,pady=3)


#Inicio
root.mainloop()