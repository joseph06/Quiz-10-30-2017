def generar_secuencia():
    impar = 1
    while True:
        yield impar
        impar = impar + 2


if __name__ == "__main__":
    generador = generar_secuencia()

    impar = generar_secuencia()
    for n in impar:
        print(n)
        if n > 14:
            break