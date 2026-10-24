
import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Lluvia de estrellas")
ventana.geometry("600x400")

lienzo = tk.Canvas(
    ventana,
    width=600,
    height=400,
    bg="#000019",
    highlightthickness=0
)
lienzo.pack()

estrellas = []

for i in range(40):
    x = random.randint(0, 600)
    y = random.randint(0, 400)

    estrella = lienzo.create_oval(
        x, y, x + 4, y + 4,
        fill="white",
        outline="white"
    )

    estrellas.append([x, y, estrella])

def mover_estrellas():
    for estrella in estrellas:
        estrella[1] += 3

        if estrella[1] > 400:
            estrella[0] = random.randint(0, 596)
            estrella[1] = 0

        lienzo.coords(
            estrella[2],
            estrella[0],
            estrella[1],
            estrella[0] + 4,
            estrella[1] + 4
        )

    ventana.after(16, mover_estrellas)

mover_estrellas()

ventana.mainloop()
