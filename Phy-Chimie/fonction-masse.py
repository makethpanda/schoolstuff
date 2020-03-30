# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:28:01 2020

@author: jboud
"""
#z)  1 = concentration en masse, 2= masse du soluté, 3= volume a prélever, 
#     4 = masse volumique   5= masse par rapport a la masse volumique
#      6 = volume pour obtenir 10g

print("1= soluté en grammes, fiole en litres, 1")
print("2= concetration en masse g/l, fiole en l, 2")
def fonction(x,y,z):
    if z==1 :
        x=int(x)
        y=float(y)
        print ("question: trouver Cm")
        print ("données:", x, "soluté", y, "solvant")
        print("relation: m/v")
        print ("application numérique:",int(x),"/", float(y))
        resultat1= int(x)/float(y)
        print ("solution: " + str(resultat1) + "g/l")
    if z==2 :
        print("question: trouver la masse de x dans un contenu y")
        x=int(x)
        y=float(y)
        print("données:",x, "g/l", y, "diole")
        print("relation: m = Cm x L")
        resultat2= int(x)*float(y)
        print("application ", x, "x", y, "=", str(resultat2))
        print("solution:", str(resultat2), "g")
        