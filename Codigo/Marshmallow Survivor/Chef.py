import pygame
import LifeBar
IDLE = 29
ATACK=38
PATH_IDLE = "imagenes/AnimacionesChef/Idle/"
PATH_ATACK = "imagenes/AnimacionesChef/atack/"
RED=(255,0,0)

class Chef(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        #Settings
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.posIdle = 0
        self.posAtack=0
        self.vidas = 4



        #
        #Carga de animaciones
        self.animacionIdle = self.cargarAnimacion(IDLE,PATH_IDLE)
        self.animacionAtack = self.cargarAnimacion(ATACK, PATH_ATACK)
        #
        #Booleanos
        self.idle = True
        self.inversa = False
        self.attacking = False
        self.throwingFireball = False
        #
        #Configurables
        self.delayIdle = 0
        self.delayAtack = 0
        #
        #Settings de sprite
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/8)
        pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x = x
        self.rect.y = y

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
        self.posAtack += 1

        if (self.posAtack == ATACK):
            self.posAtack = 0
            self.attacking = False
            self.throwingFireball = False

        if (self.posAtack == ATACK - 7):
            self.throwingFireball = True

    def actualizarIdle(self):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.posIdle += 1
        if (self.posIdle == IDLE +1):
            self.posIdle = 0

    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []
        while contador != cantidad + 1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            contador += 1

        return listaAnimacion
    def dropListas(self):
        del self.animacionAtack[:]
        del self.animacionIdle[:]