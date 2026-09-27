contactos = {}


def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el número telefónico: ")

    contactos[nombre] = telefono
    print("Contacto agregado correctamente.\n")


def mostrar_contactos():
    if not contactos:
        print("No hay contactos registrados.\n")
        return

    print("\n--- Lista de contactos ---")
    for nombre, telefono in contactos.items():
        print(f"Nombre: {nombre} | Teléfono: {telefono}")
    print()


def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in contactos:
        print(f"Teléfono de {nombre}: {contactos[nombre]}\n")
    else:
        print("El contacto no existe.\n")


def eliminar_contacto():
    nombre = input("Ingrese el nombre que desea eliminar: ")

    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado correctamente.\n")
    else:
        print("El contacto no existe.\n")


# Menú principal
while True:
    print("===== REGISTRO DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.\n")
