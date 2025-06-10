from SistemaDeRP import *

usuario1 = ["pan", "leche", "café", "manteca", "pantalon de boca"]
usuario2 = ["café", "azúcar", "leche", "café", "remera de boca"]

opcion = 0
while opcion != 5:
    print("\n🔎 ANÁLISIS DE HISTORIAL DE COMPRAS")
    print("1. Mostrar productos en común")
    print("2. Mostrar productos exclusivos de cada usuario")
    print("3. Mostrar catálogo total de productos")
    print("4. Mostrar recomendaciones para cada usuario")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            comunes = productos_en_comun(usuario1, usuario2)
            print("Productos en común:", comunes)
        case 2:
            exclusivos1 = productos_exclusivos(usuario1, usuario2)
            exclusivos2 = productos_exclusivos(usuario2, usuario1)
            print("Productos exclusivos del usuario 1:", exclusivos1)
            print("Productos exclusivos del usuario 2:", exclusivos2)
        case 3:
            catalogo = catalogo_total(usuario1, usuario2)
            print("Catálogo total de productos:", catalogo)
        case 4:
            recomendaciones(usuario1, usuario2)
        case 5:
            print("Saliendo del programa....")
        case _:
            print("Opción inválida, intente nuevamente.")