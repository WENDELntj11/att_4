import math 

def volume_da_esfera():
    raio_esfera = float(input("Digite o valor do raio de uma esfera em m:"))

    volume = (4/3)*math.pi*(raio_esfera**3) 

    volume_litros = volume * 1000  
    
    return f"O volume da esfera é aproximadamente {volume_litros:.2f} litros."


print(volume_da_esfera())