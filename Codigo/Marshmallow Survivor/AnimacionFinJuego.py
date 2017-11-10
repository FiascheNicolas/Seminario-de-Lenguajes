import pygame
PATH_WIN = "imagenes/FinalJuego/AnimacionWin/"
PATH_LOSE = "imagenes/FinalJuego/AnimacionLose/"
FINAL = 39
class AnimacionFinJuego(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho,WIN,LOSE):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.posWin = 0
        self.posLose = 0
        self.WIN=WIN
        self.LOSE=LOSE
        
        self.animacionWin = self.cargarAnimacion(FINAL, PATH_WIN)
        self.image = pygame.transform.scale(self.animacionWin[0], (self.alto, self.ancho))
        
        self.animacionLose = self.cargarAnimacion(FINAL,PATH_LOSE)
        self.image = pygame.transform.scale(self.animacionLose[0],(self.alto,self.ancho))
                
        
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x                      #Las posiciones x e y tienen que ser 0,0
        self.rect.y = y
    def update(self):
        if self.WIN:
            
            self.image = pygame.transform.scale(self.animacionWin[self.posWin],(self.alto,self.ancho))
            self.posWin +=1
            if(self.posWin==FINAL):
                self.posWin=0
        if self.LOSE:
            
            self.image = pygame.transform.scale(self.animacionLose[self.posLose],(self.alto,self.ancho))
            self.posLose +=1
            if(self.posLose==FINAL):
                self.posLose = 0
    def eliminarListas(self):
        
        
        del self.animacionWin[:]
        
        del self.animacionLose[:]
    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []

        while contador != cantidad +1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            contador += 1

        return listaAnimacion