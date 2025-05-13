import PIA_modulo
lista_datos = PIA_modulo.obtener_datos()

opcion=""
while opcion!="13":
	print("Menú")
	print("1.Datos de un país especifico de Ámerica")
	print("2.Mediana y media de las áreas")
	print("3.Gráfico de línea país-área")
	print("4.País con menor población")	
	print("5.Gráfica barras de los 5 países con menor población")
	print("6.País con mayor población")
	print("7.Gráfica barras de los 5 países con mayor población")
	print("8.Frecuencia de idiomas en Ámerica")
	print("9.Gráfica de barras frecuencia de idiomas en Ámerica")
	print("10.Porcentaje de idiomas")
	print("11.Gráfica de pastel porcentaje de idiomas")
	print("12.Crear un archivo de excel con todos los datos")
	print("13.Salir")

	opcion=input("Elija un número:")

	if opcion=="1":
		nombre_pais=input("Ingrese el nombre del país del cual desea obtener sus datos:")
		PIA_modulo.datos_pais(lista_datos, nombre_pais)

	elif opcion=="2":
		areas=PIA_modulo.main_areas(lista_datos)
		PIA_modulo.analisis_areas(areas)

	elif opcion=="3":
		areas=PIA_modulo.main_areas(lista_datos)
		PIA_modulo.graf_areas(areas, lista_datos)
	
	elif opcion=="8":
		frecuencia_idiomas=PIA_modulo.frecuencia_idiomas(lista_datos)
		PIA_modulo.impresion_frecuencia_idiomas(frecuencia_idiomas)

	elif opcion=="9":
		PIA_modulo.frecuencia_idiomas(lista_datos)
		PIA_modulo.grafica_frecuencia_idiomas(frecuencia_idiomas)
		

	elif opcion=="10":
		porcentajes=PIA_modulo.porcentaje_idiomas(lista_datos)
		PIA_modulo.impresion_porcentaje_idiomas(porcentajes)

	elif opcion=="11":
		porcentajes=PIA_modulo.porcentaje_idiomas(lista_datos)
		PIA_modulo.grafica_porcentaje_idiomas(porcentajes)
		
	elif opcion=="12":
		PIA_modulo.excel(lista_datos)

	elif opcion=="13":
		print("Saliendo...")
	
	else:
		print("Opción fuera de rango. Intente de nuevo")




	