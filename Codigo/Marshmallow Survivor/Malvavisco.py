import pygame

#CONSTANTES
RUN = 36
IDLE = 40
JUMP = 20
PATH_RUN = "imagenes/AnimacionesMalvavisco/Run/"
PATH_RUN_INVERTIDA = "imagenes/AnimacionesMalvavisco/RunInvertido/"
PATH_IDLE = "imagenes/AnimacionesMalvavisco/Idle/"
PATH_IDLE_INVERTIDA = "imagenes/AnimacionesMalvavisco/IdleInvertido/"
PATH_JUMP = "imagenes/AnimacionesMalvavisco/Jump/"
PATH_JUMP_INVERTIDA = "imagenes/AnimacionesMalvavisco/JumpInvertido/"


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
        self.alto = alto
        self.ancho = ancho
        self.posRun = 0
        self.posIdle = 0
        self.posJump = 0
        self.distanciaSalto=100
        
        self.animacionRun = self.cargarAnimacion(RUN, PATH_RUN)
        self.animacionRunInvertida = self.cargarAnimacion(RUN, PATH_RUN_INVERTIDA)
        self.animacionIdle = self.cargarAnimacion(IDLE, PATH_IDLE)
        self.animacionIdleInvertida = self.cargarAnimacion(IDLE, PATH_IDLE_INVERTIDA)
        self.animacionJump = self.cargarAnimacion(JUMP, PATH_JUMP)
        self.animacionJumpInvertida = self.cargarAnimacion(JUMP, PATH_JUMP_INVERTIDA)
        
        
        self.image= pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))   
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        #self.rect.center=(x/2,y/2)# instancio la imagen en el centro de la pantalla
        self.posactual=self.rect.y
        #self.rect.center=(0,0)# instancio la imagen en el centro de la pantalla
        
    def update(self, *args):  
        key=pygame.key.get_pressed() #detecto que tecla estoy presionando
        print self.rect.y
        if key[pygame.K_SPACE] and self.rect.y==self.posactual:
            self.salto = True 
            
        if key[pygame.K_d]:
            self.derecha = True
            self.run = True
            self.rect.x += self.velocidad + 1
            
        if key[pygame.K_a]:
            self.derecha=False
            self.run=True
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
      
        else: #Si no estoy saltando
            
            if self.derecha: # Si salto y miro para la derecha
                self.actualizarJump()
                if(self.rect.y>self.posactual-100) and self.limite==False:
                    self.rect.y -=5
                    
                elif(self.rect.y!=self.posactual):
                    self.limite=True
                    self.rect.y += 5
                    if(self.rect.y==self.posactual):
                        self.limite=False
                        self.salto=False
                    
                        
                    
                
                
                    
                
              
            else: #Si salto y miro para la izquierda
                self.actualizarJumpInvertido()
                if(self.rect.y>self.posactual-self.distanciaSalto) and self.limite==False:
                    self.rect.y -=5
                    
                elif(self.rect.y!=self.posactual):
                    self.limite=True
                    self.rect.y += 5
                    if(self.rect.y==self.posactual):
                        self.limite=False
                        self.salto=False
        

  
        
                    
        
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
            
    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []
        while contador != cantidad + 1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            contador += 1
        
        return listaAnimacion
          

