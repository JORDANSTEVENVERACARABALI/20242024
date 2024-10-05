import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Crear la entrada para nuevas tareas
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task_event)

        # Crear el Listbox para mostrar las tareas
        self.task_list = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        # Botones para añadir, completar y eliminar tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Asignar eventos de teclado
        root.bind("<Escape>", self.close_app)
        root.bind("<Delete>", self.delete_task_event)
        root.bind("<c>", self.complete_task_event)

        # Listas de tareas pendientes y completadas
        self.pending_tasks = []
        self.completed_tasks = []

    # Añadir tarea
    def add_task(self):
        task = self.entry.get()
        if task:
            self.pending_tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def add_task_event(self, event):
        self.add_task()

    # Marcar tarea como completada
    def complete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            selected_task = self.task_list.get(selected_task_index)

            if selected_task in self.pending_tasks:
                self.task_list.itemconfig(selected_task_index, {'fg': 'green'})
                self.pending_tasks.remove(selected_task)
                self.completed_tasks.append(selected_task)
            else:
                messagebox.showwarning("Advertencia", "Esta tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea.")

    def complete_task_event(self, event):
        self.complete_task()

    # Eliminar tarea
    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            selected_task = self.task_list.get(selected_task_index)
            if selected_task in self.pending_tasks:
                self.pending_tasks.remove(selected_task)
            elif selected_task in self.completed_tasks:
                self.completed_tasks.remove(selected_task)
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea.")

    def delete_task_event(self, event):
        self.delete_task()

    # Cerrar aplicación con "Escape"
    def close_app(self, event):
        self.root.quit()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
