def conteo_digitos(numero):
  print(f'Secuencia: {"".join([str(num) for num in range(1, numero + 1)])}')
  return len("".join([str(num) for num in range(1, numero + 1)]))


if __name__ == "__main__":
    import sys

    try:
        numero = int(sys.argv[1])
        digitos_totales = conteo_digitos(numero)
        print(f"El número {numero} tiene {digitos_totales} dígitos consecutivos")
    except:
        print("Es necesario pasar un un número como parámetro.")