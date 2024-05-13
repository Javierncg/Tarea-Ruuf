# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:42:19 2024

@author: javie
"""

import numpy as np

def CuentaPaneles(x1,y1,a1,b1):

    a=a1
    b=b1
    x=x1
    y=y1
    #Se corrige la orientación del input
    if a>b:
        a=b1
        b=a1
    if x>y:
        x=y1
        y=x1    
        
    nvx=x//a
    nhy=y//a
    #Se revisa si se puede ubicar al menos un panel
    if nvx==0 or nhy==0:
        return 0
    
    #Se calcula la cantidad máxima que podria entrar de manera ficticia y superpuesta
    nc=(nhy*nvx)
    n=2**nc
    
    Px=np.zeros([n,nhy,nvx])
    Py=np.zeros([n,nhy,nvx])
    CT=np.zeros([1,n])
    
    #Se crean todas las combinaciones
    for i in range(0,n):
        combinacion = bin(i)[2:].zfill(nc)
        combX=combinacion.replace('0',str(a)).replace('1', str(b))
        combY=combinacion.replace('0',str(b)).replace('1', str(a))
        Or0X=np.array([int(digito) for digito in combX])
        Or0Y=np.array([int(digito) for digito in combY])
        Px[i,:,:]=np.reshape(Or0X,[nhy,nvx])
        Py[i,:,:]=np.reshape(Or0Y,[nhy,nvx])
    
    #Se revisa la factibilidad
    for i in range(0,n):
        OX=Px[i,:,:]
        OY=Py[i,:,:]
        
        SX=np.sum(OX,axis=1)
        SY=np.sum(OY,axis=0)
        
        #Se eliminan elementos que no calzan
        for j in range(0,nhy):
            e=-1
            while SX[j]>x:
                OX[j,e]=0
                SX=np.sum(OX,axis=1)
                e=e-1
            Px[i,:,:]=OX
            
        for j in range(0,nvx):
            e=-1
            while SY[j]>y:
                OY[e,j]=0
                SY=np.sum(OY,axis=0)
                e=e-1
            Py[i,:,:]=OY        
            
        CT[0,i]=np.count_nonzero(OX*OY)
    Cmax=np.max(CT[0,:])
    return Cmax


x=7
y=7

a=3
b=2

print(CuentaPaneles(x,y,a,b))