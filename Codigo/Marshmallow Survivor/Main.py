#13/09 Esqueleto de pygame
import pygame
import Malvavisco
import Chef
import Background
#CONSTANTES
WIDTH=900
HEIGHT=500
FPS=60
WHITE=(255,255,255)
BLACK=(0,0,0)


spritesPrincipales = pygame.sprite.Group()
#background=Background.Background(0,0,900,500)
malvavisco = Malvavisco.Malvavisco(0,-50000,100,100)
chef = Chef.Chef(100, 0, 300, 300)


#spritesPrincipales.add(background)
spritesPrincipales.add(malvavisco)
spritesPrincipales.add(chef)


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
    spritesPrincipales.update()
    
    
    #its=pygame.sprite.spritecollide(malvavisco,enemys, False)
    #if hits:
    #   running=False
    #Draws
    screen.fill(BLACK)
    
    spritesPrincipales.draw(screen)
    #despues de dibujar,flip the display
    pygame.display.flip()
 
pygame.quit()