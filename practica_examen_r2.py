#practica_examen_r2
#SALIR = input ("Calculo de Calificiones: ingrese S para salir o cualquier otra tecla para continuar:  ")
#while SALIR != 'S'
#	if SALIR != 'S'
#	try:
ValorA = input ("Ingrese la  Calificacion del Alumno: ")
ValorA = (int(ValorA))
if ValorA <= 100 and ValorA >= 91:
	print ("La Calificacion es de A, el estudiante aprueba")
if ValorA <=90 and ValorA >= 71:
	print ("La Calificacion es de B, el estudiante aprueba")
if ValorA <=70 and ValorA >= 61:
	print ("La Calificacion es de C, el estudiante no aprueba")
if ValorA <=60 and ValorA >= 50:
	print ("La Calificacion es de D, el estudiante no aprueba")
if ValorA <=49 and ValorA >= 1:
	print ("La Calificacion es de F, el estudiante no aprueba")	