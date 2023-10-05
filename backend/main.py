from connection import create_db_connection, close_db_connection
from products import Product, create_product, read_all_products, update_product, delete_product, manage_products, read_product_by_id

if __name__ == "__main__":
    connection = create_db_connection()
    
    if connection:
        manage_products(connection)
        close_db_connection(connection)
    else:
        print("No se pudo establecer una conexión a la base de d# import categorias")
# import facturacion
# import pedidos
# import products
# import usuario

#Sección Menu en construcción disponible en Sprint 2
def menu_principal():
    menu = True
    while menu == True:
        print("\n•·.·•·.·•·.·•·.·•Menú Principal•·.·•·.·•·.·•·.·•\n")
        print("1. Inicio")
        print("2. Quienes Somos?")
        print("3. Productos")
        print("4. Contacto")
        print("5. Ingresar")
        print("6. Registro")
        print("7. Salir")
        opcion = input("\n⮞ Ingrese una opción: ")

        if opcion == "1":
            print("Sección en construcción")
            pass
        elif opcion == "2":
            print("Sección en construcción")
            pass
        elif opcion == "3":
            print("Sección en construcción")
            pass
        elif opcion == "4":
            print("Sección en construcción")
            pass
        elif opcion == "5":
            print("Sección en construcción")
            pass
        elif opcion == "6":
            print("Sección en construcción")
            pass
        elif opcion == "7":            
            print("Ha salido del programa. ¡Hasta luego!")
            menu = False     
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

