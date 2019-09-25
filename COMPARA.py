# COMPARA.PY
# AUTOR: FERNANDA HERRERA
# FECHA DE CREACION: 19/09/2019

"Dame dos cantidades: "
numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."

if (numero1==numero2):
#ENTRA A ESTA LINEA SI LOS NUMEROS CAPTURADOS SON IGUALES
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    #CONDICIONALES ANIDADOS UN IF DENTRO DE OTRO IF.
    #SI LOS NUMEROS NO SON IGUALES 
    if numero1>numero2:
        #ESTA LINEA SE EJECUTA SI EL PRIMER NUMERO ES MAYOR QUE EL SEGUNDO 
        print(salida.format(numero1, numero2,"El mayor es el primero"))

    else:
        #DE SER LO CONTRARIO, SE CORRERA ESTA LINEA SI EL SEGUNDO ES MAYOR QUE EL PRIMERO 
        print(salida.format(numero1, numero2, "El mayor es el segundo"))