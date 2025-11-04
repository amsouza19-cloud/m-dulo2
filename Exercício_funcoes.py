1.
def saldação ()
print ("Olá Mundo, bem vindo ao Python!")

2.
def dobro (número):
    return número *2
    print (dobro(4))
    print (dobro(15))
    print (dobro(30))

3.
def soma (a, b):
return  a + b
    print (soma (8, 8))

4.
def mensagem ("nome = visitante"):
    print (f"olá, {nome}!")
    mensagem ("joão")
    mensagem()

5.
def operações (a, b):
    soma = a + b
    subitração = a - b
    multiplicação = a * b
    return, soma, subitração, multiplicação
    resultado igual operações (9, 5)
    print ("soma:", resultado [0])
    print ("subitração:", resultado [1])
    print ("multiplicação:", resultado[2])

6.
def media (*números):
    return sum (números) / len(números)
    print (media(10, 20, 30))
    print (mrdia (5, 15, 25, 35, 45))
    print (media (2, 4, 6, 8, 10, 12, 14))

7.
def dados_pessoais (**info):
    for chave, valor in info.items():
        print (f"{chave.capitalize()}: {valor}")
        dados_pessoais (nome="Ana", Idade=40, cidade="Jaboatão")

8.
def calculadora():
    def soma(a, b): return a + b
    def subtrair(a, b): return a - b
    def multiplicar(a, b): return a * b
    def dividir(a, b):
        return "erro: divisão por zero" if b == 0 else a / b
    print("escolha a opção: +, -, *, /")
    op = input("operação:")
    a = float(input("digite o primeiro número:"))
    b = float(input("Digite o segundo número:"))

    if op == '+':
        print("resultado:", soma (a, b))
    elif op == '-':
        print("Resultado:", subtrair(a,b))
    elif op == '*':
        print("Resultado:", multiplicar(a,b))
    else op == '/':
        print("Operação Inválida.")
    calcular ()

9.
def aplicar_operação(a, b, funcao):
    return funcao(a, b)

def soma(a, b):
    return a + b

def multiplicação(a, b):
    return a *b

print(aplicar_operação(3, 4, soma))
print(aplicar_operação(3, 4, multiplicação))
