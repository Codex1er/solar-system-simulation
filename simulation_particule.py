# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:12:09 2021

@author: Utilisateur
"""
"""
#1er version

simulation de particules interagissants entre elles à l'aide d'une force décroissant avec le carré de la distance. 

"""


import pylab
import random

const=0.0025
max_X=100
max_Y=100
d=100#rayon de la particule=d*const*masse**(1/3)


nb_image=30
dure_image=200


"""
nb_particule=104
p_X=[[5],[16],[-18],[19]]
p_Y=[[4],[-13],[-4],[16]]
v_X=[[0],[0.05],[0.03],[-0.04]]
v_Y=[[0],[0.06],[-0.03],[-0.02]]
masse=[1,1,1,1]
"""
"""
nb_particule=2
p_X=[[-50],[50]]
p_Y=[[-50],[50]]
v_X=[[.01],[-.01]]
v_Y=[[-.01],[.01]]
masse=[100,100]




"""
nb_particule=100
p_X=[]
p_Y=[]
v_X=[]
v_Y=[]
masse=[]
for i in range(nb_particule):
    p_X=p_X+[[random.random()*max_X*2-max_X]]
    p_Y=p_Y+[[random.random()*max_Y*2-max_Y]]
    v_X=v_X+[[p_Y[i][0]*(p_Y[i][0]**2+p_X[i][0]**2)**(1/2)*0.000001]]
    v_Y=v_Y+[[-p_X[i][0]*(p_Y[i][0]**2+p_X[i][0]**2)**(1/2)*0.000001]]    
    masse=masse+[10*random.random()]












pylab.xlabel('p_X')
pylab.ylabel('p_Y')
    
pylab.xlim(-max_X,max_X)
pylab.ylim(-max_Y,max_Y)
    

X=[]
Y=[]
for i in range(nb_particule):
    if masse[i]<=0:
        X=X+[p_X[i][-1]]
        Y=Y+[p_Y[i][-1]]
pylab.plot(X,Y,'yo')
X=[]
Y=[]
for i in range(nb_particule):
    if masse[i]>0:
        X=X+[p_X[i][-1]]
        Y=Y+[p_Y[i][-1]]
pylab.plot(X,Y,'go')
pylab.grid()
pylab.show()



for k in range(nb_image):
    colision_X=[]
    colision_Y=[]



    
    for t in range(dure_image*k,dure_image*(k+1)):
        
        for i in range(nb_particule):
            v_X[i].append(v_X[i][t])
            v_Y[i].append(v_Y[i][t])        
            
            for j in range(nb_particule):
    
                if i!=j:
                    if p_X[i][t]>=p_X[j][t]:
                        x=1
                    else:
                        x=0
                    if p_Y[i][t]>=p_Y[j][t]:
                        y=1
                    else:
                        y=0
                        
                    
                    if masse[i]<=0 or masse[j]<=0:
                        m=-1
                    else:
                        m=1
                    
                    v_X[i][t+1]=v_X[i][t+1]+m*abs(masse[j])*const*(p_X[j][t]-p_X[i][t])/((p_X[i][t]-p_X[j][t])**2+(p_Y[i][t]-p_Y[j][t])**2)**(3/2)
                    v_Y[i][t+1]=v_Y[i][t+1]+m*abs(masse[j])*const*(p_Y[j][t]-p_Y[i][t])/((p_X[i][t]-p_X[j][t])**2+(p_Y[i][t]-p_Y[j][t])**2)**(3/2)
            p_X[i].append(p_X[i][t]+v_X[i][t+1])
            p_Y[i].append(p_Y[i][t]+v_Y[i][t+1])
            
            """  
        i=0       
        while i<nb_particule:
           
            if p_X[i][t+1]>max_X or p_X[i][t+1]<-max_X or p_Y[i][t+1]>max_Y or p_Y[i][t+1]<-max_Y:
                nb_particule=nb_particule-1
                colision_X=colision_X+[p_X[i]]
                colision_Y=colision_Y+[p_Y[i]]
                p_X=p_X[:i]+p_X[i+1:]
                p_Y=p_Y[:i]+p_Y[i+1:]
                v_X=v_X[:i]+v_X[i+1:]
                v_Y=v_Y[:i]+v_Y[i+1:]
                masse=masse[:i]+masse[i+1:]
            i=i+1
            
            """
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
            if p_X[i][t+1]>max_X:
                p_X[i][t+1]=2*max_X-p_X[i][t+1]
                v_X[i][t+1]=0
                v_Y[i][t+1]=0 
            if p_X[i][t+1]<-max_X:
                p_X[i][t+1]=-2*max_X-p_X[i][t+1]
                v_X[i][t+1]=0
                v_Y[i][t+1]=0 
            if p_Y[i][t+1]>max_Y:
                p_Y[i][t+1]=2*max_Y-p_Y[i][t+1]
                v_Y[i][t+1]=0
                v_X[i][t+1]=0 
            if p_Y[i][t+1]<-max_Y:
                p_Y[i][t+1]=-2*max_Y-p_Y[i][t+1]
                v_Y[i][t+1]=0
                v_X[i][t+1]=0 
        i=0       
        while i<nb_particule:
            j=i
            while j<nb_particule:
                if i!=j and ((p_X[i][t+1]-p_X[j][t+1])**2+(p_Y[i][t+1]-p_Y[j][t+1])**2)<=d*const*(abs(masse[j])**(1/3)+abs(masse[i])**(1/3)):
                    nb_particule=nb_particule-1
                    p_X[i][t+1]=(abs(masse[i])*p_X[i][t+1]+abs(masse[j])*p_X[j][t+1])/(abs(masse[i])+abs(masse[j]))
                    p_Y[i][t+1]=(abs(masse[i])*p_Y[i][t+1]+abs(masse[j])*p_Y[j][t+1])/(abs(masse[i])+abs(masse[j]))
                    v_X[i][t+1]=(abs(masse[i])*v_X[i][t+1]+abs(masse[j])*v_X[j][t+1])/(abs(masse[i])+abs(masse[j]))
                    v_Y[i][t+1]=(abs(masse[i])*v_Y[i][t+1]+abs(masse[j])*v_Y[j][t+1])/(abs(masse[i])+abs(masse[j]))
                    colision_X=colision_X+[p_X[j]]
                    colision_Y=colision_Y+[p_Y[j]]                
                    p_X=p_X[:j]+p_X[j+1:]
                    p_Y=p_Y[:j]+p_Y[j+1:]
                    v_X=v_X[:j]+v_X[j+1:]
                    v_Y=v_Y[:j]+v_Y[j+1:]
                    masse[i]=masse[i]+masse[j]
                    masse=masse[:j]+masse[j+1:]
                    j=j-1
                j=j+1
            i=i+1
    
    
    
    
    for i in range(nb_particule+len(colision_X)):
        X=p_X+colision_X
        Y=p_Y+colision_Y
        
        pylab.plot(X[i][dure_image*k:],Y[i][dure_image*k:],'-')
    
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]<=-100:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'ro')
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]<=-10 and masse[i]>-100:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'mo')
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]<=0 and masse[i]>-10:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'yo')
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]>=0 and masse[i]<10:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'go')
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]>=10 and masse[i]<100:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'co')
    X=[]
    Y=[]
    for i in range(nb_particule):
        if masse[i]>=100:
            X=X+[p_X[i][-1]]
            Y=Y+[p_Y[i][-1]]
    pylab.plot(X,Y,'bo')
    
    
    pylab.xlabel('p_X')
    pylab.ylabel('p_Y')
        
    pylab.xlim(-max_X,max_X)
    pylab.ylim(-max_Y,max_Y)
        
    pylab.grid()
    pylab.show()
    
    
    






