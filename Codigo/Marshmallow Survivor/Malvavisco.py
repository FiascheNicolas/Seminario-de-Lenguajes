import random
import pygame
from pygame.locals import *

run0=pygame.image.load("imagenes/run/0.png")
run1=pygame.image.load("imagenes/run/1.png")
run2=pygame.image.load("imagenes/run/2.png")
run3=pygame.image.load("imagenes/run/3.png")
run4=pygame.image.load("imagenes/run/4.png")
run5=pygame.image.load("imagenes/run/5.png")
run6=pygame.image.load("imagenes/run/6.png")
run7=pygame.image.load("imagenes/run/7.png")
run8=pygame.image.load("imagenes/run/8.png")
run9=pygame.image.load("imagenes/run/9.png")
run10=pygame.image.load("imagenes/run/10.png")
run11=pygame.image.load("imagenes/run/11.png")
run12=pygame.image.load("imagenes/run/12.png")
run13=pygame.image.load("imagenes/run/13.png")
run14=pygame.image.load("imagenes/run/14.png")
run15=pygame.image.load("imagenes/run/15.png")
run16=pygame.image.load("imagenes/run/16.png")
run17=pygame.image.load("imagenes/run/17.png")
run18=pygame.image.load("imagenes/run/18.png")
run19=pygame.image.load("imagenes/run/19.png")
run20=pygame.image.load("imagenes/run/20.png")
run21=pygame.image.load("imagenes/run/21.png")
run22=pygame.image.load("imagenes/run/22.png")
run23=pygame.image.load("imagenes/run/23.png")
run24=pygame.image.load("imagenes/run/24.png")
run25=pygame.image.load("imagenes/run/25.png")
run26=pygame.image.load("imagenes/run/26.png")
run27=pygame.image.load("imagenes/run/27.png")
run28=pygame.image.load("imagenes/run/28.png")
run29=pygame.image.load("imagenes/run/29.png")
run30=pygame.image.load("imagenes/run/30.png")
run31=pygame.image.load("imagenes/run/31.png")
run32=pygame.image.load("imagenes/run/32.png")
run33=pygame.image.load("imagenes/run/33.png")
run34=pygame.image.load("imagenes/run/34.png")
run35=pygame.image.load("imagenes/run/35.png")
run36=pygame.image.load("imagenes/run/36.png")

#Todas las posiciones de la animacion run invertida
Irun0=pygame.image.load("imagenes/Irun/0.png")
Irun1=pygame.image.load("imagenes/Irun/1.png")
Irun2=pygame.image.load("imagenes/Irun/2.png")
Irun3=pygame.image.load("imagenes/Irun/3.png")
Irun4=pygame.image.load("imagenes/Irun/4.png")
Irun5=pygame.image.load("imagenes/Irun/5.png")
Irun6=pygame.image.load("imagenes/Irun/6.png")
Irun7=pygame.image.load("imagenes/Irun/7.png")
Irun8=pygame.image.load("imagenes/Irun/8.png")
Irun9=pygame.image.load("imagenes/Irun/9.png")
Irun10=pygame.image.load("imagenes/Irun/10.png")
Irun11=pygame.image.load("imagenes/Irun/11.png")
Irun12=pygame.image.load("imagenes/Irun/12.png")
Irun13=pygame.image.load("imagenes/Irun/13.png")
Irun14=pygame.image.load("imagenes/Irun/14.png")
Irun15=pygame.image.load("imagenes/Irun/15.png")
Irun16=pygame.image.load("imagenes/Irun/16.png")
Irun17=pygame.image.load("imagenes/Irun/17.png")
Irun18=pygame.image.load("imagenes/Irun/18.png")
Irun19=pygame.image.load("imagenes/Irun/19.png")
Irun20=pygame.image.load("imagenes/Irun/20.png")
Irun21=pygame.image.load("imagenes/Irun/21.png")
Irun22=pygame.image.load("imagenes/Irun/22.png")
Irun23=pygame.image.load("imagenes/Irun/23.png")
Irun24=pygame.image.load("imagenes/Irun/24.png")
Irun25=pygame.image.load("imagenes/Irun/25.png")
Irun26=pygame.image.load("imagenes/Irun/26.png")
Irun27=pygame.image.load("imagenes/Irun/27.png")
Irun28=pygame.image.load("imagenes/Irun/28.png")
Irun29=pygame.image.load("imagenes/Irun/29.png")
Irun30=pygame.image.load("imagenes/Irun/30.png")
Irun31=pygame.image.load("imagenes/Irun/31.png")
Irun32=pygame.image.load("imagenes/Irun/32.png")
Irun33=pygame.image.load("imagenes/Irun/33.png")
Irun34=pygame.image.load("imagenes/Irun/34.png")
Irun35=pygame.image.load("imagenes/Irun/35.png")
Irun36=pygame.image.load("imagenes/Irun/36.png")


