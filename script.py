import requests
from pprint import pprint

#--------------------URL------------------------------
url="https://api.meraki.com/api/v1/organizations/"

#----------------API-Key---------------------------------
Key = {"X-Cisco-Meraki-API-Key" : "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

#------------Definicion de Funciones--------------------

def getOrganizations (): #Imprime y devuelve la lista de las organizaciones
	
	response = requests.get(url,headers=Key)

	print("La lista de las organizaciones es:\n")
	
	pprint(response.json())

	res_org=response.json()
	
	return res_org

org = getOrganizations()







