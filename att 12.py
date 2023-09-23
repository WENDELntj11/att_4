def contar_letras_do_seu_nome(texto, nome):
    texto = texto.lower()
    nome = nome.lower()
    contador = 0
    for letra in texto:
        if letra in nome:
            contador += 1
    return contador
seu_nome = input("Por Favor, Digite seu nome:")
texto_inserido = input("Digite um texto:")
numero_de_letras = contar_letras_do_seu_nome(texto_inserido, seu_nome)
print(f"O texto inserido contem{numero_de_letras} letras que tambem estao no seu nome.")