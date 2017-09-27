import pygame
import Malvavisco
import Chef
import Background
import Dulce
from random import randint

#CONSTANTES
WIDTH=900
HEIGHT=500
FPS=60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
pygame.display.set_caption("Marshmallow Survivor")
clock = pygame.time.Clock()

background = Background.Background(0, 0, 1366, 768)
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
    
    numeroRandom = randint(1, 7)
    
    if numeroRandom > 6:
        nuevoDulce = Dulce.Dulce()
        spritesDulces.add(nuevoDulce)
        listaDulces.append(nuevoDulce)
    
    clock.tick(FPS)
    #Eventos
    for event in pygame.event.get():
        #chequear si se cierra la ventana
        if event.type==pygame.QUIT:
            running = False
    
    for sprite in spritesDulces:
        
        if sprite.y > 500:
            spritesDulces.delete(sprite)
    
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