lista_numeros_divisiveis_por_7_não_multiplo_de_5 = []


for dividendo in range(2000,3200+1):
    if dividendo % 7 == 0:
        if dividendo % 5 != 0:
            lista_numeros_divisiveis_por_7_não_multiplo_de_5.append(dividendo)

print(lista_numeros_divisiveis_por_7_não_multiplo_de_5)