Universidad Simón Bolívar
Trimestre Abril-Julio 2022
EC5756 Redes Definidas por Software (SDN)
Carnet: 17-10381
Estudiante: Amy Meneses
Profesora: Emma Di Batista

# **Práctica 2 - Python & Git**

## Descripción
***
Programa que permite acceder y listar las organizaciones con las que se tiene acceso con la API Key para Cisco Meraki otorgada por la compañía DeLab.

Crea un archivo Inventario.csv donde se listan los dispositivos "wireless" y "appliance" de la organización DeLab. Este contiene: Tipo_Poducto, Modelo, Nombre, Direccion_MAC, Serial, Direccion_IP_LAN, Direccion_IP_Publica y Status.

###### Estado:
***
Culminado

## Instalación
***
Para utilizar el programa debe utilizar python3 e instalar las librerías requests, pprint, json y csv. 

Para instalarlo se debe utilizar el CMD, en la carpeta donde está el archivo requierements.txt del proyecto y utilizar el comando:

	pip install -r requirements.txt

## Contenido
***
Con el uso de import se importan las librerías requeridas para ejecutar este programa.

### getOrganizations()

Es una función que imprime y devuelve la lista de las organizaciones con la que se puede acceder con la API-Key asignada por DeLab.

Utiliza el comando requests.get() para solicitar la lista de organizaciones, cuyos parámetros requeridos son la url de la API Meraki, contenida en la variable **url_1**, y la API-Key asignada, contenida en formato json en variable **Key**.
Devuelve la respuesta de la solicitud en response. Y con el comando **response.json()** retona el objeto JSON del resultado, que se imprime con **pprint()**. Finalmente, se retorna la lista de las organizaciones a las que se puede acceder con el API-Key asignado.

Para verificar si hay un error en la respuesta HTTP, se imprime **response.raise_for_status()**, si imprime NONE no hay error, en caso contrario, ha ocurrido un error en la respuesta.

### getOrganizationsDevices(org) 

Es una función que devuelve la lista de los dispostivos tipo "wireless" y "appliance" de la compañía DeLab en el archivo "Inventario.csv", este contiene los siguientes parámetros de los dispositivos:

- Tipo_Poducto
- Modelo
- Nombre
- Direccion_MAC
- Serial
- Direccion_IP_LAN
- Direccion_IP_Publica y Status. 

Busca en la lista de diccionarios que retorna **getOrganizations()** el id correspondiente a la compañia DeLab y utiliza la función **DevicesList(id)** para retornar la lista en el archivo "Inventario.csv".

### DevicesList(id) 

Es una función que realiza una petición de la lista de los dispositivos correspondientes al **id** de la compañía, en este caso, DeLab, a los que se puede acceder con el API-Key asignada. 

La url a la cual se le va a hacer la petición es la url_combine que contiene la dirección correspondiente al id de la compañia de la cual se requiere la lista de dispositivos.

**res_devices** contiene la lista de los dispositivos de la compañia, por otro lado, para obtener el status de los dispositivos, **res_status** tiene la lista de los dispositivos con su estatus que retorna la funcion **DevicesStatuses(id)**. Luego, se crea una lista de diccionarios denominada devices en las que se listan los dispositivos "wireless" y "appliance" de la compañía solicitada, en las que se guardan los parámetros:  Tipo_Poducto, Modelo, Nombre, Direccion_MAC, Serial, Direccion_IP_LAN, Direccion_IP_Publica y Status. 

Finalmente, se utiliza la función **DicttoCSV(devices)** donde se almacena la lista de dispositivos con sus parámetros en el archivo csv "Inventario.csv"

## DevicesStatuses(id) 

Es una función que retorna la respuesta obtenida al realizar la petición del estatus de la lista de los dispositivos correspondientes al id de la compañia solicitada, a partir del comando **requests.get()**.

## DicttoCSV(devices) 

Es una función que recibe una lista de diccionarios y lo guarda en el archivo "Inventario.csv" en el formato de valores separados por coma. 

Este archivo contiene la lista de los dispositivos "wireless" y "appliance" de la organización DeLab, este contiene: Tipo_Poducto, Modelo, Nombre, Direccion_MAC, Serial, Direccion_IP_LAN, Direccion_IP_Publica y Status.


## ¿Cómo ejecutar?
***
Debe estar en la carpeta donde tiene el script.py, para ello utilice en el CMD los siguientes comandos:
```sh
cd ruta
python3 script.py
```
