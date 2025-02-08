#Definindo variaveis
controle = 0
checagem = 0
resultado = 0
#Iniciando loop while
while controle == 0:
  while checagem == 0:
    #variaveis para obter o valor do usuário
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    #checando se a opção é valida
    operacao = input('Escolha a operação: \n[+]Soma [-]Subtração\n[*]Multiplicação [/]Divisão')
    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
      checagem = 1
    else:
      print('Opção Inválida')
  #Verificando qual a operação escolhida e realizando os calculos
  if operacao == '+':
    resultado = numero1 + numero2
  elif operacao == '-':
    resultado = numero1 - numero2
  elif operacao == '*':
    resultado = numero1 * numero2
  else:
    resultado = numero1  / numero2
  #mostrando na tela
  print(f'{numero1} {operacao} {numero2} = {resultado}')
  break
