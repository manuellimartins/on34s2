valor1=int (input ("Digite o primeiro valor: "))
valor2=int (input("Digite o segundo valor: "))

Soma= valor1+valor2
print("Resultado da soma:", Soma)
eh_impar=Soma%2
print("O número",Soma,"é impar?" ,bool(eh_impar))


Subtracao= valor1-valor2
print("Resultado da subtração:", Subtracao)
eh_impar=Subtracao%2
print("O número",Subtracao,"é impar?" ,bool(eh_impar))


Multiplicacao= valor1*valor2
print("Resultado da multiplicação:", Multiplicacao)
eh_impar=Multiplicacao%2
print("O número", Multiplicacao,"é impar?" ,bool(eh_impar))


Divisão= valor1/valor2
print("Resultado da divisão:", Divisão)
eh_impar=Divisão%2
print("O número",Divisão,"é impar?" ,bool(eh_impar))


Potenciação= valor1**valor2
print("Resultado da potenciação:", Potenciação)
eh_impar=Potenciação%2
print("O número",Potenciação,"é impar?" ,bool(eh_impar))
