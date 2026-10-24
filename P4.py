
import tkinter as tk

ventana = tk.Tk()
ventana.title("Boton")
ventana.geometry("600x400")
ventana.configure(bg="#F0F0F0")

color = "#0096FF"

def cambiar_color():
    global color

    if color == "#0096FF":
        color = "#00C850"
    else:
        color = "#0096FF"

    boton.configure(bg=color)

boton = tk.Button(
    ventana,
    text="PULSE AQUI",
    font=("Arial", 16),
    bg=color,
    fg="white",
    command=cambiar_color,
    width=15,
    height=2
)

boton.place(x=200, y=150, width=200, height=80)

ventana.mainloop()
