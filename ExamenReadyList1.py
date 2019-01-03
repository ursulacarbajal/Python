"""Create an array Named ReadyList1 with the following:
one integer
one double quotation string
one Boolean
one Sub-array with 3 elements of choice
one float
one single quotation string"""
#indices      0,      1           ,  2  ,       3      ,   4
ReadyList1 = [8,"double quotation", True,["hi", 1, 2.5], 2.5, 'Single Quotation']
#n.card:     1st,   2nd           , 3rd,        4th
#Lets print
print (ReadyList1)

#Change the third index in the Array into a number 5
ReadyList1[2] = 5
#Let's Print ReadyList1 with the change
print (ReadyList1)
#Do some Slicing begin from Index1 and copying 3 elements of the array ReadyList1.
ReadyList2 = ReadyList1[1:4]
print (ReadyList2)
#Create ReadyList3 and fill it with the same information as the original ReadyList1
#Lets make the change to restore the original ReadyList1
ReadyList3 = ReadyList1[:]
ReadyList3[2] = True
print (ReadyList3)

