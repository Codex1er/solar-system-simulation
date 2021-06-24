# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:39:40 2021

@author: Utilisateur
"""

"""
#3eme version
utilse rk2 car odeint fait tros de caprice

simulation de particules interagissants entre elles à l'aide d'une force décroissant avec le carré de la distance. 

"""
import random
import numpy
from moviepy.editor import *
import math
import copy



const=0.0025
max_X=100
max_Y=100
d=100#rayon de la particule=d*const*masse**(1/3)


nb_image=10000

nb_particule=100
p_X=[]
p_Y=[]
v_X=[]
v_Y=[]
masse=[]
for i in range(nb_particule):
    p_X=p_X+[random.random()*max_X*2-max_X]
    p_Y=p_Y+[random.random()*max_Y*2-max_Y]
    v_X=v_X+[p_Y[i]*(p_Y[i]**2+p_X[i]**2)**(1/2)*0.000001]
    v_Y=v_Y+[-p_X[i]*(p_Y[i]**2+p_X[i]**2)**(1/2)*0.000001]    
    masse=masse+[10*random.random()]

collision=[]

def fonction(p_X,p_Y,masse):#RFD
    for i in range(nb_particule):
        a_X=[0 for i in range(nb_particule)]
        a_Y=[0 for i in range(nb_particule)]
        if i not in collision:
            for j in range(nb_particule):
                if i!=j and (j not in collision):
                    if p_X[t][i]>=p_X[t][j]:
                        x=1
                    else:
                        x=0
                    if p_Y[t][i]>=p_Y[t][j]:
                        y=1
                    else:
                        y=0
                        
                    
                    if masse[t][i]<=0 or masse[t][j]<=0:
                        m=-1
                    else:
                        m=1
                    
                    a_X[i]=a_X[i]+m*abs(masse[j])*const*((-1)**(x))/((p_X[i]-p_X[j])**2+(p_Y[i]-p_Y[j])**2)
                    a_Y[i]=a_Y[i]+m*abs(masse[j])*const*((-1)**(y))/((p_X[i]-p_X[j])**2+(p_Y[i]-p_Y[j])**2)
            p_X[t+1][i]=p_X[t][i]+v_X[t+1][i]
            p_Y[t+1][i]=p_Y[t][i]+v_Y[t+1][i]
          





    return

    

    for i in range(nb_particule):
        for j in  range(i+1,nb_particule):
            if masse(i)!=None and masse(j)!=None:
                if p_X[i]==p_X[j] and p_Y[i]==p_Y[j] and v_X[i]==v_X[j] and v_Y[i]==v_Y[j]:
                    masse[i]=masse[i]+masse[j]
                    masse[j]=None

    for i in range(nb_particule):
        for j in  range(i+1,nb_particule):
            if masse(i)!=None and masse(j)!=None: 
                if i!=j and ((p_X[i]-p_X[j])**2+(p_Y[i]-p_Y[j])**2)<=d*const*(abs(masse[j])**(1/3)+abs(masse[i])**(1/3)):
                    p_X[i]=(abs(masse[i])*p_X[i]+abs(masse_r[j])*p_X[j])/(abs(masse_reel[i])+abs(masse_reel[j]))
                    p_Y[i]=(abs(masse[i])*p_Y[i]+abs(masse[j])*p_Y[j])/(abs(masse_reel[i])+abs(masse_reel[j]))
                    v_X[i]=(abs(masse[i])*v_X[i]+abs(masse[j])*v_X[j])/(abs(masse_reel[i])+abs(masse_reel[j]))
                    v_Y[i]=(abs(masse[i])*v_Y[i]+abs(masse[j])*v_Y[j])/(abs(masse_reel[i])+abs(masse_reel[j]))
                    p_X[t+1][j]=None
                    p_Y[t+1][j]=None
                    v_X[t+1][j]=None
                    v_Y[t+1][j]=None
                    masse[t][i]=masse[t][i]+masse[t][j]
                    masse[t][j]=None



for t in range(nb_image):   
    p_X.append([None for i in range(nb_particule)])
    p_Y.append([None for i in range(nb_particule)])
    v_X.append([None for i in range(nb_particule)])
    v_Y.append([None for i in range(nb_particule)])
    for i in range(nb_particule):
        if i not in colision:
            v_X[t+1][i]=v_X[t][i]
            v_Y[t+1][i]=v_Y[t][i]        
            
            for j in range(nb_particule):
                if i!=j and (j not in colision):
                    if p_X[t][i]>=p_X[t][j]:
                        x=1
                    else:
                        x=0
                    if p_Y[t][i]>=p_Y[t][j]:
                        y=1
                    else:
                        y=0
                        
                    
                    if masse[t][i]<=0 or masse[t][j]<=0:
                        m=-1
                    else:
                        m=1
                    
                    v_X[t+1][i]=v_X[t+1][i]+m*abs(masse[t][j])*const*((-1)**(x))/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)
                    v_Y[t+1][i]=v_Y[t+1][i]+m*abs(masse[t][j])*const*((-1)**(y))/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)
            p_X[t+1][i]=p_X[t][i]+v_X[t+1][i]
            p_Y[t+1][i]=p_Y[t][i]+v_Y[t+1][i]
            

            """
            if p_X[i][t+1]>max_X:
                p_X[i][t+1]=2*max_X-p_X[i][t+1]
                v_X[i][t+1]=-v_X[i][t+1]
            if p_X[i][t+1]<-max_X:
                p_X[i][t+1]=-2*max_X-p_X[i][t+1]
                v_X[i][t+1]=-v_X[i][t+1]
            if p_Y[i][t+1]>max_Y:
                p_Y[i][t+1]=2*max_Y-p_Y[i][t+1]
                v_Y[i][t+1]=-v_Y[i][t+1]
            if p_Y[i][t+1]<-max_Y:
                p_Y[i][t+1]=-2*max_Y-p_Y[i][t+1]
                v_Y[i][t+1]=-v_Y[i][t+1]
            """
            if p_X[t+1][i]>max_X:
                p_X[t+1][i]=2*max_X-p_X[t+1][i]
                v_X[t+1][i]=0
                v_Y[t+1][i]=0 
            if p_X[t+1][i]<-max_X:
                p_X[t+1][i]=-2*max_X-p_X[t+1][i]
                v_X[t+1][i]=0
                v_Y[t+1][i]=0 
            if p_Y[t+1][i]>max_Y:
                p_Y[t+1][i]=2*max_Y-p_Y[t+1][i]
                v_Y[t+1][i]=0
                v_X[t+1][i]=0 
            if p_Y[t+1][i]<-max_Y:
                p_Y[t+1][i]=-2*max_Y-p_Y[t+1][i]
                v_Y[t+1][i]=0
                v_X[t+1][i]=0 
    i=0       
    while i<nb_particule:
        j=i+1
        while j<nb_particule:
            if i not in colision and j not in colision: 
                if i!=j and ((p_X[t+1][i]-p_X[t+1][j])**2+(p_Y[t+1][i]-p_Y[t+1][j])**2)<=d*const*(abs(masse[t][j])**(1/3)+abs(masse[t][i])**(1/3)):
                    p_X[t+1][i]=(abs(masse[t][i])*p_X[t+1][i]+abs(masse[t][j])*p_X[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    p_Y[t+1][i]=(abs(masse[t][i])*p_Y[t+1][i]+abs(masse[t][j])*p_Y[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    v_X[t+1][i]=(abs(masse[t][i])*v_X[t+1][i]+abs(masse[t][j])*v_X[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    v_Y[t+1][i]=(abs(masse[t][i])*v_Y[t+1][i]+abs(masse[t][j])*v_Y[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    colision.append(j)
                    p_X[t+1][j]=None
                    p_Y[t+1][j]=None                        
                    v_X[t+1][j]=None
                    v_Y[t+1][j]=None
                    masse[t][i]=masse[t][i]+masse[t][j]
                    masse[t][j]=None
            j=j+1
        i=i+1
    masse.append(copy.deepcopy(masse[-1]))



def image(p_X_t,p_Y_t,masse_t):
    img=numpy.array([[[255,255,255] for i in range(200)] for j in range(200)] )
    for i in range(nb_particule):
        if masse_t[i]!=None:
            
            for theta in [2*math.pi*i/10 for i in range(10)]:
                img[min(int(p_X_t[i]+math.cos(theta)*d*const*masse_t[i]**(1/3))+100,199),min(int(p_Y_t[i]+math.sin(theta)*d*const*masse_t[i]**(1/3))+100,199),:]=[0,0,0]

    return img

def F(p_X,p_Y,masse):
    F=[]
    for t in range(0,nb_image,5):
        F.append(image(p_X[t],p_Y[t],masse[t]))
    
    return F

F=F(p_X,p_Y,masse)

film=ImageSequenceClip(F, fps=30)
film.write_videofile("nuage.mp4",fps=30)