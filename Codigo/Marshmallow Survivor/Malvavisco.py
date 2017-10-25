import pygame

#CONSTANTES
RUN = 16


IDLE = 19
JUMP = 10
ROCK = 12
PATH_RUN = "imagenes/AnimacionesMalvavisco/Run/"
PATH_RUN_INVERTIDA = "imagenes/AnimacionesMalvavisco/RunInvertido/"
PATH_IDLE = "imagenes/AnimacionesMalvavisco/Idle/"
PATH_IDLE_INVERTIDA = "imagenes/AnimacionesMalvavisco/IdleInvertido/"
PATH_JUMP = "imagenes/AnimacionesMalvavisco/Jump/"
PATH_JUMP_INVERTIDA = "imagenes/AnimacionesMalvavisco/JumpInvertido/"
PATH_JUMP_DOWN = "imagenes/AnimacionesMalvavisco/JumpDown/"
PATH_JUMP_DOWN_INVERTIDA = "imagenes/AnimacionesMalvavisco/JumpDownInvertido/"
PATH_THROW_ROCK = "imagenes/AnimacionesMalvavisco/ThrowRock/"
PATH_IDLE_ROCK = "imagenes/AnimacionesMalvavisco/IdleRock/"
PATH_IDLE_ROCK_INVERTIDA = "imagenes/AnimacionesMalvavisco/IdleRockInvertido/"
PATH_RUN_ROCK = "imagenes/AnimacionesMalvavisco/RunRock/"
PATH_RUN_ROCK_INVERTIDA = "imagenes/AnimacionesMalvavisco/RunRockInvertido/"


