ll = [2, "tres", True, ["uno",10]]
print (ll)
#Using the Array Index
ll2 = ll[1]
print (ll2)
print (ll[0])
print (ll[3])
#Accesing Array's index that are in an Array list: [indexinArray][indexInList]
ll3 = ll[3][0]
print (ll3)
print (str (ll[3][1]))



#modifying inner array's data with the index:
l = [2, "tres", True, ["uno", 10], 5, "Hi"]
l[1] = 4
l2 = l[1]
print (l2)
print ('Imprimir cambio de dato en Indice 1:' + str (12))
#slicing: Copy some information from an Array towards another one [beggningIndex]
l3 = l[0:3]
l7 = l[1:2]
print ('Imprimir Slicing de Indice 0, 3 Elementos: ' + str (l3))
#copy some information from an Array towards another one by skipping some information [begginingIndex:QuantityofcopyingElement:Amountof SkipsPerIndex]
l4 = l[0:3:2]
print('Imprimir desde indice 0, 3 elementos, saltando cada 2 elementos' + str(l4))
#Copy some information from an Array towards another one by skipping each we want [begginingIndex:AmountofSkipsperIndex]
l5 = [2,"tres",True,["uno", 10],6]
l6 = l5 [0::2]
print ('ImprimirLista 5: ' + str(l5))
print ('Imprimir la informacion saltando los daos consecutivos: ' + str (l6))
