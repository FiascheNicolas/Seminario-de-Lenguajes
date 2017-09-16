#13/09 Esqueleto de pygame
import pygame
import random
import Malvavisco


WIDTH=500
HEIGHT=500
FPS=60
# definir colores
WHITE=(255,255,255)
BLACK=(0,0,0)




all_sprites = pygame.sprite.Group()
player=Malvavisco.Malvavisco()

all_sprites.add(player)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Malvavisco")
clock = pygame.time.Clock()

# loop del juego

running =True
while running:
    #Correr a la velocidad correcta
    clock.tick(FPS)
    
    #Eventos
    for event in pygame.event.get():
        #chequear si se cierra la ventana
        if event.type==pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Draws
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    #despues de dibujar,flip the display
    pygame.display.flip()
 
pygame.quit()   
    
    
    