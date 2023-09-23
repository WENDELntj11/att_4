def perimetro_de_area_retangulo():
    print("Vamos calcular perímetro e a área do retângulo\n")

    altura = float(input("Insira a  altura do retângulo:"))
    comprimento = float(input("Digite comprimento do retângulo: "))

    perimetro_retangulo = 2 * (altura+comprimento)
    area_retangulo = altura*comprimento

    return f" O perimetro do retângulo e: {perimetro_retangulo},\n A área do retângulo e: {area_retangulo} "

print(perimetro_de_area_retangulo())