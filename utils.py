from tkinter import *
#Importar pillow para que tkinter soporte mas formatos de imágenes.
from PIL import Image, ImageTk
from DAO.dao import *

root = Tk()
root.title('Utils')
root.config(bg='LightBlue2')

#frames

left_frame = Frame(root, width=200,height=400)
left_frame.rowconfigure(0, weight=1)
left_frame.columnconfigure(0, weight=1)
left_frame.grid(row=0, column=0,padx=10,pady=5)


right_frame = Frame(root, width=650,height=400,bg='grey')
right_frame.grid(row=0, column=1,padx=10,pady=5)


#img
image = Image.open('./Assets/icon.jpg') #Open image
img = image.resize((150,150)) #resize image
icon = ImageTk.PhotoImage(img) #convert image
Label(left_frame,image=icon).grid(row=0,column=0,padx=5,pady=5)

#Pendiente, frames entrada y salida.


#Tool bar

tool_bar = Frame(left_frame, width=180,height=185,bg='purple')
tool_bar.grid(row=2, column=0,padx=5,pady=5)
#Label(left_frame,text="Example test").grid(row=1,column=0,padx=5,pady=5)

#Etiquetas que contienen otras cosas.

Label(tool_bar, text="Herramientas",relief=RAISED).grid(row=0,column=0,padx=5,pady=5)

#Input Texto.

input_label = Label(right_frame, text="Entrada", bg='#878787', fg='black')
input_label.pack(side='top')

input_text = Text(right_frame)
input_text.place(x=0,y=0,width=200,height=400)
input_text.config(state='normal',bg='#878787',fg='black')
input_text.pack(fill='both',expand=1,side='top')

output_label = Label(right_frame, text="Salida",bg='#878787',fg='black')
output_label.pack(side='top')

output_text = Text(right_frame)
output_text.place(x=0,y=100,width=200,height=400)
output_text.config(state='disabled',bg='#878787',fg='black')
output_text.pack(fill='both',expand=1,side='bottom')

#output_text.icursor(0)

#Botones
Button(tool_bar, text='Eliminar Duplicados',relief='groove', command=lambda: in_line(input_text,output_text) ).grid(row=1,column=0,padx=5,pady=5)
Button(tool_bar, text="Convertir STR SQL",relief='groove', command=lambda: convert_str(input_text,output_text)).grid(row=2,column=0,padx=5,pady=5)
Button(tool_bar, text="Busqueda Ransack",relief='groove', command=lambda: ransack_search(input_text,output_text)).grid(row=3,column=0,padx=5,pady=5)




root.mainloop()