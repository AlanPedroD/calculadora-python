def calculadora(opcao, n1, n2):
    if opcao == '1':
        return n1 + n2
    elif opcao == '2':
        return n1 - n2
    elif opcao == '3':
        return n1 * n2
    elif opcao == '4':
        return round(n1 / n2, 2)

opcao = None
while opcao != '0':
    opcao = input('Escolha uma opção:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\n')

    if opcao in ['1', '2', '3', '4']:
        primeiro_numero = float(input('Digite o primeiro número: '))
        segundo_numero = float(input('Digite o segundo número: '))
        resultado = calculadora(opcao, primeiro_numero, segundo_numero)
        print(f'Resultado: {resultado}')
    elif opcao == '0':
        print('Programa finalizado')
    else:
        print('Opção inválida')