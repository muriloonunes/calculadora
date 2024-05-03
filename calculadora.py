import sys
import math 

"__version__ == 1.1"

while True:
    try:
        n1 = float(input("Digite o primeiro numero\n").strip())
        break
    except ValueError as e:
        print("numero invalido")
        
while True:
    try: 
        n2 = float(input("Digite o segundo numero\n").strip())
        break
    except ValueError as e:
        print("numero invalido")
        
while True:
    operacao = input("Digite a operação que você quer realizar\n").strip().lower()
    if operacao in ["soma", "+", "sum", "subtracao", "-", "difference", "dif", "sub",
                    "multiplicacao", "*", "product", "mul", "divisao", "/", "quotient", "div",
                    "potencia", "**", "power"]:
        break
    else:
        print("Operação inválida")

if n1 % 1 == 0 and n2 % 1 == 0:
    n1 = int(n1)
    n2 = int(n2)
    
if operacao=="soma" or operacao=="+" or operacao=="sum":
    resultado = n1+n2
    print(f"{n1}+{n2} =",resultado)
elif operacao=="subtracao" or operacao=="-" or operacao=="difference" or operacao=="dif" or operacao=="sub":
    resultado = n1-n2
    print(f"{n1}-{n2} =",resultado)
elif operacao=="multiplicacao" or operacao=="*" or operacao=="product" or operacao=="mul":
    resultado = (n1*n2)
    print(f"{n1} * {n2} = {resultado:.3f}")
elif operacao=="divisao" or operacao=="/"or operacao=="quotient" or operacao=="div":
    try:
        resultado = (n1/n2)
        print(f"{n1}/{n2} =",resultado)
    except ZeroDivisionError as e:
        print("não é possível dividir por 0")
        sys.exit(1)
elif operacao=="potencia" or operacao=="**" or operacao=="power":
    resultado=n1**n2
    print(resultado)