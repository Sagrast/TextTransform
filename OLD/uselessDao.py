def ransack_search(input_widget,output_widget):
    
    text = input_widget.get('1.0','end')
    lines = text.strip().splitlines()
    
    lines = eliminar_duplicados(lines)
    lines = [line for line in lines]
    text = ' OR '.join(lines)
    
    output_widget.config(state='normal')
    output_widget.delete("1.0","end")
    output_widget.insert('end',text)    
    output_widget.config(state='disabled')