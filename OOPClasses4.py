class Human:
     def __init__(self, age): #El age aqui es una variable
    #self.attribute = variable
           self.edad = age #edad es un atributo = age (variable)
           print ('I am a human been')
     def talk(self, message):
           print (message)
Leslie = Human(23) 
Michael = Human(26)
Leslie.talk("Hello, Michael")
Michael.talk("Oh\! Hi, Leslie")
print ("I\'m Michael, and I have " + str(Michael.edad) + " years old")
print ("I\'m Leslie, and I have " + str(Leslie.edad) + " years old")

