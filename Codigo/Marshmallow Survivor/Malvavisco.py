import random
import pygame
from pygame.locals import *
from xmlrpclib import boolean
contador=0
listarun=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
#Cargo en una lista todas las imagenes de la animacion run
while contador!=37:
    
    listarun[contador]=pygame.image.load("imagenes/run/"+str(contador)+".png")
    contador += 1

contador=0
listaIrun=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
#Cargo en una lista todas las imagenes de la animacion Irun 
while contador!=37:
    listaIrun[contador]=pygame.image.load("imagenes/Irun/"+str(contador)+".png")
    contador += 1

contador=0
listaidle=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
#Cargo en una lista todas las imagenes de la animacion idle
while contador != 41:
    listaidle[contador]=pygame.image.load("imagenes/idle/"+str(contador)+".png")
    contador += 1

contador=0
listaIidle=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
#Cargo en una lista todas las imagenes de la animacion Iidle
while contador != 41:
    listaIidle[contador]=pygame.image.load("imagenes/Iidle/"+str(contador)+".png")
    contador += 1

contador=0
listajump=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Cargo en una lista todas las imagenes de la animacion jump
while contador !=21:
    listajump[contador]=pygame.image.load("imagenes/jump/"+str(contador)+".png")
    contador += 1

contador=0
listaIjump=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Cargo en una lista todas las imagenes de la animacion Ijump
while contador !=21:
    listaIjump[contador]=pygame.image.load("imagenes/Ijump/"+str(contador)+".png")
    contador +=1
class Malvavisco(pygame.sprite.Sprite):
    
        
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        
        self.run=False
        self.idle=True
        self.derecha=True
        self.salto=False
        self.limite=False
        self.velocidad=10
        self.alto=500
        self.ancho=400
        self.posrun=0
        self.posidle=0
        self.posjump=0
        
        #Animaciones//
        self.listarun=listarun
        self.listaIrun=listaIrun
        self.listaidle=listaidle  
        self.listaIidle=listaIidle
        self.listajump=listajump
        self.listaIjump=listaIjump
        
        #////////
        
        self.image= pygame.transform.scale(self.listaidle[self.posidle],(self.alto,self.ancho))   
        self.rect = self.image.get_rect()
        self.rect.center=(x/2,y/2)# instancio la imagen en el centro de la pantalla
        self.posactual=self.rect.y
       # self.rect.center=(0,0)# instancio la imagen en el centro de la pantalla
    def update(self, *args):
        #pygame.sprite.Sprite.update(self, *args)    
        
        key=pygame.key.get_pressed() #detecto que tecla estoy presionando
        
        if key[pygame.K_SPACE] and self.rect.y==self.posactual:
           self.salto=True 
            
        
        if key[pygame.K_d]:
            self.derecha=True
            self.run=True
           
            self.rect.x +=self.velocidad  
        if key[pygame.K_a]:
            self.derecha=False
            self.run=True
            
            self.rect.x -=self.velocidad
        
            
        
        
      
            
        if self.salto==False:
            if self.rect.y!=self.posactual:self.rect.y +=20
            if self.derecha: # si esta mirando a la derecha
                if self.idle==True:
                     self.image= pygame.transform.scale(self.listaidle[self.posidle],(self.alto,self.ancho))
                     self.posidle=self.posidle+1
                     if(self.posidle==41):self.posidle=0
                if self.run==True:
                    self.image=pygame.transform.scale(self.listarun[self.posrun],(self.alto,self.ancho))
                    self.posrun=self.posrun+1
                    if(self.posrun==36):self.posrun=0
                    if (not key[pygame.K_d]):self.run=False
         
            else:#Si esta mirando a la izquierda
                if self.idle==True:
                    self.image=pygame.transform.scale(self.listaIidle[self.posidle],(self.alto,self.ancho))
                    self.posidle=self.posidle+1
                    if(self.posidle==41):self.posidle=0
                if self.run==True:
                    self.image=pygame.transform.scale(self.listaIrun[self.posrun],(self.alto,self.ancho))
                    self.posrun=self.posrun+1
                    if(self.posrun==36):self.posrun=0
                    if (not key[pygame.K_a]):self.run=False    
      
        else:
            
            if self.derecha: # Si salto y miro para la derecha
                self.image=pygame.transform.scale(self.listajump[self.posjump],(self.alto,self.ancho))
                self.posjump=self.posjump+1
                
                if(self.posjump==21):
                    self.posjump=0
                  
                if(self.rect.y>20):
                    self.rect.y -=20
                else:self.salto=False
              
            else: #Si salto y miro para la izquierda
                self.image=pygame.transform.scale(self.listaIjump[self.posjump],(self.alto,self.ancho))
                self.posjump=self.posjump+1
                if(self.posjump==21): self.posjump=0
                
                   
                  
                if(self.rect.y>20):
                    self.rect.y -=20
                else:self.salto=False 
        
    
            
          

