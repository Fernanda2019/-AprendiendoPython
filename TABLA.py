# TABLA.PY
# AUTOR: MARIA FERNANDA HERRERA TREJO
# FECHA DE CREACION: 19/09/2019

numero=input("Dame un numero del 1 al 19: ")
numero=int(numero)
#LA SENTENCIA FOR EJECUTA UN BLOQUE DE CODIGO UN DETERMINADO NUMERO DE VECES (ACTUA COMO UN BUCLE)
#MIENTRAS SE LE PIDE QUE RECORRA UN RANGO DE VALORES. EN ESTE NO SE LLEGA AL SEGUNDO RANGO SINO 
#UN VALOR ABAJO, EN ESTE CASO DEL 1 AL 20

for i in range(1,21):
#i VA VARIANDO A CADA ALITERACION.
   salida="{} x {} = {}"
   print(salida.format(numero,i,i*numero))
