from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
from DAO.dao import *
from PIL import Image, ImageTk
from ttkthemes import themed_tk as tttk

def theme(value):
    if value == 'dark':
        root.set_theme('black')
    else:
        root.set_theme('blue')
        
#Root
root = tttk.ThemedTk()
root.set_theme('black')
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
                          #background="black",
                          fieldbackground="black")

#Frame principal
mainframe = ttk.Frame(root,style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W,N,E,S))

#Estilos de botones
estilos_botones = ttk.Style()
estilos_botones.configure('botones.TButton', 
                          font=("TkFixedFont", 12),
                          relief='groove',                                                     
                          )
estilos_botones.map('botones.TButton',background=[('active', '#050236')],foreground=[('active','blue')])

#Estilos reset.
estilos_botones = ttk.Style()
estilos_botones.configure('reset.TButton',
                          font="Ubuntu 12",
                          relief='sunken',                           
                          foreground="black")
estilos_botones.map('reset.TButton',background=[('active', '#050236')],foreground=[('active','red')])

#Creación de botones de herramientas
tool_bar = Label(mainframe)
tool_bar.configure(anchor='center')
tool_bar.grid(column=0,row=0,rowspan=8,sticky=(W,N,E,S))

avatar = ttk.Label(tool_bar, image=icon)

reset_button = ttk.Button(tool_bar,text="Reset",style='reset.TButton', command=lambda: reset(input_text_box,output_text_box))
inline_sql = ttk.Button(tool_bar,text='Inline Integer',style='botones.TButton',command=lambda: in_line(input_text_box,output_text_box))
inline_str = ttk.Button(tool_bar,text='Inline String(\')',style='botones.TButton', command=lambda: convert_str(input_text_box,output_text_box,1))
inline_str_2 = ttk.Button(tool_bar,text='Inline String(\")',style='botones.TButton', command=lambda: convert_str(input_text_box,output_text_box,2))
ransack_or = ttk.Button(tool_bar,width=5,text='Ransack',style='botones.TButton', command=lambda: ransack_search(input_text_box,output_text_box))



#Posicionamiento de botones.
avatar.grid(column=0,row=0,sticky=(W,N,E,S))
reset_button.grid(column=0,row=1,sticky=(W,E))
inline_sql.grid(column=0, row=2,sticky=(W,E))
inline_str.grid(column=0, row=3,sticky=(W,E))
inline_str_2.grid(column=0, row=4,sticky=(W,E))
ransack_or.grid(column=0, row=5,sticky=(W,E))


#Creación de cajas de texto.
#Input
input_name_box = Label(mainframe)
input_name_box.configure(#background="#00044A",
                         #foreground="white",
                         text='Entrada',
                         anchor="center",
                         font=("Arial", 15),
                         )
input_text_box = scrolledtext.ScrolledText(mainframe)
input_text_box.configure(#background="#00044A",
                         #foreground="black",
                         state="normal")
#output
output_name_box = Label(mainframe)
output_name_box.configure(#background="#00044A",
                          #foreground="white",
                          text='Salida',
                          anchor="center",
                          font=('Arial', 15)
                          )
output_text_box = scrolledtext.ScrolledText(mainframe)
output_text_box.configure(#background="#00044A",
                          #foreground="black",
                          state="disabled")



#posicionamiento de cajas de texto.
input_text_box.grid(column=1,row=0,columnspan=4,rowspan=4,sticky=(W,N,E,S))
input_name_box.grid(column=1,row=4,columnspan=4,sticky=(W,N,E,S),ipady=10)
output_name_box.grid(column=1,row=10,columnspan=4,sticky=(W,N,E,S),ipady=10)
output_text_box.grid(column=1,row=5,columnspan=4,rowspan=4,sticky=(W,N,E,S))


themes_bar = Label(mainframe)
themes_bar.configure(anchor='center')
themes_bar.grid(column=0,row=10,sticky=(N,E))
#Temas
dark_theme = ttk.Button(themes_bar,text="Tema Oscuro", command=lambda: theme('dark'))
light_theme = ttk.Button(themes_bar,text="Tema Claro", command=lambda: theme('light'))

#Posicionamiento
dark_theme.grid(column=0, row=0,sticky=(W,E))
light_theme.grid(column=1, row=0,sticky=(W,E))


for child in mainframe.winfo_children():
    child.grid_configure(padx=1,pady=1)


#Inicio
root.mainloop()