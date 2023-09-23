def somar_numeros_rangen(numero):
    soma_n = 0
    for n in range(1, numero+1):
        soma_n +=n

    return soma_n

while True:
    numero = int(input("\n\t Insira um número inteiro positivo:"))
    if numero > 0:
        print(f"soma de todos os números inteiros positivos entre 1 e {numero} e: {somar_numeros_rangen(numero)}")
        break