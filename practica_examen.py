#Practica_examen
SALIR = input ("Desea realizar una compra? pulse S para salir u otra tecla para continuar: ")
while SALIR != 'S':
	if SALIR !='S':
		try:
			ValorA = input ("Ingresa Cant Art A: ") 
			ValorB = input ("Ingresa Cant Art B: ")
			ValorC = input ("Ingresa Cant Art C: ")
			ValorD = input ("Ingresa Cant Art D: ")
			descA = ((float(ValorA) * 750) * 0.25)
			descB = ((float(ValorB) * 1500) * 0.75)
			print ("Sus descuentos son: " + str(descA) + " y " + str(descB))
			A = ((float(ValorA) * 750) - float(descA))
			B = ((float(ValorB) * 1500) - float(descB))
			C = ((float(ValorC) * 500) + float(ValorD)*500)
			TOT = A + B + C
			print ("El total de su compra es: " + str(TOT))
			SALIR = input ("Desea realizar una compra? pulse S para salir u otra tecla para continuar: ")
		except:
			print("Use numbers, not letters")	
	else:
		SALIR = input ("Desea realizar una compra? pulse S para salir u otra tecla para continuar: ")