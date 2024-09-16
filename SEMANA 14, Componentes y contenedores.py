import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_eventos = tk.Frame(root)
        self.frame_eventos.pack(pady=10)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para los campos de entrada
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=20)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(self.frame_entrada, date_pattern='y-mm-dd')
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
        self.time_entry = tk.Entry(self.frame_entrada)
        self.time_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # Botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=5)
        tk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

        # Lista de eventos (en memoria)
        self.eventos = []

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not self.validar_hora(hora):
            messagebox.showerror("Error", "La hora debe tener el formato HH:MM.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})

        # Limpiar los campos
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Debe seleccionar un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)

    def validar_hora(self, hora):
        try:
            datetime.datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