#Todas las posiciones de la animacion idle
idle0=pygame.image.load("imagenes/idle/0.png")
idle1=pygame.image.load("imagenes/idle/1.png")
idle2=pygame.image.load("imagenes/idle/2.png")
idle3=pygame.image.load("imagenes/idle/3.png")
idle4=pygame.image.load("imagenes/idle/4.png")
idle5=pygame.image.load("imagenes/idle/5.png")
idle6=pygame.image.load("imagenes/idle/6.png")
idle7=pygame.image.load("imagenes/idle/7.png")
idle8=pygame.image.load("imagenes/idle/8.png")
idle9=pygame.image.load("imagenes/idle/9.png")
idle10=pygame.image.load("imagenes/idle/10.png")
idle11=pygame.image.load("imagenes/idle/11.png")
idle12=pygame.image.load("imagenes/idle/12.png")
idle13=pygame.image.load("imagenes/idle/13.png")
idle14=pygame.image.load("imagenes/idle/14.png")
idle15=pygame.image.load("imagenes/idle/15.png")
idle16=pygame.image.load("imagenes/idle/16.png")
idle17=pygame.image.load("imagenes/idle/17.png")
idle18=pygame.image.load("imagenes/idle/18.png")
idle19=pygame.image.load("imagenes/idle/19.png")
idle20=pygame.image.load("imagenes/idle/20.png")
idle21=pygame.image.load("imagenes/idle/21.png")
idle22=pygame.image.load("imagenes/idle/22.png")
idle23=pygame.image.load("imagenes/idle/23.png")
idle24=pygame.image.load("imagenes/idle/24.png")
idle25=pygame.image.load("imagenes/idle/25.png")
idle26=pygame.image.load("imagenes/idle/26.png")
idle27=pygame.image.load("imagenes/idle/27.png")
idle28=pygame.image.load("imagenes/idle/28.png")
idle29=pygame.image.load("imagenes/idle/29.png")
idle30=pygame.image.load("imagenes/idle/30.png")
idle31=pygame.image.load("imagenes/idle/31.png")
idle32=pygame.image.load("imagenes/idle/32.png")
idle33=pygame.image.load("imagenes/idle/33.png")
idle34=pygame.image.load("imagenes/idle/34.png")
idle35=pygame.image.load("imagenes/idle/35.png")
idle36=pygame.image.load("imagenes/idle/36.png")
idle37=pygame.image.load("imagenes/idle/37.png")
idle38=pygame.image.load("imagenes/idle/38.png")
idle39=pygame.image.load("imagenes/idle/39.png")
idle40=pygame.image.load("imagenes/idle/40.png")

#Todas las posiciones de la animacion idle inventida
Iidle0=pygame.image.load("imagenes/Iidle/0.png")
Iidle1=pygame.image.load("imagenes/Iidle/1.png")
Iidle2=pygame.image.load("imagenes/Iidle/2.png")
Iidle3=pygame.image.load("imagenes/Iidle/3.png")
Iidle4=pygame.image.load("imagenes/Iidle/4.png")
Iidle5=pygame.image.load("imagenes/Iidle/5.png")
Iidle6=pygame.image.load("imagenes/Iidle/6.png")
Iidle7=pygame.image.load("imagenes/Iidle/7.png")
Iidle8=pygame.image.load("imagenes/Iidle/8.png")
Iidle9=pygame.image.load("imagenes/Iidle/9.png")
Iidle10=pygame.image.load("imagenes/Iidle/10.png")
Iidle11=pygame.image.load("imagenes/Iidle/11.png")
Iidle12=pygame.image.load("imagenes/Iidle/12.png")
Iidle13=pygame.image.load("imagenes/Iidle/13.png")
Iidle14=pygame.image.load("imagenes/Iidle/14.png")
Iidle15=pygame.image.load("imagenes/Iidle/15.png")
Iidle16=pygame.image.load("imagenes/Iidle/16.png")
Iidle17=pygame.image.load("imagenes/Iidle/17.png")
Iidle18=pygame.image.load("imagenes/Iidle/18.png")
Iidle19=pygame.image.load("imagenes/Iidle/19.png")
Iidle20=pygame.image.load("imagenes/Iidle/20.png")
Iidle21=pygame.image.load("imagenes/Iidle/21.png")
Iidle22=pygame.image.load("imagenes/Iidle/22.png")
Iidle23=pygame.image.load("imagenes/Iidle/23.png")
Iidle24=pygame.image.load("imagenes/Iidle/24.png")
Iidle25=pygame.image.load("imagenes/Iidle/25.png")
Iidle26=pygame.image.load("imagenes/Iidle/26.png")
Iidle27=pygame.image.load("imagenes/Iidle/27.png")
Iidle28=pygame.image.load("imagenes/Iidle/28.png")
Iidle29=pygame.image.load("imagenes/Iidle/29.png")
Iidle30=pygame.image.load("imagenes/Iidle/30.png")
Iidle31=pygame.image.load("imagenes/Iidle/31.png")
Iidle32=pygame.image.load("imagenes/Iidle/32.png")
Iidle33=pygame.image.load("imagenes/Iidle/33.png")
Iidle34=pygame.image.load("imagenes/Iidle/34.png")
Iidle35=pygame.image.load("imagenes/Iidle/35.png")
Iidle36=pygame.image.load("imagenes/Iidle/36.png")
Iidle37=pygame.image.load("imagenes/Iidle/37.png")
Iidle38=pygame.image.load("imagenes/Iidle/38.png")
Iidle39=pygame.image.load("imagenes/Iidle/39.png")
Iidle40=pygame.image.load("imagenes/Iidle/40.png")


