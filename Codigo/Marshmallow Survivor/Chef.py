import pygame
IDLE = 10
ATACK=10
PATH_IDLE = "imagenes/AnimacionesChef/Idle/"
PATH_ATACK = "imagenes/AnimacionesChef/atack/"
class Chef(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.idle = True
        self.animacionIdle = self.cargarAnimacion(IDLE,PATH_IDLE)
        self.animacionAtack = self.cargarAnimacion(ATACK, PATH_ATACK)
        self.alto = alto
        self.ancho = ancho
        self.posIdle = 0
        self.posAtack=0
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inversa = False

        
        self.attacking =True
        
        self.delayIdle = 0
        self.delayAtack = 0
        
    
    


    def cargarAnimacionIdle(self):
        contador = 1
        listaAnimacionIdleChef = []
        while contador != 32:
            listaAnimacionIdleChef.append(pygame.image.load("imagenes/AnimacionesChef/Idle/" + str(contador) + ".png").convert_alpha())
            contador += 1

        return listaAnimacionIdleChef


    def update(self, *args):
        
        
        if not self.attacking:
            self.actualizarIdle()
        else:
            self.actualizarAtack()
            
            
    def actualizarAtack(self):
        self.image = pygame.transform.scale(self.animacionAtack[self.posAtack], (self.alto, self.ancho))
        
        self.delayAtack += 1   
        if(self.delayAtack == 5): 
            self.delayAtack = 0
            self.posAtack +=1
            if (self.posAtack == ATACK):
                self.posAtack=0
    def actualizarIdle(self):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))

        
        self.delayIdle += 1   
        if(self.delayIdle == 4): 
            self.delayIdle = 0
            self.posIdle +=1
            if (self.posIdle == IDLE +1):
                self.posIdle=0
    
    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []
        while contador != cantidad + 1:
            
            
            #listaAnimacion.append(imagen.subsurface(0,0,1040,721))
            #istaAnimacion.append(pygame.image.load(path + str(contador) + ".png").subsurface(0,0,0,0))
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            #listaAnimacion.append(pygame.image.load("imagenes/testeo.png").convert_alpha())
            
           
            
            
            contador += 1
        
        return listaAnimacion    
        
        

