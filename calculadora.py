import sys
import math 

__version__ == "1.1.1"

while True:
    try:
        n1 = float(input("Digite o primeiro numero\n"))
        break
    except ValueError as e:
        print("numero invalido")
        
while True:
    try: 
        n2 = float(input("Digite o segundo numero\n"))
        break
    except ValueError as e:
        print("numero invalido")
        
while True:
    operacao = input("Digite a operação que você quer realizar (+, -, *, /, **)\n")
    if operacao in ["+","-","*", "/", "**",]:
        break
    else:
        print("Operação inválida")

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
        print("não é possível dividir por 0")
        sys.exit(1)
elif operacao=="**":
    resultado=n1**n2
    print(resultado)