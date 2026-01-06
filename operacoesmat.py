#3. solicitar 2 numeros como entrada e depois retornar uma operação matemática simples entre eles:

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação matemática (+, -, *, /): ")
if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: Divisão por zero não é permitida.")