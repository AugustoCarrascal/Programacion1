def pedir_numero () -> int:
  numero = input("Ingrese un número: ")  
  while not numero.isdigit():  
    print("Número inválido, ingrese nuevamente.")
    numero = input("Ingrese un número: ")
  return int(numero)

