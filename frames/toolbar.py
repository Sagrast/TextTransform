from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
from PIL import ImageTk
from ttkthemes import themed_tk as tttk


class Toolbar(ttk.Frame):
    def __init__(self, mainframe, icon_image):
        super().__init__(mainframe)

        inputs_bar = ttk.Label(self)
        inputs_bar.grid(column=2, row=0, rowspan=50)
        # img
        img = icon_image.resize((260, 260))  # resize image
        self.icon = ImageTk.PhotoImage(img)  # convert image

        avatar = ttk.Label(self, image=self.icon)
        avatar.grid(column=0, row=0, sticky=(W, N, E, S))

        reset_button = ttk.Button(self, text="RESET", style='reset.TButton', command=lambda: reset(
            input_text_box, input_text_box2, output_text_box))
        inline_sql = ttk.Button(self, width=12, text='Inline Integer', style='botones.TButton',
                                command=lambda: in_line(input_text_box, output_text_box))
        inline_str = ttk.Button(self, width=12, text='Inline String(\')', style='botones.TButton',
                                command=lambda: convert_str(input_text_box, output_text_box, 1))
        inline_str_2 = ttk.Button(self, width=12, text='Inline String(\")', style='botones.TButton',
                                  command=lambda: convert_str(input_text_box, output_text_box, 2))
        ransack_or = ttk.Button(self, width=12, text='Ransack', style='botones.TButton',
                                command=lambda: process_string(input_text_box, output_text_box, '', ''))
        remove_duplicates_button = ttk.Button(self, text='Eliminar duplicados', style='botones.TButton',
                                              command=lambda: eliminar_duplicados(input_text_box, output_text_box))
        # Cadena para procesar en un AND o un OR
        string_to_process_label = ttk.Label(
            self, text='Cadena a procesar', anchor='center')
        string_to_process = ttk.Entry(self, width=10)
        and_button = ttk.Button(self, width=12, text='AND', style='botones.TButton', command=lambda: process_string(
            input_text_box, output_text_box, string_to_process.get(), 'AND'))
        or_button = ttk.Button(self, width=12, text='OR', style='botones.TButton', command=lambda: process_string(
            input_text_box, output_text_box, string_to_process.get(), 'OR'))
        # Nimbleset
        nimbleset_label = ttk.Label(
            self, text='Operaciones SET', anchor='center')
        xor_button = ttk.Button(self, width=12, text='XOR', style='botones.TButton', command=lambda: xor_function(
            input_text_box, input_text_box2, output_text_box, 'XOR'))
        union_button = ttk.Button(self, width=12, text='UNION', style='botones.TButton', command=lambda: xor_function(
            input_text_box, input_text_box2, output_text_box, 'UNION'))
        
        for child in self.winfo_children():
            child.grid_configure(ipadx=5, ipady=5)

        # Posicionamiento de botones.
        avatar.grid(column=0, row=0, sticky=(W, N, E, S), ipadx=0, ipady=0, padx=0,pady=0)
        reset_button.grid(column=0, row=1, sticky=(W, E),pady=0)
        inline_sql.grid(column=0, row=2, sticky=(W),pady=0)
        ransack_or.grid(column=0, row=2, sticky=(E),pady=0)
        inline_str.grid(column=0, row=3, sticky=(W),pady=0)
        inline_str_2.grid(column=0, row=3, sticky=(E),pady=0)
        # AND,OR
        remove_duplicates_button.grid(column=0, row=5, sticky=(W, E),pady=0)
        string_to_process_label.grid(column=0, row=6, sticky=(W, E),pady=0)
        string_to_process.grid(column=0, row=7, sticky=(W, E),pady=0)
        and_button.grid(column=0, row=8, sticky=(W),pady=0)
        or_button.grid(column=0, row=8, sticky=(E),pady=0)
        # NimbleSet
        nimbleset_label.grid(column=0, row=9, sticky=(W, E),pady=0)
        xor_button.grid(column=0, row=10, sticky=(W),pady=0)
        union_button.grid(column=0, row=10, sticky=(E),pady=0)

    # Creación de cajas de texto.
        # Input
        input_name_box = Label(inputs_bar)
        input_name_box.config(  # background="#00044A",
            # foreground="white",
            text='Entrada Principal',
            anchor="center",
            font=("Arial", 15),
        )
        input_text_box = scrolledtext.ScrolledText(inputs_bar)
        input_text_box.config(  # background="#00044A",
            # foreground="black",
            state="normal",
            width=50)
        # input2
        input_name_box2 = Label(inputs_bar)
        input_name_box2.config(  # background="#00044A",
            # foreground="white",
                                 text='Entrada Secundaria',
                                 anchor="center",
                                 font=("Arial", 15),
        )
        input_text_box2 = scrolledtext.ScrolledText(inputs_bar)
        input_text_box2.config(  # background="#00044A",
            # foreground="black",
                                 state="normal",
                                 width=50)
        # output
        output_name_box = Label(inputs_bar)
        output_name_box.config(  # background="#00044A",
            # foreground="white",
            text='Salida',
            anchor="center",
            font=('Arial', 15))
        output_text_box = scrolledtext.ScrolledText(inputs_bar)
        output_text_box.config(  # background="#00044A",
            # foreground="black",
            state="disabled",
            width=100)

        # posicionamiento de cajas de texto.
        input_text_box.grid(column=0, row=0, columnspan=1, sticky=(N, S))
        input_name_box.grid(column=0, row=4, columnspan=1,
                            sticky=(W, N, E, S), ipady=5)
        input_text_box2.grid(column=1, row=0, columnspan=1, sticky=(N, S))
        input_name_box2.grid(column=1, row=4, columnspan=1,
                             sticky=(W, N, E, S), ipady=5)

        # Outputs
        output_name_box.grid(column=0, row=10, columnspan=2,
                             sticky=(W, N, E, S), ipady=5)
        output_text_box.grid(column=0, row=5, columnspan=2,
                             rowspan=4, sticky=(W, N, E, S))
        
        
        ########################## METODOS DE CLASE #########################

        # Devuelve una lista igual a la original eliminando los duplicados.
        def eliminar_duplicados(input_widget, output_widget):

            if output_widget != 0:
                lines = input_widget.get("1.0", "end").strip().splitlines()

                lines = set(lines)
                lines = sorted(lines)
                text = list(lines)

                text = '\n'.join(lines)

                show_results(output_widget, text)

            else:
                # Convertir la lista a un conjunto para eliminar los elementos duplicados
                eliminar_duplicados = set(input_widget)
                eliminar_duplicados = sorted(eliminar_duplicados)
                # Convertir el conjunto de nuevo a una lista y devolverla
                return list(eliminar_duplicados)

        # Convierte una lista de lineas en una linea con cada dato entrecomillado y separado por comas.
        def convert_str(input_widget, output_widget, flag):
            # recoge los datos del widget de entrada y crea un array de un elemento por cada linea.
            lines = input_widget.get("1.0", "end").strip().splitlines()
            # llama a la función eliminar duplicados y recupera una lista de todos los elementos únicos del array.
            lines = eliminar_duplicados(lines, 0)
            # recorre el array creando una cadena de texto con el formato deseado.
            if flag == 1:
                lines = ['\'' + line + '\'' for line in lines]
                text = ','.join(lines)
                text = '(' + text + ')'
            else:
                lines = ['\"' + line + '\"' for line in lines]
                text = ','.join(lines)

            show_results(output_widget, text)

        # Recibe una lista de lineas y devuelve una cadena de texto con las lineas separadas por ','
        def in_line(input_widget, output_widget):

            lines = input_widget.get("1.0", "end").strip().splitlines()

            lines = eliminar_duplicados(lines, 0)
            lines = [line for line in lines]
            text = ','.join(lines)
            text = '(' + text + ')'

            show_results(output_widget, text)

        # Recibe una lista de lineas, una cadena que indica el string a concatenar y un flag que decide la estructura final a devolver.
        def process_string(input_widget, output_widget, chain, flag):

            lines = input_widget.get("1.0", "end").strip().splitlines()

            chain = chain.strip()

            lines = eliminar_duplicados(lines, 0)
            if flag == 'OR':  # Fomar Query
                text = ''
                count = 0
                for line in lines:
                    if count != 0:
                        text += ' OR ' + chain + f' LIKE \'%{line}%\''
                    else:
                        text += chain + f' LIKE \'%{line}%\''
                        count += 1
                text = '(' + text + ')'

            elif flag == 'AND':  # Fomar un AND :?
                text = ''
                count = 0
                for line in lines:
                    if count != 0:
                        text += ' AND ' + chain + f' LIKE \'%{line}%\''
                    else:
                        text += chain + f' LIKE \'%{line}%\''
                        count += 1
                text = '(' + text + ')'

            else:  # Ransack
                lines = [line for line in lines]
                text = ' OR '.join(lines)
                text = '(' + text + ')'

            show_results(output_widget, text)

        # Borrado de ambos paneles
        def reset(input_widget, input_widget2, output_widget):

            input_widget.delete("1.0", "end")
            input_widget2.delete("1.0", "end")

            output_widget.config(state='normal')
            output_widget.delete("1.0", "end")
            output_widget.config(state='disabled')

        def xor_function(input_widget, input_widget2, output_widget, flag):

            text1 = input_widget.get('1.0', 'end').strip().splitlines()
            text2 = input_widget2.get('1.0', 'end').strip().splitlines()

            if len(text1) != 0 and len(text2) != 0:
                if flag == 'XOR':

                    text1 = set(text1)
                    text2 = set(text2)

                    result = set(text1) - set(text2)
                    result = list(result)
                    text = '\n'.join(result)

                elif flag == 'UNION':
                    text1 = set(text1)
                    text2 = set(text2)

                    result = set(text1) & set(text2)
                    result = list(result)
                    text = '\n'.join(result)
            else:
                text = 'Debes de cubrir ambos campos de entrada para usar esta función.'

            show_results(output_widget, text)

        def show_results(output_widget, text):
           # Reactiva el widget de salida.
            output_widget.config(state="normal")
            # vacía el contenido que este tenga.
            output_widget.delete("1.0", "end")
            # Inserta el texto generado
            output_widget.insert("end", text)
            # Vuelve a deshabilitar el widgt de salida para evitar modificaciones accidentales
            output_widget.config(state="disabled")
