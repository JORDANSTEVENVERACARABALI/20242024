import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

# Función para marcar una tarea como completada
def mark_task_completed():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        completed_task = f"[Completada] {task}"
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, completed_task)
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Crear el campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Asociar la tecla Enter con la función add_task
task_entry.bind("<Return>", add_task)

# Botón para añadir tarea
add_task_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_task_button.grid(row=0, column=1, padx=10)

# Crear el Listbox para mostrar las tareas
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tarea como completada
mark_task_button = tk.Button(root, text="Marcar como Completada", command=mark_task_completed)
mark_task_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Botón para eliminar tarea
delete_task_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_task_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Iniciar el bucle de eventos
root.mainloop()
