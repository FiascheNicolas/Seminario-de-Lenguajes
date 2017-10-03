import pygame
import Malvavisco
import Chef
import Background
import Dulce
import Fireball
from random import randint

#import Background


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
pygame.mixer.music.load("Sonidos/Alone.mp3")

background = Background.Background(0, 0, ALTO, ANCHO)
malvavisco = Malvavisco.Malvavisco(375, 550, 200, 200)
chef = Chef.Chef(500, 0, 250, 250)

spritesPrincipales = pygame.sprite.Group()
spriteBackground = pygame.sprite.Group()
spriteFireball = pygame.sprite.Group()      #FIREBALL
spritesPrincipales.add(malvavisco)
spritesPrincipales.add(chef)
spriteBackground.add(background)

#background = pygame.image.load("imagenes/fondo.jpg").convert_alpha()
# loop del juego

running = True
listaDulces = []
spritesDulces = pygame.sprite.Group()
pygame.mixer.music.play(-1)

while running:
    #Correr a la velocidad correcta
    
    numeroRandom = randint(1, 20)
    
    if numeroRandom > 19:
        nuevoDulce = Dulce.Dulce()
        spritesDulces.add(nuevoDulce)
        listaDulces.append(nuevoDulce)
        
    nRandom = randint(1,200)
    if nRandom > 199:
        fireball = Fireball.Fireball(500, 0, 200, 200,malvavisco.rect.x,malvavisco.rect.y)
        spriteFireball.add(fireball)
        
    
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
    spriteFireball.draw(screen)
    spritesPrincipales.update()
    spritesDulces.update()    
    spriteFireball.update()
    #despues de dibujar,flip the display
    pygame.display.flip()
 
pygame.quit()