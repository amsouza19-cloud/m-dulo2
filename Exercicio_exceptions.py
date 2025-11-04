1.
try:
    numero = int(input("digite um número inteiro:"))
    printe(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: valor digitado não é um número inteiro:")

2.
try:
    a = float(input("digite o primeiro número: "))
    b = float(input("digite o segundo número: "))
    print(f"Resultado da multiplicação:{a * b}")
except ValueError:
        print("Erro: por favor, digite apenas números!")

3.
try:
    n = int(input("Digite um número inteiro: "))
except ValueError:
        print("Erro: isso não é um número inteiro!")
else:
        print(f"Perdeito! Você digitou o numero {n} corretamente.")

4.
try:
    aruivo = open("dados.txt", "r")
    print("Arquivo não encontrado.")
finally:
    print("Encerrando programa...")

5.
def dividir(a,b):
    if b == 0:
        raise ZeroDivisionErro("Erro: divid]ao por zero não permitida!")
    return a / b

try:
    print(dividir(10, 2))
    print(dividir(8, 0))
except ZeroDivisionError as e:
    print(e)

6.
class IdadeInvalidaError(exception):
    pass 

def cadastrar_idade(idadae):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa!")

try:
    cadastrar_idade(-5)
except IdadeInvalidaError as e:
    print("Erro:", e)

7.
try:
    n1 = float(input("digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = n1 / n2
except ValueError:
    print("Erro: entrada inválida! Digite apenas números.")
except ZeroDivisionError:
    print("Erro: entrada inválida! Digite apenas números.")
else:
    print(f"Resultado da divisão: {resultado}")

8.
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Rrro: entrada Inválida!")
else:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("o número é impar.")
finally:
    print("Fim do programa.")

9.
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo Insuficiente para saque!")
    return saldo - valor

try:
    novo_saldo = sacar(1000, 1200)
    print(f"saque realizado. Novo saldo: R$ {novo_saldo}")
except SaldoInsuficienteError as e:
    print("Erro:", e)
