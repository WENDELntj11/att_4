def palindromo(palavra):
    lista_palavra = []

    for i in range(len(palavra)-1, -1, -1):
        char = palavra[i]
        lista_palavra.append(char)

    new_palavra = "".join(map(str, lista_palavra))

    if new_palavra == palavra:
        return f"\n\t Palavra ({palavra}) é um palíndromo.\n"
    else:
        return f"\n\t Palavra ({palavra}) não é um palíndromo.\n"


print(palindromo(input("Por Favor,Digite uma palavra ")))