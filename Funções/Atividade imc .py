"""
Escreva um programa que solicite ao utilizador o fornecimento do seu peso em Kg e de sua altura em m e a partir deles calcule o índice de massa corpórea do utilizador.

"""
import os
os.system("cls || clear")

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))


def calculo_imc(n1,n2):
    imc = n1 / (pow(n2, 2))

    return imc



def verificando_imc(imc):
    if imc < 18.5:
        return """Abaixo do peso \nConsulte um nutricionista para orientação"""
    elif imc >= 18.5 and imc < 24.9:
        return """Peso normal \nMantenha hábitos saudáveis!"""
    elif imc >= 25 and imc < 29.9:
        return """Sobrepeso \nConsidere uma dieta balanceada e atividade física"""
    elif imc >= 30 and imc < 34.9:
        return """Obesidade grau 1 \nProcure orientação de um profissional de saúde"""  
    elif imc >= 35 and imc < 39.9:
        return """Obesidade grau 2 \nConsulte um médico para avaliação e orientação"""  
    elif imc >= 40:
        return """Obesidade grau 3 \nBusque assistência médica imediatamente"""  
    
imc = calculo_imc(peso, altura)
calssificacao = verificando_imc(imc)


print(f"Seu IMC é: {imc:.2f}")
print(f"{calssificacao}")


