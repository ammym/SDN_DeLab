import requests
from pprint import pprint
import json
import csv
import time


#--------------------URL's------------------------------
url="https://api.meraki.com/api/v1/organizations/"

#----------------API-Key---------------------------------
Key = {"X-Cisco-Meraki-API-Key" : "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

#------------Definicion de Funciones--------------------

def getOrganizations (): #Imprime y devuelve la lista de las organizaciones
	
	response = requests.get(url,headers=Key)
	
	if (response.raise_for_status()!=None):
		print("Ha ocurrido un error en la consulta de las listas de las organizaciones")

	print("La lista de las organizaciones es:\n")
	
	pprint(response.json())

	res_org=response.json()
	
	return res_org

def getOrganizationsDevices (org): #Devuelve la lista de dispositivos de DeLab en archivo "Inventario.csv"
	for i in range(len(org)):
		if org[i]["name"] == "DeLab":
			id=org[i]["id"]
			DevicesList(id)
			break

def DevicesList(id):
	
	id_devices = id + "/devices"

	url_combine = url + id_devices

	response = requests.get(url_combine, headers=Key)
	
	if (response.raise_for_status()!=None):
		print("Ha ocurrido un error en la consulta de las listas de los dispositivos")

	res_devices = response.json()  #Lista de dispositivos

	res_status = DevicesStatuses(id) #Lista de status de dispositivos
	
	devices = []
	Dict = {}

	for i in range (len(res_devices)):
		if res_devices[i]["productType"] == "wireless" or res_devices[i]["productType"] == "appliance":
	
			Dict["Tipo_Producto"] = res_devices[i]["productType"]
			Dict["Modelo"] = res_devices[i]["model"]
			Dict["Nombre"] = res_devices[i]["name"]
			Dict["Direccion_MAC"] = res_devices[i]["mac"]
			Dict["Serial"] = res_devices[i]["serial"]
			if res_devices[i]["productType"] == "wireless":
				Dict["Direccion_IP_LAN"] = res_devices[i]["lanIp"]
			else:	
				Dict["Direccion_IP_LAN"] = ""
			for l in range(len(res_status)):
				if res_status[l]["serial"] == res_devices[i]["serial"] and res_status[l]["name"]==res_devices[i]["name"]:
					Dict["Direccion_IP_Publica"] = res_status[l]["publicIp"]
					Dict["Status"] = res_status[l]["status"]
			devices.append(Dict)
			Dict = {}

	DicttoCSV(devices)

def DevicesStatuses (id):

	id_devices_status = id + "/devices/statuses"

	url_combine = url + id_devices_status

	response = requests.get(url_combine, headers=Key)
	
	if (response.raise_for_status()!=None):
		print("Ha ocurrido un error en la consulta de los status de las listas de los dispositivos")
	
	res_status = response.json()
		
	return res_status

def DicttoCSV (devices):

	keys = devices[0].keys()

	with open('Inventario.csv',mode='w') as inventario:
		name_w=csv.DictWriter(inventario,delimiter=',', fieldnames = keys)
		name_w.writeheader()
		name_w.writerows(devices)


def Repeticion (): #Consulta cada 5min
	time.sleep(5*60)
	print("El archivo Inventario.csv se actualizo")

while(True): #Se realiza la consulta cada 5min y se actualiza el archivo "Inventario.csv"
	org=getOrganizations()
	getOrganizationsDevices (org)
	Repeticion()












