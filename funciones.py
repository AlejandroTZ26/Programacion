# Demostración de los diferentes tipos de funciones
# Argumentos utilizados
# No recibe argumentos
# Recibe argumentos
# Tiene argumentos opcionales
# Retorno de valores
# No retorna valores
# Retorna valores
# Se pueden dar combinaciones de ambos aspectos

# Para declarar funciones se utiliza def

# def nombredefuncion ():
# codigo

# El codigo de la función es obligatorio. Si no hay
# hay codigo por el momento, usar pass

# Si una variable se declara fuera de procedimiento
# se dice que es global 
variableglobal = "Soy global"
# Dentro de las funciones, si se quiere usar la
# variable global, debe anteponerse la palabra
# reservada global

def  pendiente ():
    pasar

def  norecibeargumentos ():
    # Si se comenta la siguiente línea, use la variable 
    # equivalente a declarar una versión local de la 
    # variable; si no se comenta, use la variable
    # implica usar la global 
    # global variableglobal
    variable global = 4
    print ( "No recibe argumentos" )
    imprimir ( variable global )

# Los argumentos se dentro de parentesis en forma
# de lista separada por comas.
def  recibeargumentos ( fname , lname ):
    print ( fname  +  ""  +  lname )
    imprimir ( variable global )

# Un argumento es opcional cuando le asignas un valor 
# al momento de su declaracion.
# Los argumentos opcionales siempre van al final de la 
# lista de argumentos.
def  argumentosopcionales ( ciudad , país  =  "México" ):
    print ( "Soy de"  +  ciudad  +  ","  +  país )

# Si se especifica return, la funcion retorna valores 
# Cuidar que el flujo del programa siempre los retorne
# Se debe utilizar como expresion, atendiendo el 
# retorno correspondiente
def  elevoalcuadrado ( x ):
  volver  x  *  x

def  main ():
    # norecibeargumentos ()
    # recibeargumentos ("Felipe", "Ramirez")
    # argumentosopcionales ("Monterrey")
    # argumentosopcionales ("Nueva York", "Estados Unidos")
    imprimir ( elevoalcuadrado ( 4 ))