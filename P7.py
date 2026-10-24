
import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("Reloj")
ventana.geometry("500x250")
ventana.configure(bg="black")

reloj = tk.Label(
    ventana,
    text="",
    font=("Arial", 40),
    fg="#00FF64",
    bg="black"
)

reloj.pack(expand=True)

def actualizar_reloj():
    hora = time.strftime("%I:%M:%S %p").lstrip("0")
    reloj.config(text=hora)
    ventana.after(1000, actualizar_reloj)

actualizar_reloj()

ventana.mainloop()
