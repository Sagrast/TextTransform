from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import StringVar
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
root.title('Utilidades')
root.geometry('+500+80')
root.resizable(width=False, height=False)
root.configure(background='black')


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
                          anchor='center'                                                     
                          )
estilos_botones.map('botones.TButton',background=[('active', '#050236')],foreground=[('active','blue')])

#Estilos reset.
estilos_botones = ttk.Style()
estilos_botones.configure('reset.TButton',
                          font=("Ubuntu", 12),
                          relief='sunken',                           
                          foreground="black",
                          anchor='center')
estilos_botones.map('reset.TButton',background=[('active', '#050236')],foreground=[('active','red')])

#Creación de botones de herramientas
tool_bar = ttk.Label(mainframe)
tool_bar.grid(column=0,row=0)



avatar = ttk.Label(tool_bar, image=icon)

reset_button = ttk.Button(tool_bar,text="RESET",style='reset.TButton', command=lambda: reset(input_text_box,output_text_box))
inline_sql = ttk.Button(tool_bar,width=15,text='Inline Integer',style='botones.TButton',command=lambda: in_line(input_text_box,output_text_box))
inline_str = ttk.Button(tool_bar,width=15,text='Inline String(\')',style='botones.TButton', command=lambda: convert_str(input_text_box,output_text_box,1))
inline_str_2 = ttk.Button(tool_bar,width=15,text='Inline String(\")',style='botones.TButton', command=lambda: convert_str(input_text_box,output_text_box,2))
ransack_or = ttk.Button(tool_bar,width=15,text='Ransack',style='botones.TButton', command=lambda: process_string(input_text_box, output_text_box,'',''))
remove_duplicates_button = ttk.Button(tool_bar,text='Eliminar duplicados',style='botones.TButton', command= lambda: remove_duplicates(input_text_box, output_text_box))
#Cadena para procesar en un AND o un OR
string_to_process_label = ttk.Label(tool_bar,text='Cadena a procesar',anchor='center')
string_to_process = ttk.Entry(tool_bar,width=10)
and_button = ttk.Button(tool_bar,width=15,text='AND',style='botones.TButton',command=lambda: process_string(input_text_box, output_text_box,string_to_process.get(),'AND'))
or_button = ttk.Button(tool_bar,width=15,text='OR',style='botones.TButton',command=lambda: process_string(input_text_box, output_text_box,string_to_process.get(),'OR'))



#Posicionamiento de botones.
avatar.grid(column=0,row=0,sticky=(W,N,E,S))
reset_button.grid(column=0,row=1,sticky=(W,E))
inline_sql.grid(column=0, row=2,sticky=(W))
ransack_or.grid(column=0, row=2,sticky=(E))
inline_str.grid(column=0, row=3,sticky=(W))
inline_str_2.grid(column=0, row=3,sticky=(E))

remove_duplicates_button.grid(column=0, row=5,sticky=(W,E))
string_to_process_label.grid(column=0, row=6,sticky=(W,E))
string_to_process.grid(column=0,row=7,sticky=(W,E))
and_button.grid(column=0, row=8,sticky=(W))
or_button.grid(column=0, row=8,sticky=(E))


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


frames = [PhotoImage(file='./Assets/mini_renegade.gif', format='gif -index %i'%(i)) for i in range(7)] 
 
def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == 7:
        ind = 0
    renegade.configure(image=frame)
    tool_bar.after(100, update, ind)
tool_bar.after(0, update, 0)

themes_bar = Label(mainframe)
themes_bar.configure(anchor='center')
themes_bar.grid(column=0,row=10,sticky=(N,E))
renegade = Label(themes_bar, image=frames[0])
#Temas

dark_theme = ttk.Button(themes_bar,text="Tema Oscuro", command=lambda: theme('dark'))
light_theme = ttk.Button(themes_bar,text="Tema Claro", command=lambda: theme('light'))

#Posicionamiento
dark_theme.grid(column=0, row=0,sticky=(W))
light_theme.grid(column=1, row=0,sticky=(E))
renegade.grid(column=3, row=0,sticky=(W))

for child in mainframe.winfo_children():
    child.grid_configure(padx=1,pady=1)


#Inicio
root.mainloop()