# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:28:01 2020

@author: jboud
"""
#z)  1 = concentration en masse, 2= masse du soluté, 3= volume a prélever, 
#     4 = masse volumique   5= masse par rapport a la masse volumique
#      6 = volume pour obtenir 10g
#cm = M/v
print("1= soluté en grammes, fiole en litres, 1")
print("2= concetration en masse g/l, fiole en l, 2")
print("3= grammes de soluté a trouver, concentration,3")
print("4= masse en grammes, volume, 4")
print("5= masse volumique en CM/G^3, volume a trouver, 5")
print("6= g/cm3, masse en g, 6")
def fonction(x,y,z):
    x=float(x)
    y=float(y)
    if z==1 :
        print ("question: trouver Cm")
        print ("données:", x, "g soluté", y, "solvant")
        print("relation: m/v")
        print ("application numérique:",int(x),"/", float(y))
        resultat1= int(x)/float(y)
        print ("resultat: " + str(resultat1) + "g/l")
    if z==2 :
        print("question: trouver la masse de x dans un contenu y")
        print("données:",x, "g/l", y, "diole")
        print("relation: m = Cm x v")
        resultat2= int(x)*float(y)
        print("application ", x, "x", y, "=", str(resultat2))
        print("resultat:", str(resultat2), "g")
    if z==3 : 
        print("question: calculer le volume qu'il fait prélever d'une solution pour avair xg de soluté")
        print("données ", x, "g de soluté que l'on veut trouver et ", y, "concentration")
        print("relation: m/Cm = v")
        resultat3 = x/y
        print("application: ",x, "/",y)
        print("résultat: ", resultat3, "l")
    if z ==4:
        print("question: calculer masse volumique par rapport a la masse (x) et le volume (y)")
        print ("données:",x, "masse en gramme et ",y,"volume")
        print("relation: p = m x g")
        print("application:",x, "x",y, " = p")
        resultat4 = x/y
        print("resultat:",resultat4,"g/cm^3")
    if z==5:
        print ("question: calculer la masse qu'il faut peser pour obtenir y sachant que masse volumique = x")
        print("données:",x, "masse volumique (g/cm^3) et ",y, "m^3 a trouver")
        print("relation: Mv = m/v donc m = Mv*v")
        print("application:",x, "x", y,"m^3 (x100) = masse")
        resultat5 = x*y*100
        print("resultats:", resultat5, "kg/m^3")
    if z==6:
        print("question: alculer le volume en cm3 de quelque chose ayant x masse volumique en g/cm^3qu'il faut mesurer pour obtenir y g ")
        print("données:", x, " g/cm^3",y, "grammes ")
        print("relation: volume a trouver = nbr de grammes a trouver/masse volumique")
        print("application:",y, "/",x,"= volume a trouver")
        resultat6= y/x
        print("resultat:", resultat6, "cm3")
        
        
        