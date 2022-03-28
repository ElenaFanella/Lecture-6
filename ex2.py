print("---- ESERCIZIO 2-----")
def controlla(list,obj):
 if obj in list:
   print("Si, l'elemento", obj, "è nella lista, ed il suo indice è", list.index(obj))
 else:
   print("No, in questa lista non c'è alcun elemento", obj)
 
numeri_primi=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
numero=input("Scegli un numero tra 0 e 100 e ti dirò se è numero primo.\n")
numero=int(numero)
controlla(numeri_primi, numero)