RED=(255,0,0)
pygame.mixer.init()
class Malvavisco(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y


        self.run = False
        self.idle = True
        self.derecha = True
        self.salto = False
        self.limite = False


        self.velocidad = 3

        self.rock = False

        self.velocidad = 5

        self.alto = alto
        self.ancho = ancho
        self.posRun = 0
        self.posIdle = 0
        self.posJump = 0
        self.posThrowRock=0
        self.distanciaSalto=100



        self.animacionRun = self.cargarAnimacion(RUN, PATH_RUN)
        self.animacionRunInvertida = self.cargarAnimacion(RUN, PATH_RUN_INVERTIDA)
        self.animacionIdle = self.cargarAnimacion(IDLE, PATH_IDLE)
        self.animacionIdleInvertida = self.cargarAnimacion(IDLE, PATH_IDLE_INVERTIDA)
        self.animacionJump = self.cargarAnimacion(JUMP, PATH_JUMP)
        self.animacionJumpInvertida = self.cargarAnimacion(JUMP, PATH_JUMP_INVERTIDA)
        self.animacionJumpDown = self.cargarAnimacion(JUMP,PATH_JUMP_DOWN)
        self.animacionJumpDownInvertida = self.cargarAnimacion(JUMP,PATH_JUMP_DOWN_INVERTIDA)


        self.animacionThrowRock = self.cargarAnimacion(ROCK, PATH_THROW_ROCK)

        self.animacionIdleRock = self.cargarAnimacion(IDLE, PATH_IDLE_ROCK)
        self.animacionIdleRockInvertida = self.cargarAnimacion(IDLE, PATH_IDLE_ROCK_INVERTIDA)
        self.animacionRunRock = self.cargarAnimacion(RUN, PATH_RUN_ROCK)
        self.animacionRunRockInvertida = self.cargarAnimacion(RUN, PATH_RUN_ROCK_INVERTIDA)



        self.sonidoSalto = pygame.mixer.Sound("Sonidos/Salto.ogg")

        self.image= pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.rect = self.image.get_rect()

        self.radius= int(self.rect.width/8)
        pygame.draw.circle(self.image,RED,self.rect.center,self.radius)

        self.rect.x=x
        self.rect.y=y
        #self.rect.center=(x/2,y/2)# instancio la imagen en el centro de la pantalla
        self.posactual=self.rect.y
        #self.rect.center=(0,0)# instancio la imagen en el centro de la pantalla

    def update(self, *args):
        key=pygame.key.get_pressed() #detecto que tecla estoy presionando

        if key[pygame.K_ESCAPE]:
            self.runningGame=False
        if key[pygame.K_SPACE] and self.rect.y==self.posactual:
            self.salto = True
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



        if not self.salto: #Si no estoy saltando

            if self.derecha: # si esta mirando a la derecha
                if self.idle:
                    self.actualizarIdle()

                if self.run:
                    self.actualizarRun()
                    if (not key[pygame.K_d]):
                        self.run = False

            else: #Si esta mirando a la izquierda
                if self.idle:
                    self.actualizarIdleInvertida()

                if self.run:
                    self.actualizarRunInvertida()
                    if (not key[pygame.K_a]):
                        self.run = False

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




        if not self.rock: # Si no tengo una piedra en la mano#
            if not self.salto:# si no estoy saltando#
                if self.derecha:# si esta mirando a la derecha#
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
        self.image = pygame.transform.scale(self.animacionIdleRockInvertida[self.posIdle], (self.alto, self.ancho))
        self.posIdle += 1
        if(self.posIdle == (IDLE + 1)):
            self.posIdle = 0

    def actualizarIdleRock(self):
        self.image = pygame.transform.scale(self.animacionIdleRock[self.posIdle], (self.alto, self.ancho),(0,0,20,41))
        self.image = (0,0,20,41)

        if(self.posIdle == (IDLE + 1)):
            self.posIdle = 0

    def actualizarThrowRock(self):
        self.image = pygame.transform.scale(self.animacionThrowRock[self.posThrowRock],(self.alto,self.ancho))
        self.posThrowRock +=1
        if (self.posThrowRock==33):
            self.posThrowRock=0
            self.rock= False




    def actualizarIdle(self):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))
        self.posIdle += 1
        if(self.posIdle == (IDLE + 1)):
            self.posIdle = 0

    def actualizarIdleInvertida(self):
        self.image = pygame.transform.scale(self.animacionIdleInvertida[self.posIdle],(self.alto,self.ancho))
        self.posIdle +=1
        if(self.posIdle == IDLE + 1):

            self.posIdle=0


            self.posIdle=0

    def actualizarRunRockInvertida(self):
        self.image = pygame.transform.scale(self.animacionRunRockInvertida[self.posRun], (self.alto, self.ancho))
        self.posRun += 1
        if(self.posRun == RUN):
            self.posRun = 0

    def actualizarRunRock(self):
        self.image = pygame.transform.scale(self.animacionRunRock[self.posRun], (self.alto, self.ancho))
        self.posRun += 1
        if(self.posRun == RUN):
            self.posRun = 0


    def actualizarRun(self):
        self.image = pygame.transform.scale(self.animacionRun[self.posRun], (self.alto, self.ancho))
        self.posRun += 1
        if(self.posRun == RUN):
            self.posRun = 0

    def actualizarRunInvertida(self):
        self.image=pygame.transform.scale(self.animacionRunInvertida[self.posRun],(self.alto,self.ancho))
        self.posRun +=1
        if(self.posRun == RUN):
            self.posRun = 0

    def actualizarJump(self):
        self.image=pygame.transform.scale(self.animacionJump[self.posJump],(self.alto,self.ancho))
        self.posJump +=1
        if (self.posJump== JUMP):
            self.posJump=0

    def actualizarJumpInvertido(self):
        self.image=pygame.transform.scale(self.animacionJumpInvertida[self.posJump],(self.alto,self.ancho))
        self.posJump +=1
        if(self.posJump==JUMP):
            self.posJump=0


    def actualizarJumpDown(self):
        self.image=pygame.transform.scale(self.animacionJumpDown[self.posJump],(self.alto,self.ancho))
        self.posJump +=1
        if(self.posJump==JUMP):
            self.posJump=0

    def actualizarJumpDownInvertido(self):
        self.image=pygame.transform.scale(self.animacionJumpDownInvertida[self.posJump],(self.alto,self.ancho))
        self.posJump +=1
        if(self.posJump==JUMP):
            self.posJump=0

    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []
        while contador != cantidad +1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())

            contador += 1

        return listaAnimacion


