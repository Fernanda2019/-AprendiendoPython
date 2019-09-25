# TABLAS.PY
# AUTOR: MARIA FERNANDA HERRERA TREJO 
# FECHA DE CREACION: 19/09/2019

for i in range(1,21):
    Encabezado="Tabla del {}"
    print(Encabezado.format(i))
#ESTE PRINT NO CONTIENE ARGUMENTOS ES SOLO UN SALTO DE LINEA
    print()
#DENTRO DE UNA SENTENCIA DE FOR SE PUEDE ANIDAR OTRA 
#SENTENCIA IGUAL O DIFERENTE EN ESTE CASO SE ANIDA DE NUEVO LA SENTENCIA FOR 
    for j in range(1,21):
        #AQUI i CONTIENE EL NUMERO BASE DE LA TABLA Y J EL ELEMENTO DE LA TABLA 
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))

    else:
        #AL TERMINAR CON LAS ITERACIONES SE EJECUTA UN SALTO DE LINEA.
        print()
