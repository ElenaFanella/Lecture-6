print("----ESERCIZIO 5-----")
def rettangolo(b,a):
 print("* "*b)
 for i in range(1,a-1):
   print("*"," "*(2*b-5), "*")
 print("* "*b)
  
risp=input("Vuoi disegnare un rettangolo? ")
while risp=="si":
 base=input("base: ")
 while base.isnumeric()==False or int(base)<3:
   base=input("Inserisci un numero intero e maggiore di 3")
 altezza=input("altezza: ")
 while altezza.isnumeric()==False or int(altezza)<3:
   altezza=input("Inserisci un numero intero e maggiore di 3")
 rettangolo(int(base),int(altezza))
 risp=input("Vuoi disegnare un altro rettangolo? ")