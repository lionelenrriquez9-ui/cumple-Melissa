import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    nombre = entrada.get()
    
    mensaje = f"""
¡Feliz cumpleaños, {nombre}! 

Espero que hayas tenido un día maravilloso
lleno de alegría y momentos especiales.

Perdón por no decírtelo antes,
pero te deseo exitos meli siendo sincero.
te quiero mucho
"""
    
    messagebox.showinfo("Mensaje de Cumpleaños", mensaje)

# Crear ventana
ventana = tk.Tk()
ventana.title("Feliz Cumpleaños 🎂")
ventana.geometry("300x150")

# Texto
label = tk.Label(ventana, text="Ingresa el nombre:")
label.pack(pady=5)

# Caja de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

# Ejecutar app
ventana.mainloop()