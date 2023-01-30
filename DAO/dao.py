#def eliminar_duplicados(cadenas):
    # Convertir la lista a un conjunto para eliminar los elementos duplicados    
#    sin_duplicados = set(cadenas)
#    sin_duplicados = sorted(sin_duplicados)
    # Convertir el conjunto de nuevo a una lista y devolverla
#    return list(sin_duplicados)

    
#Devuelve una lista igual a la original eliminando los duplicados.
def eliminar_duplicados(input_widget,output_widget):
   
    
    if output_widget != 0:
        lines = input_widget.get("1.0","end").strip().splitlines()
    
        lines = set(lines)    
        lines = sorted(lines)
        text = list(lines)
        
        text = '\n'.join(lines)    
          
        show_results(output_widget,text)
 
        
    else:
        # Convertir la lista a un conjunto para eliminar los elementos duplicados            
        eliminar_duplicados = set(input_widget)
        eliminar_duplicados = sorted(eliminar_duplicados)
        # Convertir el conjunto de nuevo a una lista y devolverla
        return list(eliminar_duplicados)

#Convierte una lista de lineas en una linea con cada dato entrecomillado y separado por comas.
def convert_str(input_widget,output_widget,flag):
    #recoge los datos del widget de entrada y crea un array de un elemento por cada linea.    
    lines = input_widget.get("1.0", "end").strip().splitlines()
    #llama a la función eliminar duplicados y recupera una lista de todos los elementos únicos del array.
    lines = eliminar_duplicados(lines,0)
    #recorre el array creando una cadena de texto con el formato deseado.
    if flag == 1:   
        lines = ['\'' + line + '\'' for line in lines]    
        text = ','.join(lines)
        text = '(' + text + ')'
    else:
        lines = ['\"' + line + '\"' for line in lines]    
        text = ','.join(lines)   
      
    show_results(output_widget,text)
        
 

#Recibe una lista de lineas y devuelve una cadena de texto con las lineas separadas por ','
def in_line(input_widget,output_widget):  
        
    lines = input_widget.get("1.0","end").strip().splitlines()
    
    lines = eliminar_duplicados(lines,0)
    lines = [line for line in lines]
    text = ','.join(lines)
    text = '(' + text + ')'
    
    show_results(output_widget,text)
 
    
#Recibe una lista de lineas, una cadena que indica el string a concatenar y un flag que decide la estructura final a devolver.
def process_string(input_widget,output_widget,chain,flag):    
    
    lines = input_widget.get("1.0","end").strip().splitlines()
    
    chain = chain.strip()
    
    lines = eliminar_duplicados(lines,0)
    if flag == 'OR':  #Fomar Query      
        text = ''
        count = 0        
        for line in lines:
            if count != 0:
                text += ' OR ' + chain + f' LIKE \'%{line}%\''
            else:
                text += chain + f' LIKE \'%{line}%\''
                count+=1            
        text = '(' + text + ')'
        
    elif flag == 'AND': #Fomar un AND :?
        text = ''
        count = 0        
        for line in lines:
            if count != 0:
                text += ' AND ' + chain + f' LIKE \'%{line}%\''
            else:
                text += chain + f' LIKE \'%{line}%\''
                count+=1            
        text = '(' + text + ')'
        
    else:        #Ransack
        lines = [line for line in lines]
        text = ' OR '.join(lines)         
        text = '(' + text + ')'
    
    show_results(output_widget,text)
 

#Borrado de ambos paneles
def reset(input_widget,input_widget2,output_widget):
    
    input_widget.delete("1.0","end")
    input_widget2.delete("1.0","end")
    
    output_widget.config(state='normal')
    output_widget.delete("1.0","end")    
    output_widget.config(state='disabled')


def xor_function(input_widget,input_widget2,output_widget,flag):
    
    text1 = input_widget.get('1.0','end').strip().splitlines()
    text2 = input_widget2.get('1.0','end').strip().splitlines()
    
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
  
    show_results(output_widget,text)
 
    
def show_results(output_widget,text):
   #Reactiva el widget de salida.
    output_widget.config(state="normal")
    #vacía el contenido que este tenga.
    output_widget.delete("1.0","end")
    #Inserta el texto generado
    output_widget.insert("end", text)
    #Vuelve a deshabilitar el widgt de salida para evitar modificaciones accidentales        
    output_widget.config(state="disabled")
    