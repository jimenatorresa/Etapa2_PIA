import requests
import json
import statistics
import matplotlib.pyplot as plt
import pandas as pd
 
def obtener_datos():
	url="https://restcountries.com/v3.1/region/america?fields=name,area,unMember,languages,independent,population,translations,capital"
	lista_datos=[]
	try:
		respuesta = requests.get(url, timeout=10)
		if respuesta.status_code==200:
			datos_paises=respuesta.json()
			with open('datos_paises.json', 'w') as archivo:
				json.dump(datos_paises, archivo, indent=4)
			for pais in datos_paises:
				if pais.get("independent")==True:
					nombre=pais["translations"]["spa"]["common"]
					area=pais["area"]
					lenguajes=list(pais["languages"].values())
					capital=pais["capital"]
					poblacion=pais["population"]
					lista_datos.append({"País":nombre, "Área": area, "Lenguajes": lenguajes, "Población": poblacion, "Capital": capital})
	
			with open('paises_america.json', 'w') as archivo:
				json.dump(lista_datos, archivo, indent=4)
	except:
		print("Error de conexión. Buscando datos locales...")
	finally:
		if not lista_datos:
			try:
				with open('paises_america.json', 'r') as archivo:
					lista_datos=json.load(archivo)
			except FileNotFoundError:
				print("El archivo no fue encontrado")
			except IOError:
				print("Error al acceder al archivo")	
	
	return(lista_datos)

#DATOS PAÍS
def datos_pais(lista_datos, nombre_pais):
	for pais in lista_datos:
		if pais["País"].lower()== nombre_pais.lower():
			print(f"Nombre: {pais["País"]}")
			print(f"Capital: {pais["Capital"]}")
			print(f"Población: {pais["Población"]}")
			print(f"Área: {pais["Área"]}")
			print(f"Idioma: {pais["Lenguajes"]}")
	
		
#EXPORTAR DATOS A EXCEL
def excel(lista_datos):
	df=pd.DataFrame(lista_datos)
	archivo_ruta='datos_america.xlsx'
	df.to_excel(archivo_ruta, index=False)
	print("Archivo de excel creado exitosamente")
	


#ANÁLISIS ÁREAS
def main_areas(lista_datos):
	return [pais["Área"] for pais in lista_datos]
		
def analisis_areas(areas):
	print(f"Media: {statistics.mean(areas):.2f} kilometros cuadrados")
	print(f"Mediana: {statistics.median(areas):.2f} kilometros cuadrados")

def graf_areas(areas, lista_datos):
	areas_ord=sorted(areas)
	ordenados=sorted(lista_datos, key=lambda x:x["Área"])
	nombres_ordenados=[pais["País"] for pais in ordenados]
	plt.plot(nombres_ordenados, areas_ord)
	plt.title("País-Área")
	plt.xlabel("País")
	plt.ylabel("Área")
	plt.xticks(rotation=90)
	plt.grid(True)
	plt.show()

#ANÁLISIS POBLACIÓN
def pais_menor_poblacion(lista_datos):
	menores = sorted(lista_datos, key=lambda x: x["Población"])[:5]
	print("País con menor población:")
	print(menores[0])
 
def grafica_menor_poblacion(lista_datos):
	menores = sorted(lista_datos, key=lambda x: x["Población"])[:5]
	nombres = [pais['País'] for pais in menores]
	poblaciones = [pais['Población'] for pais in menores]
 
	plt.figure(figsize=(10, 6))
	plt.bar(nombres, poblaciones, color='orange')
	plt.title("5 países con menor población en América")
	plt.xlabel("País")
	plt.ylabel("Población")
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()
	return menores[0]
 
def pais_mayor_poblacion(lista_datos):
	print("País con mayor población:")
	print(mayores[0])
 
def grafica_mayor_poblacion(lista_datos):
	mayores = sorted(lista_datos, key=lambda x: x["Población"], reverse=True)[:5]
	nombres = [pais['País'] for pais in mayores]
	poblaciones = [pais['Población'] for pais in mayores]
 
	plt.figure(figsize=(10, 6))
	plt.bar(nombres, poblaciones, color='green')
	plt.title("5 países con mayor población en América")
	plt.xlabel("País")
	plt.ylabel("Población")
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()
 
	return mayores[0]

#ANÁLISIS IDIOMAS
def frecuencia_idiomas (lista_datos): #Definimos la función
 
	from collections import Counter		#Importamos Counter para sacar la frecuencia
 
	#Sacamos la frecuencia de idiomas hablados en el continente americano
	todos_lenguajes=[]	
	for pais in lista_datos:
		todos_lenguajes.extend(pais["Lenguajes"])	#Cuenta los países que coinciden en el idioma
	return Counter(todos_lenguajes)
 
def impresion_frecuencia_idiomas(frecuencia_idiomas):
	for idioma, count in frecuencia_idiomas.most_common():
		print(f"{idioma}: {count}")	#Muestra los datos obtenidos
 
def grafica_frecuencia_idiomas(frecuencia_idiomas):
 

	#Realizamos gráfica de barras con matplotlib
	etiquetas = list(frecuencia_idiomas.keys()) 
	valores = list(frecuencia_idiomas.values()) 
	plt.bar(etiquetas, valores, color='purple') 
	plt.title("Frecuencia de idiomas en América") 
	plt.show()
 
########
 
def porcentaje_idiomas(lista_datos):	#Definimos la función
	frecuencia= frecuencia_idiomas(lista_datos)	
	#Sacamos porcentajes
	total_paises=len(lista_datos)
	porcentajes = {}
	for idioma, count in frecuencia.items():
		porcentajes[idioma] =(count / total_paises) * 100
	return porcentajes
 
def impresion_porcentaje_idiomas(porcentajes):
 
	print("Porcentaje de idiomas en América (por países)")
	for idioma, porcentaje in porcentajes.items():
    		print(f"{idioma}: {porcentaje:.2f}%")	#Imprimimos los datos
 
def grafica_porcentaje_idiomas(porcentajes):
 
	#Realizamos gráfica de pastel
	idiomas= list(porcentajes.keys()) 
	valores = list(porcentajes.values()) 
	plt.pie(valores, labels=idiomas, autopct='%1.1f%%') 
	plt.title("Porcentaje de idiomas hablados en el continente americano") 
	plt.axis('equal') 
	plt.show()




		



	