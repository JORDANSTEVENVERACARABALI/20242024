import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar():
    info = entry_text.get()
    if info:
        listbox.insert(tk.END, info)
        entry_text.delete(0, tk.END)

# Función para limpiar la lista y el campo de texto
def limpiar():
    entry_text.delete(0, tk.END)
    listbox.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de GUI")

# Crear y colocar una etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Crear y colocar un campo de texto
entry_text = tk.Entry(ventana, width=50)
entry_text.pack(pady=5)

# Crear y colocar un botón "Agregar"
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

# Crear y colocar un botón "Limpiar"
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# Crear y colocar una lista para mostrar los datos
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
