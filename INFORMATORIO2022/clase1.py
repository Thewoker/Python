productA= input("Ingrese que productos va a llevar\n")
PrecioA = input("Precio\n")

cantA = input("Ingrese la cantidad\n")

productB= input("Ingrese que productos va a llevar\n")
PrecioB = input("Precio\n")

cantB = input("Ingrese la cantidad\n")

productC= input("Ingrese que productos va a llevar\n")
PrecioC = input("Precio\n")

cantC = input("Ingrese la cantidad\n")

print ("\nSu lista de compra es\n--------------------------------------")
print (f"{productA}\t{cantA}\n{productB}\t{cantB}\n{productC}\t{cantC}")
print (f"Total + IVA: {1.21*(int(PrecioA)*(int(cantA)) + int(PrecioB)*(int(cantB)) + int(PrecioC)*(int(cantC)))}")
