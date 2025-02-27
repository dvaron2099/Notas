def tabla_multiplicar(numero):
    header = f"# Tabla del {numero} #"
    print(header)
    for i in range(1, 11):
        multi = i * numero
        print(f"{i} x {numero} = {multi}")

tabla_multiplicar(2)