class Malvavisco(pygame.sprite.Sprite):
    
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.run=False
        self.idle=True
        self.derecha=True
        self.velocidad=3
        self.alto=500
        self.ancho=400
        self.posrun=0
        self.posidle=0
        self.listarun=[run0,run1,run2,run3,run4,run5,run6,
                       run7,run8,run9,run10,run11,run12,run13,
                       run14,run15,run16,run17,run18,run19,run20,
                       run21,run22,run23,run24,run25,run26,run27,run28,
                       run28,run30,run31,run32,run33,run34,run35,run36]
        self.listaidle=[idle0,idle1,idle2,idle3,idle4,idle5,idle6,idle7,idle8,idle9,idle10,
                        idle11,idle12,idle13,idle14,idle15,idle16,idle17,idle18,idle19,idle20,
                        idle21,idle22,idle23,idle24,idle25,idle26,idle27,idle28,idle29,idle30,
                        idle31,idle32,idle33,idle34,idle35,idle36,idle37,idle38,idle39,idle40,]   
                  
        self.listaIidle=[Iidle0,Iidle1,Iidle2,Iidle3,Iidle4,Iidle5,Iidle6,Iidle7,Iidle8,Iidle9,Iidle10,
                        Iidle11,Iidle12,Iidle13,Iidle14,Iidle15,Iidle16,Iidle17,Iidle18,Iidle19,Iidle20,
                        Iidle21,Iidle22,Iidle23,Iidle24,Iidle25,Iidle26,Iidle27,Iidle28,Iidle29,Iidle30,
                        Iidle31,Iidle32,Iidle33,Iidle34,Iidle35,Iidle36,Iidle37,Iidle38,Iidle39,Iidle40,]   
        
        self.listaIrun=[Irun0,Irun1,Irun2,Irun3,Irun4,Irun5,Irun6,
                       Irun7,Irun8,Irun9,Irun10,Irun11,Irun12,Irun13,
                       Irun14,Irun15,Irun16,Irun17,Irun18,Irun19,Irun20,
                       Irun21,Irun22,Irun23,Irun24,Irun25,Irun26,Irun27,Irun28,
                       Irun28,Irun30,Irun31,Irun32,Irun33,Irun34,Irun35,Irun36]
        
        self.image= pygame.transform.scale(self.listaidle[self.posidle],(self.alto,self.ancho))   
        self.rect = self.image.get_rect()
        self.rect.center=(900/2,800/2)# instancio la imagen en el centro de la pantalla
       # self.rect.center=(0,0)# instancio la imagen en el centro de la pantalla
    def update(self, *args):
        pygame.sprite.Sprite.update(self, *args)    
        
        key=pygame.key.get_pressed() #detecto que tecla estoy presionando
        
        if key[pygame.K_d]:
            self.derecha=True
            self.run=True
            self.rect.x +=self.velocidad  
        if key[pygame.K_a]:
            self.derecha=False
            self.run=True
            self.rect.x -=self.velocidad
        
            
        if self.derecha:    # en caso de que este mirando a la derecha
            if self.idle==True:
                self.image= pygame.transform.scale(self.listaidle[self.posidle],(self.alto,self.ancho))
                self.posidle=self.posidle+1
                if(self.posidle==41):self.posidle=0
            if self.run==True:
                self.image= pygame.transform.scale(self.listarun[self.posrun],(self.alto,self.ancho))
                self.posrun=self.posrun+1
               
                if(self.posrun==36):self.posrun=0
                if (not key[pygame.K_d]) : self.run=False #si no aprieta la tecla d vuelve a su estado idle
                
        else:     # en caso de que este mirando a la izquierda
            if self.idle==True:
                self.image=pygame.transform.scale(self.listaIidle[self.posidle],(self.alto,self.ancho))
                self.posidle=self.posidle+1
                if(self.posidle==41):self.posidle=0
            if self.run==True:
                self.image=pygame.transform.scale(self.listaIrun[self.posrun],(self.alto,self.ancho))
                self.posrun=self.posrun+1
                
                if(self.posrun==36):self.posrun=0
                if (not key[pygame.K_a]) : self.run=False #si no aprieta la tecla a vuelve a su estado idle
        
        
    
            
          

