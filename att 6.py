fatorar = int(input("Insira um número positivo:"))

if fatorar < 0:
    print("Por favor, insira um número positivo.")
elif fatorar == 0:
    print("O fatorial de 0 é 1.")
else:
    numfat = 1
    for fat in range(fatorar, 1, -1):
        numfat = numfat * fat

    print(f"O fatorial de {fatorar} é {numfat}")