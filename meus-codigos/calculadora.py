def adicionar (x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, Y):
    return x / y 

print("selecione  a operação")
print("1. Adição")
print("2. Subtração")
print("3. multiplicação")
print("4.Divisão")

escolha = input("digite o número da operação (1/2/3/4): ")

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo número: "))

if escolha == '1':
    print("resultado:", adicionar(num1, num2))
elif escolha == '2':
    print("resultado:", subtrair(num1, num2))
elif escolha == '3':
    print("Resultado:", multiplicar(num1, num2))
elif escolha == '4':
    print("resultado:", dividir(num1, num2))
else:
    print("operação inválida")