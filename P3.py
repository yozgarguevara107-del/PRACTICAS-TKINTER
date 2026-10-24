
import tkinter as tk

ventana = tk.Tk()
ventana.title("MOVER CUADRADO")
ventana.geometry("600x400")

lienzo = tk.Canvas(ventana, width=600, height=400, bg="#E6E6E6")
lienzo.pack()

x = 280
y = 180
velocidad = 5

cuadrado = lienzo.create_rectangle(
    x, y, x + 40, y + 40,
    fill="red"
)

def mover(evento):
    global x, y

    if evento.keysym == "Left":
        x -= velocidad
    elif evento.keysym == "Right":
        x += velocidad
    elif evento.keysym == "Up":
        y -= velocidad
    elif evento.keysym == "Down":
        y += velocidad

    x = max(0, min(x, 560))
    y = max(0, min(y, 360))

    lienzo.coords(cuadrado, x, y, x + 40, y + 40)

ventana.bind("<KeyPress>", mover)
ventana.mainloop()
