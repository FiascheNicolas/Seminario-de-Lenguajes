import pygame
import Malvavisco
import Chef
import Background
import Dulce
from random import randint

#CONSTANTES
ALTO=1360
ANCHO=768
FPS=60

pygame.init()
pygame.mixer.init()
#screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
screen = pygame.display.set_mode((ALTO, ANCHO))
pygame.display.set_caption("Marshmallow Survivor")
clock = pygame.time.Clock()

background = Background.Background(0, 0, ALTO, ANCHO)
malvavisco = Malvavisco.Malvavisco(375, 550, 200, 200)
chef = Chef.Chef(500, 0, 250, 250)
spritesPrincipales = pygame.sprite.Group()
spriteBackground = pygame.sprite.Group()
spritesPrincipales.add(malvavisco)
spritesPrincipales.add(chef)
spriteBackground.add(background)

#background = pygame.image.load("imagenes/fondo.jpg").convert_alpha()
# loop del juego

running = True
listaDulces = []
spritesDulces = pygame.sprite.Group()

while running:
    #Correr a la velocidad correcta
    
    numeroRandom = randint(1, 20)
    
    if numeroRandom > 19:
        nuevoDulce = Dulce.Dulce()
        spritesDulces.add(nuevoDulce)
        listaDulces.append(nuevoDulce)
    
    clock.tick(FPS)
    #Eventos
    for event in pygame.event.get():
        #chequear si se cierra la ventana
        if event.type==pygame.QUIT:
            running = False
    #Update
    #its=pygame.sprite.spritecollide(malvavisco,enemys, False)
    #if hits:
    #   running=False
    #Draws

    spriteBackground.draw(screen)
    spritesDulces.draw(screen)
    spritesPrincipales.draw(screen)
    spritesPrincipales.update()
    spritesDulces.update()
    #despues de dibujar,flip the display
    pygame.display.flip()
 
pygame.quit()