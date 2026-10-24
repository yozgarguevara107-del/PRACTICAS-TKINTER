import pygame

pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Semaforo")

reloj = pygame.time.Clock()
colores = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
indice = 0
tiempo = 0
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    tiempo += 1
    if tiempo >= 120:
        indice = (indice + 1) % 3
        tiempo = 0

    ventana.fill((220, 220, 220))
    pygame.draw.rect(ventana, (40, 40, 40), (140, 40, 120, 320))

    for i in range(3):
        color = colores[i] if i == indice else (70, 70, 70)
        pygame.draw.circle(ventana, color, (200, 100 + i * 100), 35)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
