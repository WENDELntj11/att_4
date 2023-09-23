dividendo = int(input("\n\nInsira um numero inteiro:"))
print("Todos os seus divisores:")
lista_divisor = []
for divisor in range(1,dividendo+1):
    if dividendo %divisor == 0:
        lista_divisor.append(divisor)
print(lista_divisor)