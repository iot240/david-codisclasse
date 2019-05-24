#!/usr/bin/env python3
"""
Data creació: 24.05.2019
@author: David Gasa i Castell
"""

from random import randint
from time import sleep
import cayenne.client

def cayene(valors):
	#enviar dades a cayenne. No cal return
	client.virtualWrite (1, valors)
	
#Aquesta funció retorna 0 o 1 en funció que passi o no passi una persona
#estem fent la suposició que en 1 segon només pot passar una persona.

def distancia():
	binari = 0
	
	# Assumim que la distància des del sensor fins a la paret és de 4 metres
	# Si obtenim una distància inferior, comptem una persona
	if (randint (0,4) < 4):
		binari = 1
	
	return binari # 0 o 1 en funció que passi una persona o no
	
#Autenticació a Cayenne

MQTT_USERNAME = "1c98e520-7c79-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "2eba1b4a8c107e05fb9fa84772fa4731a94ee996"
MQTT_CLIENT_ID = "7757d1c0-7dfe-11e9-be3b-372b0d2759ae"

client = cayenne.client.CayenneMQTTClient()
client.begin (MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

#El programa enviarà dades a cayenne cada minut

while True:
	client.loop()
	persones = 0
	for segons in range(60):
		persones += distancia()
		sleep(1)
		
	cayene(persones)
