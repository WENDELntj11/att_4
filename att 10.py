def dicionario():
    dic_n = {}
    while True:
        try:
            numero_inserido = int(input("Digite um número inteiro positivo para n:"))
            if numero_inserido > 0:
                break
            else:
                print("Por favor, Digite o número inteiro positivo válido.\n")
        except ValueError:
            print("Por favor, Digite o número inteiro positivo válido.\n")

    for i in range(1, numero_inserido+1):
        dic_n[i] = i*i

    for mostrar in dic_n:
        print(f"{mostrar} : {dic_n[mostrar]}")



dicionario()