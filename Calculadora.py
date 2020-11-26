#Cabeçalho da calculadora (Apresentação)
print("************************************************************************")
print("******************** BEM VINDO A CALCULADORA PYTHON ********************")
print("************************************************************************")

# Agora definimos as operações que serão possíveis de se realizar e seus respectivos números para escolha do usuário
print("Selecione o tipo de operação que deseja realizar: ")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
operacao = int(input("Digite a opção que deseja (1/2/3/4): "))

#Aqui o usuário ira digitar os números que desejar
num = int(input("Digite o primeiro número: "))
num1 = int(input ("Digite o segundo número: "))
resultado = 0

#Configuração de cada opção da calculadora
if operacao == 1:
    resultado = num + num1
    print("O resultado da soma entre os números %s e %r foi:" %(num, num1), resultado)
elif operacao == 2:
    resultado = num - num1
    print("O resultado da subtração entre os números %s e %r foi:" %(num, num1), resultado)
elif operacao == 3:
    resultado = num * num1
    print("O resultado da multiplicação entre os números %s e %r foi:" %(num, num1), resultado)
elif operacao == 4:
    resultado = num / num1
    print("O resultado da divisão entre os números %s e %r foi:" %(num, num1), resultado)
else:
    print("Operação não identificada")

#Aqui o usuário ira decidir se vai continuar usando a calculadora
pergunta = input("Deseja realizar outra operação? (S/N): ")

#Caso a resposta for Não, o programa ira fechar e reproduzir a mensagem a seguir
if pergunta == "N":
    print("Obrigado por utilizar minha calculadora, até a proxima")

#Se a resposta for Sim, a calculadora ira rodar com todos os comandos até o loop ser finalizado pelo usuário (Responder N)
while pergunta == "S":
    if (pergunta == "S"):
        print("Selecione o tipo de operação que deseja realizar: ")
        print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
        operacao = int(input("Digite a opção que deseja (1/2/3/4): "))

        num = int(input("Digite o primeiro número: "))
        num1 = int(input("Digite o segundo número: "))
        resultado = 0

        if operacao == 1:
            resultado = num + num1
            print("O resultado da soma entre os números %s e %r foi:" % (num, num1), resultado)
        elif operacao == 2:
            resultado = num - num1
            print("O resultado da subtração entre os números %s e %r foi:" % (num, num1), resultado)
        elif operacao == 3:
            resultado = num * num1
            print("O resultado da multiplicação entre os números %s e %r foi:" % (num, num1), resultado)
        elif operacao == 4:
            resultado = num / num1
            print("O resultado da divisão entre os números %s e %r foi:" % (num, num1), resultado)
        else:
            print("Operação não identificada")

        #Se o usuário quiser encerrar o loop, ira apenas apertar a tecla "N" e o programa ira fechar
        pergunta = input("Deseja realizar outra operação? (S/N): ")
        if (pergunta == "N"):
                print("Obrigado por utilizar minha calculadora, até a proxima")