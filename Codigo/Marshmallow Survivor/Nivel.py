import pygame
import Malvavisco
import Chef
import Background
import Dulce
from random import randint
from pygame.constants import K_ESCAPE



FPS=60

def iniciar(screenMenu,ALTO,ANCHO):
    
    pygame.init()
    pygame.mixer.init()
    screen = screenMenu
    pygame.display.set_caption("Marshmellow Survivor")
    clock = pygame.time.Clock()
    running = True
    background=Background.Background(0,0,ALTO,ANCHO)
    malvavisco = Malvavisco.Malvavisco(375,550,200,200,running)
    chef = Chef.Chef(500,0,250,250)
    spritesPrincipales = pygame.sprite.Group()
    spritesPrincipales.add(malvavisco)
    spriteBackground = pygame.sprite.Group()
    spritesPrincipales.add(chef)
    spriteBackground.add(background)
    
    
    listaDulces = []
    spritesDulces = pygame.sprite.Group()
    while running:
        
        numeroRandom = randint(1, 20)
        if numeroRandom > 19:
            nuevoDulce = Dulce.Dulce()
            spritesDulces.add(nuevoDulce)
            listaDulces.append(nuevoDulce)
        clock.tick(FPS)
        
        for event in pygame.event.get():
           
            
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                
    
        spriteBackground.draw(screen)
        spritesDulces.draw(screen)
        spritesPrincipales.draw(screen)
        spritesPrincipales.update()
        spritesDulces.update()
        pygame.display.flip()
        
pygame.quit()     