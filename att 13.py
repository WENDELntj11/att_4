import math

def entrada_numero(mensagem,tipo):
    while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Digite a entrada corretamente! \n")



numero = entrada_numero("Digite um numero inteiro",int)
while numero < 0:
    numero = entrada_numero("Digite um numero inteiro positivo",int)



raiz_quadrada = math.sqrt(numero)
print(f"Raiz quadra de {numero} = {raiz_quadrada:.3f}")