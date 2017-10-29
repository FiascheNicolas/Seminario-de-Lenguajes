import pygame

#CONSTANTES

RUN = 16 #35
IDLE = 18 #39
JUMP = 1 #1
ROCK = 11 #22

PATH_RUN = "imagenes/AnimacionesMalvavisco/Run/"
PATH_IDLE = "imagenes/AnimacionesMalvavisco/Idle/"
PATH_JUMP = "imagenes/AnimacionesMalvavisco/Jump/"
PATH_JUMP_DOWN = "imagenes/AnimacionesMalvavisco/JumpDown/"
PATH_THROW_ROCK = "imagenes/AnimacionesMalvavisco/ThrowRock/"
PATH_IDLE_ROCK = "imagenes/AnimacionesMalvavisco/IdleRock/"
PATH_RUN_ROCK = "imagenes/AnimacionesMalvavisco/RunRock/"
RED=(255,0,0)

pygame.mixer.init()
class Malvavisco(pygame.sprite.Sprite):
    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.posRun = 0
        self.posIdle = 0
        self.posJump = 0
        self.posThrowRock=0
        #
        #Booleanos
        self.run = False
        self.idle = True
        self.derecha = True
        self.salto = False
        self.limite = False
        self.rock = False        #tengo la piedra en la mano?
        self.throwing = False    #estoy tirando la piedra?
        #
        #Configurables
        self.alto = alto
        self.ancho = ancho
        self.velocidad = 3
        self.distanciaSalto = 100
        self.delayIdle = 0
        self.delayIdleInvertido = 0
        self.delayRun = 0
        self.delayRunInvertido = 0
        self.delayIdleRock = 0
        self.delayIdleRockInvertido = 0
        self.delayRunRock = 0
        self.delayRunRockInvertido = 0
        self.delayThrowRock = 0
        self.delayThrowRockInvertido = 0
        #
        #Carga de animaciones y recursos
        self.animacionRun = self.cargarAnimacion(RUN, PATH_RUN)
        self.animacionIdle = self.cargarAnimacion(IDLE, PATH_IDLE)
        self.animacionJump = pygame.image.load( PATH_JUMP + "0.png").convert_alpha()
        self.animacionJumpDown = pygame.image.load(PATH_JUMP_DOWN + "0.png").convert_alpha()
        self.animacionThrowRock = self.cargarAnimacion(ROCK, PATH_THROW_ROCK)
        self.animacionIdleRock = self.cargarAnimacion(IDLE, PATH_IDLE_ROCK)
        self.animacionRunRock = self.cargarAnimacion(RUN, PATH_RUN_ROCK)
        self.sonidoSalto = pygame.mixer.Sound("Sonidos/Salto.ogg")
        #
        #Imagen, primera posicion, configuracion de imagen para colision
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/8)
        pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x = x
        self.rect.y = y
        self.posactual = self.rect.y

    def update(self, *args):
        key=pygame.key.get_pressed() #detecto que tecla estoy presionando

        if key[pygame.K_ESCAPE]:
            self.runningGame=False

        if key[pygame.K_w] and self.rect.y == self.posactual:
            self.salto = True
            if self.rock == False:
                self.sonidoSalto.play()

        if key[pygame.K_d]:
            self.derecha = True
            self.run = True
            if(self.rect.x<1247):
                self.rect.x += self.velocidad + 1

        if key[pygame.K_a]:
            self.derecha=False
            self.run=True
            if(self.rect.x>-61):
                self.rect.x -=self.velocidad

        if not self.rock:                   # Si no tengo una piedra en la mano#
            if not self.salto:              # si no estoy saltando#
                if self.derecha:            # si esta mirando a la derecha#
                    if self.idle:
                        self.actualizarIdle()
                    if self.run:
                        self.actualizarRun()
                        if(not key[pygame.K_d]):
                            self.run=False
                else: #Si esta mirando a la izquierda#
                    if self.idle:
                        self.actualizarIdleInvertida()
                    if self.run:
                        self.actualizarRunInvertida()
                        if(not key[pygame.K_d]):
                            self.run=False

            else: #Si estoy saltando
                if self.derecha: # Si salto y miro para la derecha

                    if(self.rect.y>self.posactual-100) and self.limite==False:
                        self.rect.y -=5
                        self.actualizarJump()

                    elif(self.rect.y!=self.posactual):
                        self.limite=True
                        self.rect.y += 5
                        self.actualizarJumpDown()
                    if(self.rect.y==self.posactual):
                        self.limite=False
                        self.salto=False

                else: #Si salto y miro para la izquierda
                    if(self.rect.y>self.posactual-self.distanciaSalto) and self.limite==False:
                        self.rect.y -=5
                        self.actualizarJumpInvertido()

                    elif(self.rect.y!=self.posactual):
                        self.limite=True
                        self.rect.y += 5
                        self.actualizarJumpDownInvertido()
                    if(self.rect.y==self.posactual):
                        self.limite=False
                        self.salto=False
        else :  #  Si tengo la piedra en la mano#
                if self.derecha:# si esta mirando a la derecha#
                    if self.idle:
                        self.actualizarIdleRock()
                    if self.run:
                        self.actualizarRunRock()
                        if(not key[pygame.K_d]):
                            self.run=False

                else: #Si esta mirando a la izquierda#
                    if self.idle:
                        self.actualizarIdleRockInvertida()
                    if self.run:
                        self.actualizarRunRockInvertida()
                        if(not key[pygame.K_d]):
                            self.run=False

    def actualizarIdleRockInvertida(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionIdleRock[self.posIdle],True,False)), (self.alto, self.ancho))
        self.delayIdleRockInvertido += 1
        if(self.delayIdleRockInvertido == 3):
            self.delayIdleRockInvertido = 0
            self.posIdle += 1

            if (self.posIdle == IDLE):
                self.posIdle=0


    def actualizarIdleRock(self):

        self.image = pygame.transform.scale(self.animacionIdleRock[self.posIdle], (self.alto, self.ancho))
        self.delayIdleRock += 1
        if(self.delayIdleRock == 3):
            self.delayIdleRock = 0
            self.posIdle += 1

            if (self.posIdle==IDLE):
                self.posIdle=0



    def actualizarThrowRock(self):
        self.image = pygame.transform.scale(self.animacionThrowRock[self.posThrowRock],(self.alto,self.ancho))
        self.delayThrowRock += 1

        if(self.delayThrowRock==3):
            self.delayThrowRock=0
            self.posThrowRock +=1

            if (self.posThrowRock==ROCK):
                self.posThrowRock=0

    def actualizarThrowRockInvertido(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionThrowRock[self.posThrowRock],True,False)),(self.alto,self.ancho))
        self.delayThrowRockInvertido += 1

        if(self.delayThrowRockInvertido == 3):
            self.delayThrowRockInvertido = 0
            self.posThrowRock += 1

            if (self.posThrowRock == ROCK):
                self.posThrowRock = 0

    def actualizarIdle(self):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))

        self.delayIdle += 1
        if(self.delayIdle == 3):
            self.delayIdle = 0
            self.posIdle +=1
            if (self.posIdle == IDLE +1):
                self.posIdle=0

    def actualizarIdleInvertida(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionIdle[self.posIdle],True,False)),(self.alto,self.ancho))

        self.delayIdleInvertido += 1
        if(self.delayIdleInvertido == 3):
            self.delayIdleInvertido = 0
            self.posIdle +=1
            if (self.posIdle == IDLE +1):
                self.posIdle=0

    def actualizarRunRockInvertida(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionRunRock[self.posRun],True,False)),(self.alto,self.ancho))

        self.delayRunRockInvertido += 1
        if(self.delayRunRockInvertido == 3):
            self.delayRunRockInvertido=0
            self.posRun +=1
            if(self.posRun == RUN):
                self.posRun = 0

    def actualizarRunRock(self):
        self.image = pygame.transform.scale(self.animacionRunRock[self.posRun], (self.alto, self.ancho))

        self.delayRunRock += 1
        if(self.delayRunRock == 3):
            self.delayRunRock=0
            self.posRun +=1
            if(self.posRun == RUN):
                self.posRun = 0

    def actualizarRun(self):
        self.image = pygame.transform.scale(self.animacionRun[self.posRun], (self.alto, self.ancho))

        self.delayRun +=1
        if(self.delayRun == 3):
            self.delayRun=0
            self.posRun +=1
            if(self.posRun == RUN):
                self.posRun = 0

    def actualizarRunInvertida(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionRun[self.posRun],True,False)),(self.alto,self.ancho))

        self.delayRunInvertido += 1
        if(self.delayRunInvertido == 3):
            self.delayRunInvertido=0
            self.posRun +=1
            if(self.posRun == RUN):
                self.posRun = 0

    def actualizarJump(self):
        self.image=pygame.transform.scale(self.animacionJump,(self.alto,self.ancho))

    def actualizarJumpInvertido(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionJump,True,False)),(self.alto,self.ancho))

    def actualizarJumpDown(self):
        self.image=pygame.transform.scale(self.animacionJumpDown,(self.alto,self.ancho))

    def actualizarJumpDownInvertido(self):
        self.image = pygame.transform.scale((pygame.transform.flip(self.animacionJumpDown,True,False)),(self.alto,self.ancho))

    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []

        while contador != cantidad +1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            contador += 1

        return listaAnimacion

    def devolverPosicionX(self):
        return self.rect.x

    def devolverPosicionY(self):
        return self.rect.y
