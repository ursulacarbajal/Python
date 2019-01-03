#encoding: utf-8
_author_ = 'AnDr3w-Jey' #The author us 
#This output allows the user to know what the program does
print("This program is to check the age range of a person \n")
#opt stands for option, which is going to be choose by the user
opt = str(input('Do you want to check an age? Write \'S\' for Yes or any other thing for NO: '))
#This IF is to control the writing of any kind of 'S'
if opt == 'S' or opt == 's':
	while opt == 'S' or opt == 's':	
		#This try-catch exception works to avoid the use of non-numbers
		try:
			#We require the age to the user
			opt = print('You didn\'t write a \'S\'. Try again: ')
			age = int(input("Write your age: "))
			if age < 0:
				print ("you have not born yet")
			if age >= 0 and age < 18:
				print ("You are underage")
			elif age >= 18 and age <= 27:
			    print ("You are a teenager")
			elif age >= 28 and age < 58:
			    print ("You are an adult")
			# If the person is more than 58 years old this option will be shown
			else:
			    print ("You are elderly old")
			#We request to the user 
			opt = print('Do you want to try another age? Say  \'S\'. if Yes: ')
		#If user didn't write a number, the exception will be executed
		except:
			opt = print('That isn\'t a number, Do you want to try again? Write a \'S\':')
else:
	print('You didn\'t write a \'S\'. Bye, Bye! ')