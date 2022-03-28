print("----ESERCIZIO 4----")
N=input("Inserisci un numero intero positivo \n")
while N.isalpha()==True:
 N=input("Devi inserire un NUMERO \n")
while "." in N:
  N=input("Devi inserire un numero INTERO \n")
while int(N)<=0:
 N=input("Devi inserire un numero intero POSITIVO! \n")
print("#"*int(N))