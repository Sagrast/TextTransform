def eliminar_duplicados(cadenas):
    # Convertir la lista a un conjunto para eliminar los elementos duplicados
    sin_duplicados = set(cadenas)
    sin_duplicados = sorted(sin_duplicados)
    # Convertir el conjunto de nuevo a una lista y devolverla
    return list(sin_duplicados)

#Convierte una lista de lineas en una linea con cada dato entrecomillado y separado por comas.
def convert_str(input_widget,output_widget):
    #recoge los datos del widget de entrada y crea un array de un elemento por cada linea.
    text = input_widget.get("1.0", "end")
    lines = text.splitlines()
    #llama a la función eliminar duplicados y recupera una lista de todos los elementos únicos del array.
    lines = eliminar_duplicados(lines)
    #recorre el array creando una cadena de texto con el formato deseado.   
    lines = ['\'' + line + '\'' for line in lines]    
    text = ','.join(lines)   
    
    #Reactiva el widget de salida.
    output_widget.config(state="normal")
    #vacía el contenido que este tenga.
    output_widget.delete("1.0","end")
    #Inserta el texto generado
    output_widget.insert("end", text)
    #Vuelve a deshabilitar el widgt de salida para evitar modificaciones accidentales        
    output_widget.config(state="disabled")
    

#Recibe una lista de lineas y devuelve una cadena de texto con las lineas separadas por ','
def in_line(input_widget,output_widget):    
    
    text = input_widget.get("1.0","end")
    lines = text.splitlines()
    
    lines = eliminar_duplicados(lines)
    lines = [line for line in lines]
    text = ','.join(lines)
    
    output_widget.config(state='normal')
    output_widget.delete("1.0","end")
    output_widget.insert('end',text)    
    output_widget.config(state='disabled')

#Recibe una lista de lineas y devuelve una cadena de texto con las lineas separadas por ' OR '    
def ransack_search(input_widget,output_widget):
    
    text = input_widget.get('1.0','end')
    lines = text.splitlines()
    
    lines = eliminar_duplicados(lines)
    lines = [line for line in lines]
    text = ' OR '.join(lines)
    
    output_widget.config(state='normal')
    output_widget.delete("1.0","end")
    output_widget.insert('end',text)    
    output_widget.config(state='disabled')