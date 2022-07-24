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

###### Estado:
***
En desarrollo

## Instalación
***
Para utilizar el programa debe utilizar python3 e instalar las librerías requests, pprint, json y csv. 

## Contenido
***
Con el uso de import se importan las librerías requeridas para ejecutar este programa.

### getOrganizations()

Es una función que imprime y devuelve la lista de las organizaciones con la que se puede acceder con la API-Key asignada por DeLab.

Utiliza el comando requests.get() para solicitar la lista de organizaciones, cuyos parámetros requeridos son la url de la API Meraki, contenida en la variable **url_1**, y la API-Key asignada, contenida en formato json en variable **Key**.
Devuelve la respuesta de la solicitud en response. Y con el comando **response.json()** retona el objeto JSON del resultado, que se imprime con **pprint()**. Finalmente, se retorna la lista de las organizaciones a las que se puede acceder con el API-Key asignado.

## ¿Cómo ejecutar?
***
Debe estar en la carpeta donde tiene el script.py, para ello utilice en el CMD los siguientes comandos:
```sh
cd ruta
python3 script.py
```
