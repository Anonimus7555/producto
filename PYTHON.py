print("-----------BOLETA DE ENTREGA-------------")
monto = int(input("Ingrese el monto del producto adquerido: "))
while (monto < 0 ):
    print("Error!!!!, volver a ingresar el monto")
    print(int(input("Ingrese el monto del producto adquerido: ")))    
    
print(f"s/  {monto}")
#sacando el igv

igv = monto * 0.18

importe_final = monto + igv

print("------------------------------------------------------")

print(f"El igv es de {igv}")
print (f"Importe final a pagar es de S/ {importe_final}")

if (importe_final > 4000):
    print("Felicidades, se puede llevar un teclado REAPER y mouse REAPER como regalo")
    
elif (importe_final < 4000) and (importe_final >= 2500):
    print("Felicidades, se pude llevar un mouse REAPER de obsequio")
    
else :
    print("Gracias por su compra")
