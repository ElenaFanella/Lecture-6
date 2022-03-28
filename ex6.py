print("----ESERCIZIO 6---")
import random
max=input("Quanto te la rischi?\n")
n=random.randint(1,int(max))
prove=input("Quanti tentativi vuoi fare?\n")
for i in range(int(prove)):
 N=input("Prova ad indovinare il numero:\n")
 while N.isalpha()==True:
   N=input("Devi inserire un NUMERO \n")
 while "." in N:
   N=input("Devi inserire un numero INTERO \n")
 while int(N)<=0:
   N=input("Devi inserire un numero intero POSITIVO! \n")
 if int(N)==n:
   print("Bella, hai al tentavivo numero",i+1)
   break
 else:
   risp=input("Sbagliato! Vuoi continuare?\n")
   if risp=="si":
     continue
   elif risp=="no":
     print("Non sai perdere! Comunque il numero era",n)
     break

   