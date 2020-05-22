import csv
import datetime
# Expresiones regulares
import re
#Sistema Operativo
import os
# Las clases que tenemos en clasePIA se ejecutan en este programa
from clasePIA import Contacto
from operator import attrgetter

# Mostraremos los elementos de las lista ejemplo
def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.TELEFONO==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

Contactos = []
#Hacemos las funcione con el csv
with open('contactos_movil.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            NickN=str(row[0])
            Name=str(row[1])
            Email=str(row[2])
            Cell=int(row[3])
            FechNac= datetime.date(*(int(s) for s in row[4].split('-')))
            Gasto= row[5]
            Contactos.append(Contacto(NickN,Name,Email,Cell,FechNac,Gasto))
            #list_temp=Contacto({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},)
        line_count += 1
    print(f'Processed {line_count} lines.')
# Se hace una lista para almacernar.
CuantosElementosHay()

# Agregamos los registros a la lista.
Contactos.append(Contacto("01HA","Alejandro Tellez","AleTZ26@unal.edu.mx",2233445566,datetime.date(year=2001,month=6,day=26),2
500))
Contactos.append(Contacto("02AP","Andre Gignac","AP10@unal.edu.mx",9182736450,datetime.date(year=1985,month=7,day=23),1700))
CuantosElementosHay()

#Menu

LimpiarPantalla = lambda: os.system('cls')

# Empezamos a validar el Txt.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)
#Empezamos con el menu principal
def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
#Acciones de el menu principal
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
#Agregar un contacto
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
#Buscar
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(f"Telefono: {Contactos[indice_obtenido].TELEFONO}")
                    print(f"Nombre: {Contactos[indice_obtenido].NOMBRE}")
                    print(f"Correo: {Contactos[indice_obtenido].CORREO}")
#Opcion Eliminar
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
#Opcion Mostrar
                print("Mostrando Contactos")
                Contactos.sort(key=attrgetter('TELEFONO'),reverse=False)
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(f"Nickname: {contacto.NICKNAME}")
                    print(f"Nombre: {contacto.NOMBRE}")
                    print(f"Email: {contacto.CORREO}")
                    print(f"Telefono: {contacto.TELEFONO}")
                    print(f"Fecha de Nacimiento: {contacto.FECHANACIMIENTO}")
                    print(f"Gastos: {contacto.GASTO}")
#Se imprimen los datos
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()