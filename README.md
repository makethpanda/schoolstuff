# repo pour travail scolaire

## index
physiques chimie:
fonction-masse.py
formules variés 
Snt:
imagestuff
image modifier, colour filter + switcheroo






# physique chimie

## comment utiliser fonctions-masse.py

### 1. aller dans le dossier correspondant et copier coller le code du fichier dans spyder (ou autre)

### 2. lancer le programme pour vérifier que tout marche
 si tout fonctionne bien ceci doit apparaitre:

####template de formule
1= soluté en grammes, fiole en litres, 1

2= concetration en masse g/l, fiole en l, 2

3= grammes de soluté a trouver, concentration,3

4= masse en grammes, volume, 4

5= masse volumique en CM/G^3, volume a trouver, 5

6= g/cm3, masse en g, 6

ce sont des templates pour comment utiliser le programme.

### 3. pour lancer un calcul

##### 1. les multiples fonctions

1- Calculer la concentration en masse d’une solution réalisée avec x g de [] dans une fiole de x mL.

2- Calculer la masse de [] contenue dans une fiole de x mL sachant que la solution présente a une
concentration en masse de x g/L.

3- Calculer le volume qu’il faut prélever d’une solution  dont la concentration en masse vaut x g/L pour obtenir
x g de sucre.

4- une espece chimique possède une masse de x g pour un volume de x cm³ . Calculer sa masse volumique en g/cm³ .

5- Calculer la masse de [] qu’il faut peser pour en obtenir x m³ sachant que sa masse volumique vaut
x g/cm³ . 

6- Calculer le volume en cm³ de [] qu’il faut mesurer pour en obtenir x g sachant que sa masse
volumique est de x g/cm³ .


#### 2. utiliser la fonction pour lancer le calcul
#### fonction(x,y,z)
x = la premiere information a donner, se réferer a la template de formule, donc pour la focntion 1 c'est le soluté en grammes
y = la 2eme information a donner, se référencer a la template de formule, donc pour la conction 1 c'est la fiole en litres
z = le numéro du calcul a effectuer (les multiples fonctions

#### exemples
1----------------------fonction(10,0.1,1)
réponse du programme:
question: trouver Cm
données: 10.0 g soluté 0.1 solvant
relation: m/v
application numérique: 10 / 0.1
resultat: 100.0g/l
2---------------------fonction(10,0.05,2)
réponse du programme:
question: trouver la masse de x dans un contenu y
données: 10.0 g/l 0.05 diole
relation: m = Cm x v
application  10.0 x 0.05 = 0.5
resultat: 0.5 g
3--------------------fonction(0.125,5,3)
réponse du programme
question: calculer le volume qu'il fait prélever d'une solution pour avair xg de soluté
données  0.125 g de soluté que l'on veut trouver et  5.0 concentration
relation: m/Cm = v
application:  0.125 / 5.0
résultat:  0.025 l
4--------------------fonction(4.32,2,4)
réponse du programme
question: calculer masse volumique par rapport a la masse (x) et le volume (y)
données: 4.32 masse en gramme et  2.0 volume
relation: p = m x g
application: 4.32 x 2.0  = p
resultat: 2.16 g/cm^3
5-------------------fonction(2.16,1,5)
réponse du programme
question: calculer la masse qu'il faut peser pour obtenir y sachant que masse volumique = x
données: 2.16 masse volumique (g/cm^3) et  1.0 m^3 a trouver
relation: Mv = m/v donc m = Mv*v
application: 2.16 x 1.0 m^3 (x100) = masse
resultats: 216.0 kg/m^3
6------------------fonction(2.16, 10, 6)
réponse du programme
question: alculer le volume en cm3 de quelque chose ayant x masse volumique en g/cm^3qu'il faut mesurer pour obtenir y g 
données: 2.16  g/cm^3 10.0 grammes 
relation: volume a trouver = nbr de grammes a trouver/masse volumique
application: 10.0 / 2.16 = volume a trouver
resultat: 4.62962962962963 cm3
------------------------------------------
# snt

all the stuff for SNT for school

## how to download
### 1. click "clone or download"
unless you only need a specific file, in which case just double click it and copy paste the code
### 2. download as zip
### 3. extract all

