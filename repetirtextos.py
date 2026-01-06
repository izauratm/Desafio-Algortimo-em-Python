#2. Solicitar uma string e um número inteiro como entrada e depois retornar essa string repetida com o numero de vezes informado:

def repetir_texto():
    texto = input("Digite uma string: ")
    numero = int(input("\nDigite um número inteiro: "))
    return (texto + ' ') * numero

print(repetir_texto())