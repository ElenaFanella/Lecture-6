print("----ESERCIZIO 1----")
elenco_disponibili = {"Farenheit 451": 10, "Zibaldone": 7,
"#Aristotle's Metaphysics": 5, "L'Alchimista": 1, "Harry Potter": 2, "Cime tempestose": 1}

def presta_libri(nome_libro):
 elenco_non_disponibili={}
 if nome_libro in elenco_disponibili:
   print("Si, abbiamo questo libro in archivio. Ora controllo quante copie") 
   if elenco_disponibili[nome_libro]>0:
     print("Ne abbiamo ancora", elenco_disponibili[nome_libro],"copie, puoi prenderlo in prestito. Buona lettura.")
     buon_fine=True
     elenco_disponibili[nome_libro]=elenco_disponibili[nome_libro]-1
     if elenco_disponibili[nome_libro]==0:
       elenco_disponibili.pop(nome_libro)
       elenco_non_disponibili={nome_libro}
   elif elenco_disponibili[nome_libro]==0:
     print("Ci spiace, tutte le copie di questo libro sono in prestito. Torna a trovarci.")
     buon_fine=False
     elenco_non_disponibili={nome_libro}
 else:
   buon_fine=False
   print("Ci dispiace non abbiamo questo libro. C'è bisogno di fare un ordine di acquisto.")
   elenco_da_ordinare={nome_libro}
 if buon_fine:
   print("Il prestito è andato a buon fine")
 else:
   print("Il prestito non è andato a buon fine")
 return buon_fine



copie=input("Benvenuto in biblioteca. Puoi prendere fino a cinque libri diversi. Quanti ne vuoi?\n")
if int(copie)>5:
  print("Mi dispiace puoi prenderene al massimo 5.")
  copie=5
for i in range(int(copie)):
   nome=input("Che libro vorresti?\n")
   prestito=presta_libri(nome)
   while not prestito:
    nome=input("Che libro vorresti?\n")
    prestito=presta_libri(nome)