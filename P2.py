
import tkinter as tk

ventana = tk.Tk()
ventana.title("Pelota rebotando")
ventana.geometry("600x400")

lienzo = tk.Canvas(ventana, width=600, height=400, bg="white")
lienzo.pack()

x = 100
y = 100
velocidad_x = 4
velocidad_y = 3
radio = 20

pelota = lienzo.create_oval(
    x-radio, y-radio, x+radio, y+radio,
    fill="red"
)

def mover_pelota():
    global x, y, velocidad_x, velocidad_y

    x = x + velocidad_x
    y = y + velocidad_y

    if x + radio >= 600 or x - radio <= 0:
        velocidad_x = -velocidad_x

    if y + radio >= 400 or y - radio <= 0:
        velocidad_y = -velocidad_y

    lienzo.move(pelota, velocidad_x, velocidad_y)

    ventana.after(16, mover_pelota)

mover_pelota()

ventana.mainloop()
