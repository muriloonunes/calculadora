import sys
import math
import locale

__version__ = "1.2"

traducoes = {
    "en": {
        "Digite o primeiro numero\n": "Enter the first number\n",
        "Digite o segundo numero\n": "Enter the second number\n",
        "Digite a operação que você quer realizar (+, -, *, /, **)\n": "Enter the operation you want to perform (+, -, *, /, **)\n",
        "Número inválido\n": "Invalid number\n",
        "Operação inválida\n": "Invalid operation\n",
        "Não é possível dividir por 0\n": "Cannot divide by 0\n",
    },
    "pt": {
        "Digite o primeiro numero\n": "Digite o primeiro número\n",
        "Digite o segundo numero\n": "Digite o segundo número\n",
        "Digite a operação que você quer realizar (+, -, *, /, **)\n": "Digite a operação que você deseja realizar (+, -, *, /, **)\n",
        "Número inválido\n": "Número inválido\n",
        "Operação inválida\n": "Operação inválida\n",
        "Não é possível dividir por 0\n": "Não é possível dividir por 0\n",
    }
}

idioma_sistema = locale.getdefaultlocale()[0][:2]

traducoes_selecionadas = traducoes.get(idioma_sistema, traducoes["en"])

while True:
    try:
        n1 = float(input(traducoes_selecionadas["Digite o primeiro numero\n"]))
        break
    except ValueError as e:
        print(traducoes_selecionadas["Número inválido\n"])
        
while True:
    try: 
        n2 = float(input(traducoes_selecionadas["Digite o segundo numero\n"]))
        break
    except ValueError as e:
        print(traducoes_selecionadas["Número inválido\n"])
        
while True:
    operacao = input(traducoes_selecionadas["Digite a operação que você quer realizar (+, -, *, /, **)\n"])
    if operacao in ["+","-","*", "/", "**",]:
        break
    else:
        print(traducoes_selecionadas["Operação inválida\n"])

if n1 % 1 == 0 and n2 % 1 == 0:
    n1 = int(n1)
    n2 = int(n2)
    
if operacao=="+":
    resultado = n1+n2
    print(f"{n1} + {n2} = ",resultado)
elif operacao=="-":
    resultado = n1-n2
    print(f"{n1} - {n2} = ",resultado)
elif operacao=="*":
    resultado = (n1*n2)
    print(f"{n1} * {n2} = {resultado:.3f}")
elif operacao=="/":
    try:
        resultado = (n1/n2)
        print(f"{n1} / {n2} = ",resultado)
    except ZeroDivisionError as e:
        print(traducoes_selecionadas["Não é possível dividir por 0\n"])
        sys.exit(1)
elif operacao=="**":
    resultado=n1**n2
    print(resultado)