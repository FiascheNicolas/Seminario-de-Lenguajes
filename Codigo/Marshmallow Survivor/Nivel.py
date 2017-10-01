import pygame
import Malvavisco
import Chef
import Background
import Dulce
from random import randint
import threading


fincarga=False
#Colores
RED=(255,0,0)
BLACK=(0,0,0)

#Instancias
background=None
malvavisco=None
chef=None




#Variables de tipo pygame
spritesPrincipales = pygame.sprite.Group()
spriteBackground = pygame.sprite.Group()
clock = pygame.time.Clock()
spritesDulces = pygame.sprite.Group()
screen=None
ALTO=None
ANCHO=None


FPS=60
#Metodo para instancias los objetos del juego
def cargaDatos():
    background = Background.Background(0,0,1360,760)
    malvavisco = Malvavisco.Malvavisco(375,550,200,200)
    
    chef = Chef.Chef(500,0,250,250)
    
    spriteBackground.add(background)
    spritesPrincipales.add(malvavisco)
    spritesPrincipales.add(chef)
    global fincarga
    fincarga=True
   

#Metodo para dibujar Texto sobre pantalla
def draw_text(surf,text,size,x,y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,RED)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
    
#Metodo para cargar todas las instancias del juego     
def cargando():
    
    running=True
    global fincarga
    global screen
    global ALTO
    global ANCHO
    fincarga=False
    clock = pygame.time.Clock()
    clock.tick(60)
    i=0
    textCargando="Cargando"
    #CREO HILO PARA LA CARGA DE SPRITES
    hiloCargando = threading.Thread(target=cargaDatos)
    hiloCargando.start()
    ####
    while running:
       
        screen.fill(BLACK)
        
        if(i==100):
            textCargando="Cargando."
        if(i==300):
            textCargando="Cargando.."
        if(i==500):
            textCargando="Cargando..."
        if(i==600):
            i=0
        draw_text(screen,textCargando, 18, ALTO/2,ANCHO/2)
        
        i+=1
        
        if(fincarga==True):
            running=False
        pygame.display.flip()
        
        
         
         
        
         
        
        
       
    
    
        
def iniciar(screenMenu,alto,ancho):
    
    
    global screen
    screen = screenMenu
    global ALTO
    ALTO=alto
    global ANCHO
    ANCHO=ancho
    global clock
    global malvavisco
    cargando()
    
    pygame.init()
    pygame.mixer.init()
    
    pygame.display.set_caption("Marshmellow Survivor")
    clock = pygame.time.Clock()
    running = True
    
    
    
    
        
   
    
    
    
    listaDulces = []
    
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
                
    
        #hits = pygame.sprite.spritecollide(malvavisco, spritesDulces,False,pygame.sprite.collide_circle)
        #if hits:
           # print"BUendia"
          
            
            
        spriteBackground.draw(screen)
        spritesDulces.draw(screen)
        spritesPrincipales.draw(screen)
        spritesPrincipales.update()
        spritesDulces.update()
        pygame.display.flip()
        
