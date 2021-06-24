# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:30:21 2021

@author: Utilisateur
"""
"""
#2eme version
sortie au format video
simulation de particules interagissants entre elles à l'aide d'une force décroissant avec le carré de la distance. 

"""
import random
import numpy
from moviepy.editor import *
import math
import copy

const=0.005
max_X=100
max_Y=100
d=70#rayon de la particule=d*const*masse**(1/3)
nb_image=5000
nb_particule=101

p_X=[[0]]
p_Y=[[0]]
v_X=[[0]]
v_Y=[[0]]
masse=[[1000]]

for i in range(1,nb_particule):
    p_X[-1]=p_X[-1]+[random.random()*max_X*2-max_X]
    p_Y[-1]=p_Y[-1]+[random.random()*max_Y*2-max_Y]
    
    v_X[-1]=v_X[-1]+[p_Y[0][i]*4*math.pi**2/((p_Y[0][i]**2+p_X[0][i]**2)**(3/4)*(const*1000)**(1/2))]
    v_Y[-1]=v_Y[-1]+[-p_X[0][i]*4*math.pi**2/((p_Y[0][i]**2+p_X[0][i]**2)**(3/4)*const*1000)**(1/2)]
    """"""
   
    masse[-1]=masse[-1]+[3*random.random()]

collision=[]
"""
v_X=[[0 for i in range(nb_particule)]]
v_Y=[[0 for i in range(nb_particule)]]
"""

[[1,2,3,6,5,9]+[4]]






for t in range(nb_image):   
    p_X.append([None for i in range(nb_particule)])
    p_Y.append([None for i in range(nb_particule)])
    v_X.append([None for i in range(nb_particule)])
    v_Y.append([None for i in range(nb_particule)])
    for i in range(nb_particule):# schema d'euler plus RFD
        if i not in collision:
            v_X[t+1][i]=v_X[t][i]
            v_Y[t+1][i]=v_Y[t][i]
            
            for j in range(nb_particule):
                if i!=j and (j not in collision):
                    """
                    if p_X[t][i]>=p_X[t][j]:#le sens des vecteur unitaire
                        x=1
                    else:
                        x=0
                    if p_Y[t][i]>=p_Y[t][j]:
                        y=1
                    else:
                        y=0
                    """
                    if masse[t][i]<=0 or masse[t][j]<=0:#la charge 
                        m=-1
                    else:
                        m=1
                    """
                    v_X[t+1][i]=v_X[t+1][i]+m*abs(masse[t][j])*const*((-1)**(x))/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)
                    v_Y[t+1][i]=v_Y[t+1][i]+m*abs(masse[t][j])*const*((-1)**(y))/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)
                    """
                    v_X[t+1][i]=v_X[t+1][i]+m*abs(masse[t][j])*const*(p_X[t][j]-p_X[t][i])/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)**(3/2)
                    v_Y[t+1][i]=v_Y[t+1][i]+m*abs(masse[t][j])*const*(p_Y[t][j]-p_Y[t][i])/((p_X[t][i]-p_X[t][j])**2+(p_Y[t][i]-p_Y[t][j])**2)**(3/2)


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
            
            if p_X[t+1][i]>max_X:# les murs
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
            """
    for i in range(nb_particule):# les collisions
        for j in range(i+1,nb_particule):
            if i not in collision and j not in collision: 
                if i!=j and ((p_X[t+1][i]-p_X[t+1][j])**2+(p_Y[t+1][i]-p_Y[t+1][j])**2)<=d*const*(abs(masse[t][j])**(1/3)+abs(masse[t][i])**(1/3)):
                    p_X[t+1][i]=(abs(masse[t][i])*p_X[t+1][i]+abs(masse[t][j])*p_X[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    p_Y[t+1][i]=(abs(masse[t][i])*p_Y[t+1][i]+abs(masse[t][j])*p_Y[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    v_X[t+1][i]=(abs(masse[t][i])*v_X[t+1][i]+abs(masse[t][j])*v_X[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    v_Y[t+1][i]=(abs(masse[t][i])*v_Y[t+1][i]+abs(masse[t][j])*v_Y[t+1][j])/(abs(masse[t][i])+abs(masse[t][j]))
                    collision.append(j)
                    p_X[t+1][j]=None
                    p_Y[t+1][j]=None                        
                    v_X[t+1][j]=None
                    v_Y[t+1][j]=None
                    masse[t][i]=masse[t][i]+masse[t][j]
                    masse[t][j]=None
    masse.append(copy.deepcopy(masse[-1]))

def image(p_X_t,p_Y_t,masse_t):
    img=numpy.array([[[255,255,255] for i in range(2*max_X)] for j in range(2*max_Y)] )
    for i in range(nb_particule):
        if masse_t[i]!=None:
            if p_X_t[i]>=-max_X and p_X_t[i]<=max_X and p_Y_t[i]>=-max_Y and p_Y_t[i]<=max_Y:
                for theta in [2*math.pi*i/10 for i in range(10)]:# 10 est le nombre de point maximale par particule
                    img[min(int(p_X_t[i]+math.cos(theta)*d*const*masse_t[i]**(1/3))+max_X,2*max_X-1),min(int(p_Y_t[i]+math.sin(theta)*d*const*masse_t[i]**(1/3))+max_Y,2*max_Y-1),:]=[0,0,0]
    return img

def Film(p_X,p_Y,masse):
    F=[]
    for t in range(0,nb_image,5):# le 5 permet de ne pas calculer plus d'image que l'on peut en voir
        F.append(image(p_X[t],p_Y[t],masse[t]))
    return F

film=ImageSequenceClip(Film(p_X,p_Y,masse),fps=30)
film.write_videofile("nuage.mp4",fps=30)