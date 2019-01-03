#Examen Ursula Carbajal - Respuesta#2
grade = input ("Ingrese la  Calificacion del Alumno: ")
grade = (int(grade))
if grade >=19  and grade <= 20:
	print ("La Calificacion es de A")
if grade >=16 and grade <= 18:
	print ("La Calificacion es de B")
if grade >=13 and grade <= 15:
	print ("La Calificacion es de C")
if grade >=10 and grade <= 12:
	print ("La Calificacion es de D")
if grade >=1 and grade <= 9:
	print ("La Calificacion es de E")	
if grade >=21 or grade <= 0:
	print ("Numero no valido")