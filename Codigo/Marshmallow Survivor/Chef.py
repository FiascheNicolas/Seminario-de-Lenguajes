import pygame

class Chef(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.idle = True
        self.animacionIdle = self.cargarAnimacionIdle()
        self.alto = 500
        self.ancho = 400
        self.posIdle = 0
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.rect = self.image.get_rect()
        self.rect.center=(x/2, y/2) # instancio la imagen en el centro de la pantalla
        self.posactual=self.rect.y
        self.inversa = False
        
    def cargarAnimacionIdle(self):
        contador = 1
        listaAnimacionIdleChef = []
        while contador !=32:
            listaAnimacionIdleChef.append(pygame.image.load("imagenes/AnimacionesChef/Idle/" + str(contador) + ".png"))
            contador += 1
            
        return listaAnimacionIdleChef
    
    def update(self, *args):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        
        if self.posIdle == 30:
            self.inversa = True
        elif self.posIdle == 1:
            self.inversa = False
            
        if self.inversa:
            self.posIdle -= 1
        else:
            self.posIdle += 1
            
        
        
        