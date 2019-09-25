# ACUMULADO.PY
# AUTOR: MARIA FERNANDA HERRERA FERNANDA 
# FECHA DE CREACION: 19/09/2019

acumulado=int(0)
numero=str("")
# AL USAR TRUE COMO CONDICION EN WHILE, SE FORMARA UN BUCLE INFINITO HASTA QUE DE FORMA EXPLICITA 
#SE USE LA INSTRUCCION BREAK

while True:
    numero=input("Dame un numero: ")
    if numero=="":
        #SI EL NUMERO ES VACIO LO REPORTA Y SALE DE LA INSTRUCCION 
        print("Vacio. Salida del programa.")
        break
    else:
        # SI SE PROPORCIONO VALOR, ACUMULADO = ACUMULADO + NUMERO 
        #SE REALIZA EL CALCULO USANDO SUMA INCLUYENTE (+=)
        acumulado+=int(numero)
        Salida="Monto acumulado: {}"
        print(Salida.format(acumulado))