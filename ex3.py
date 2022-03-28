print("----ESERCIZIO 3----")
def freq_lettere(stringa): 
 dic={}
 for lettera in stringa:
   if lettera in dic:
     dic[lettera]=dic[lettera]+1
   else:
     dic[lettera]=1
 for c in dic:
  if c.isalpha():
    print(c,"*"*int(dic[c]))

#parola=input("insterisci una parola: ")
#print("Con stringa scelta dall'utente: ", parola)
#freq_lettere(parola)

file=open("f.txt",'r')
righe=file.readlines()
file.close()
#print("\n Leggendo le righe dal file f.txt")
i=1
for riga in righe:
 i+=1
 print("\nriga numero",i,"parola:",riga)
 freq_lettere(riga)