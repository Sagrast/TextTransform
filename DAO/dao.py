def eliminar_duplicados(cadenas):
    # Convertir la lista a un conjunto para eliminar los elementos duplicados
    sin_duplicados = set(cadenas)
    sin_duplicados = sorted(sin_duplicados)
    # Convertir el conjunto de nuevo a una lista y devolverla
    return list(sin_duplicados)


def convert_str(input_widget,output_widget):
        
    text = input_widget.get("1.0", "end")
    lines = text.splitlines()
    
    lines = eliminar_duplicados(lines)   
    lines = ['\'' + line + '\'' for line in lines]    
    text = ','.join(lines)   
    
    
    output_widget.config(state="normal")
    output_widget.delete("1.0","end")
    output_widget.insert("end", text)
        
    output_widget.config(state="disabled")
    


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