#Examen respuesta 1
exit = input ("Ingrese para realizar una compra pulse S para salir u otra tecla para continuar")
while exit != 'S':
	if exit != 'S':
		try:
			numA = input ("Ingresa cantidad a comprar de Art A: ")
			numB = input ("Ingresa cantidad a comprar de Art B: ")
			numC = input ("Ingresa cantidad a comprar de Art C: ")
			numD = input ("Ingresa cantidad a comprar de Art D: ")
			numE = input ("Ingresa cantidad a comprar de Art E: ")
			descA = ((float(numA) * 1000) * 0.75)
			descB = ((float(numB) * 500) * 0.5)
			descC = ((float(numC) * 250) * 0.25)
			print ("Su descuento en prod A: " + str(descA) + " Su descuento en prod B: " + str(descB) + "Su descuento en prod C: " + str(descC))
			A = ((float(numA) * 1000) - float(descA))
			B = ((float(numB) * 500) - float(descB))
			C = ((float(numC) * 250) - float(descB))
			D = ((float(numD) * 100))
			E = ((float(numE) * 50))
			TOTAL = A + B + C + D + E
			print ("El total de su compra es de: " + str(TOTAL))
			exit = input ("Desea realizar otra compra? pulse S para salir u otra tecla para continuar: ")
		except:
			print("Use numbers, not letters")
	else:
		exit = input ("Desea realizar una compra? pulse S para salir u otra tecla para continuar: ")