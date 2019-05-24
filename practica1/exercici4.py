#!/usr/bin/env python3
"""
Data creació: 24.05.2019
@author: David Gasa i Castell
"""

from random import randint
from time import sleep
import matplotlib.pyplot as plt

def grafica(llista):
    x=range(llista.__len__())
    y=llista
    
    plt.xticks(x)
    plt.yticks(range(0,70,10))
    
    plt.bar (x,y)
    plt.show()

#Aquesta funció retorna 0 o 1 en funció que passi o no passi una persona
#estem fent la suposició que en 1 segon només pot passar una persona.

def distancia():
	binari = 0
	
	# Assumim que la distància des del sensor fins a la paret és de 4 metres
	# Si obtenim una distància inferior, comptem una persona
	if (randint (0,4) < 4):
		binari = 1
	
	return binari # 0 o 1 en funció que passi una persona o no



# Codi principal

while True:
	llistapersones=[]
	minuts=0
	while (minuts<10):
		persones=0
		for segons in range(60):
			persones += distancia()
			sleep(1)
		llistapersones.append (persones)
		minuts += 1
		
	grafica(llistapersones)