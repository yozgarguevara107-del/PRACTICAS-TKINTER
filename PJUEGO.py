
import tkinter as tk
import random
import math
import time

ANCHO = 800
ALTO = 600

ventana = tk.Tk()
ventana.title("ZOMBIE ATTACK")
ventana.resizable(False, False)

pantalla = tk.Canvas(
    ventana, width=ANCHO, height=ALTO,
    bg="#121419", highlightthickness=0
)
pantalla.pack()

NEGRO = "#121419"
BLANCO = "white"
VERDE = "#3CDC5A"
ROJO = "#F0323C"
AZUL = "#3C96FF"
AMARILLO = "#FFDC32"

fuente = ("Arial", 16, "bold")
titulo = ("Arial", 42, "bold")

teclas = set()
jugador = [ANCHO / 2, ALTO / 2]
zombis = []
balas = []
puntos = 0
vidas = 3
terminado = False
siguiente_zombi = 0


def reiniciar():
    global jugador, zombis, balas
    global puntos, vidas, terminado, siguiente_zombi

    jugador = [ANCHO / 2, ALTO / 2]
    zombis = []
    balas = []
    puntos = 0
    vidas = 3
    terminado = False
    siguiente_zombi = time.time() + 1
    teclas.clear()
    actualizar()


def tecla_presionada(evento):
    global terminado

    tecla = evento.keysym.lower()

    if tecla == "escape":
        ventana.destroy()
        return

    if terminado and tecla == "r":
        reiniciar()
        return

    teclas.add(tecla)


def tecla_soltada(evento):
    teclas.discard(evento.keysym.lower())


def disparar(evento):
    if terminado:
        return

    dx = evento.x - jugador[0]
    dy = evento.y - jugador[1]
    distancia = math.hypot(dx, dy)

    if distancia > 0:
        dx = dx / distancia
        dy = dy / distancia

        balas.append([
            jugador[0], jugador[1],
            dx * 9, dy * 9
        ])


def crear_zombi():
    lado = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if lado == "arriba":
        return [random.randint(0, ANCHO), -20]
    elif lado == "abajo":
        return [random.randint(0, ANCHO), ALTO + 20]
    elif lado == "izquierda":
        return [-20, random.randint(0, ALTO)]
    else:
        return [ANCHO + 20, random.randint(0, ALTO)]


def distancia(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)


def actualizar():
    global puntos, vidas, terminado, siguiente_zombi

    if not terminado:
        # Mover al jugador
        dx = 0
        dy = 0

        if "left" in teclas or "a" in teclas:
            dx -= 1
        if "right" in teclas or "d" in teclas:
            dx += 1
        if "up" in teclas or "w" in teclas:
            dy -= 1
        if "down" in teclas or "s" in teclas:
            dy += 1

        if dx != 0 or dy != 0:
            distancia_movimiento = math.hypot(dx, dy)
            jugador[0] += dx / distancia_movimiento * 4
            jugador[1] += dy / distancia_movimiento * 4

        jugador[0] = max(20, min(ANCHO - 20, jugador[0]))
        jugador[1] = max(20, min(ALTO - 20, jugador[1]))

        # Crear zombis
        ahora = time.time()

        if ahora >= siguiente_zombi:
            zombis.append(crear_zombi())
            siguiente_zombi = ahora + max(
                0.3, (1100 - puntos * 15) / 1000
            )

        # Mover balas
        for bala in balas[:]:
            bala[0] += bala[2]
            bala[1] += bala[3]

            if (bala[0] < 0 or bala[0] > ANCHO or
                    bala[1] < 0 or bala[1] > ALTO):
                balas.remove(bala)

        # Mover zombis
        for zombi in zombis[:]:
            dx = jugador[0] - zombi[0]
            dy = jugador[1] - zombi[1]
            distancia_zombi = math.hypot(dx, dy)

            if distancia_zombi > 0:
                velocidad = 1.2 + min(puntos * 0.01, 1.5)
                zombi[0] += dx / distancia_zombi * velocidad
                zombi[1] += dy / distancia_zombi * velocidad

            # Si toca al jugador
            if distancia(
                jugador[0], jugador[1],
                zombi[0], zombi[1]
            ) < 28:
                zombis.remove(zombi)
                vidas -= 1

                if vidas <= 0:
                    terminado = True
                    break

        # Detectar balas contra zombis
        for bala in balas[:]:
            for zombi in zombis[:]:
                if distancia(
                    bala[0], bala[1],
                    zombi[0], zombi[1]
                ) < 23:
                    zombis.remove(zombi)

                    if bala in balas:
                        balas.remove(bala)

                    puntos += 1
                    break

    # Dibujar escenario
    pantalla.delete("all")

    for x in range(20, ANCHO, 40):
        for y in range(20, ALTO, 40):
            pantalla.create_oval(
                x - 2, y - 2, x + 2, y + 2,
                fill="#23262B", outline=""
            )

    # Dibujar jugador
    x, y = jugador

    pantalla.create_oval(
        x - 18, y - 18, x + 18, y + 18,
        fill=AZUL, outline=""
    )

    pantalla.create_oval(
        x + 1, y - 9, x + 9, y - 1,
        fill=BLANCO, outline=""
    )

    # Dibujar zombis
    for x, y in zombis:
        pantalla.create_oval(
            x - 17, y - 17, x + 17, y + 17,
            fill=VERDE, outline=""
        )

        pantalla.create_oval(
            x - 8, y - 6, x - 2, y,
            fill=ROJO, outline=""
        )

        pantalla.create_oval(
            x + 2, y - 6, x + 8, y,
            fill=ROJO, outline=""
        )

    # Dibujar balas
    for bala in balas:
        pantalla.create_oval(
            bala[0] - 5, bala[1] - 5,
            bala[0] + 5, bala[1] + 5,
            fill=AMARILLO, outline=""
        )

    # Mostrar puntos, vidas y zombis
    pantalla.create_text(
        15, 15, anchor="nw",
        text="PUNTOS: " + str(puntos),
        fill=BLANCO, font=fuente
    )

    pantalla.create_text(
        15, 50, anchor="nw",
        text="VIDAS: " + str(vidas),
        fill=ROJO, font=fuente
    )

    pantalla.create_text(
        15, 85, anchor="nw",
        text="ZOMBIS: " + str(len(zombis)),
        fill=VERDE, font=fuente
    )

    # Pantalla de Game Over
    if terminado:
        pantalla.create_rectangle(
            140, 190, 660, 410,
            fill="#1E1E28", outline=BLANCO
        )

        pantalla.create_text(
            400, 240, text="GAME OVER",
            fill=ROJO, font=titulo
        )

        pantalla.create_text(
            400, 300,
            text="Puntuacion: " + str(puntos),
            fill=BLANCO, font=fuente
        )

        pantalla.create_text(
            400, 355,
            text="Pulsa R para volver a jugar",
            fill=AMARILLO, font=fuente
        )

    ventana.after(16, actualizar)


ventana.bind("<KeyPress>", tecla_presionada)
ventana.bind("<KeyRelease>", tecla_soltada)
pantalla.bind("<Button-1>", disparar)

reiniciar()
ventana.mainloop()
