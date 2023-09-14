import math

def calcular_volume_cilindro(raio, altura):
    area_base = math.pi * raio**2
    volume = area_base * altura
    return volume

raio = float(input("Digite o valor do raio do cilindro em metros: "))
altura = float(input("Digite o valor da altura do cilindro em metros: "))

volume_cilindro = calcular_volume_cilindro(raio, altura)
print("O volume do cilindro é:", volume_cilindro, "metros cúbicos")

def calcular_quantidade_agua(volume_cilindro):
    densidade_agua = 1000  # densidade da água em kg/m³
    quantidade_agua = volume_cilindro * densidade_agua
    return quantidade_agua

quantidade_agua = calcular_quantidade_agua(volume_cilindro)
quantidade_litros = quantidade_agua / 1000
print("A quantidade de água no cilindro é:", quantidade_agua, "quilogramas ou:", quantidade_litros, "litros")
