#Escriba un programa que solicite el número de filas e imprima un triángulo.

print("**********************")
n=int(input("Ingresar un número cualquiera: \n"))
x=0
while x<=n:
  print("*"*x)
  x=x+1

i=0
for i in range(n+1):
	print("*"*i)
	
for i in range(n+1):
 espacio=n-i
 print(" "*espacio+"*"*i)

for i in range(n+1):
 espacio=n-i
 print(" "*espacio+"* "*i)
