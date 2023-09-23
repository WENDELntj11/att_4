def input_numero(mensagem,tipo): 
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Digite uma entrada corretamente! \n")

def fibonacci(qt_fibi):
    lista_fibonacci = [0,1]

    if qt_fibi < 2:
        return lista_fibonacci[0]
    
    sequencia =2
    while sequencia < qt_fibi:
        sequencia +=1
        fibi = lista_fibonacci[-2] + lista_fibonacci[-1]
        lista_fibonacci.append(fibi)
    
    return ", ".join(map(str, lista_fibonacci))

print(fibonacci(input_numero('Quantos números de Fibonacci o usuario deseja ver? ',int)))