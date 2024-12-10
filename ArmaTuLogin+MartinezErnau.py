"""
Consigna.
Para tu primera entrega, te proponemos que crees un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. 
Hazlo utilizando el concepto de funciones, diccionarios, bucles y condicionales.

Objetivos
Practicar el concepto de funciones.
Desarrollar la parte lógica para el registro de usuarios.

Requisitos
Diccionarios (guardado de datos)
Input (solicitud de datos)

Variables

If (chequeo de datos)

While (iteración para el programa, sea para agregar, loguear o mostrar)

For (recorrer datos y para búsqueda)

Print

Funciones separadas para registro, almacenamiento y muestra

Recomendaciones
El formato de registro es: Nombre de usuario y Contraseña.

Utilizar una función para almacenar la información y otra función para mostrar la información.

Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).

Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

Formato
El proyecto debe compartirse utilizando Colab bajo el nombre “ArmaTuLogin+Apellido”, por ejemplo “ArmaTuLogin+Fernandez”


"""
##############################################################

def login_create(user,password):
    if users.get(user):
       print("El usuario ya existe")
    else:
       users[user] = password
       print("Usuario creado exitosamente")

    return

def login_validation(user,password):
    
    if users.get(user) == password:
        print("Sesión iniciada correctamente !!!! ")
    else:
         print("Usuario o contraseña inválidos.")
     
    return   

def login_list():
    for user, password in users.items():
        print(f"USUARIO: {user} - CONTRASEÑA: {password}")
    return

##############################################################

def main():

    while True:

        print()

        print("LOGIN OPERATIONS:")
        print("1. Login")
        print("2. Crear Login")
        print("3. Listar Logins")
        print("0. Exit")

        print()
        operacion = input("Ingrese número de operación: ")

        if operacion == '1':
            user = input("Ingrese nombre usuario: ")
            password = input("Ingrese contraseña: ")

            print()

            login_validation(user,password)

        elif operacion == '2':
            user = input("Ingrese nombre usuario: ")
            password = input("Ingrese contraseña: ")

            print()

            login_create(user,password)

        elif operacion == '3':
            print()

            login_list()

        elif operacion == '0':
            break

        else: 
            print()
            print ("Operación inválida.")

    return

users = {}
main()
