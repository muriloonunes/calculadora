import sys
import math 

"__version__ == 1.0"


n1 = float(input("Digite o primeiro numero\n").strip())
n2 = float(input("Digite o segundo numero\n").strip())
operacao = input("Digite a operacao que voce quer realizar\n").strip()

if n1 % 1 == 0 and n2 %1 ==0:
    n1 = int(n1)
    n2 = int(n2)
    
if operacao=="soma" or operacao=="+" or operacao=="sum":
    resultado = n1+n2
    print(f"{n1}+{n2} =",resultado)
elif operacao=="subtracao" or operacao=="-" or operacao=="difference" or operacao=="dif" or operacao=="sub":
    resultado = n1-n2
    print(f"{n1}-{n2} =",resultado)
elif operacao=="multiplicacao" or operacao=="*" or operacao=="product" or operacao=="mul":
    resultado = round(n1*n2)
    print(f"{n1}*{n2} ={resultado:.3f}")
elif operacao=="divisao" or operacao=="/"or operacao=="quotient" or operacao=="div":
    resultado = round(n1/n2)
    print(f"{n1}/{n2} =",resultado)
elif operacao=="potencia" or operacao=="**" or operacao=="power":
    resultado=n1**n2
    print(resultado)
else:
    print("Invalid operation")
