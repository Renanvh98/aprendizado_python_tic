def calculadora ():
    while True:
        print ("Calculadora Simples")
        print()
        print("1. SOMA")
        print("2. SUBTRAÇÃO")
        print("3. MULTIPLICAÇÃO")
        print("4. DIVISÃO")
        print("S. SAIR")
        operacao = input("selecione uma opção ou 'S' para sair:")

        if operacao == 's' or operacao == 'S':
            print ("obrigado por utilizar a calculadora")
            break

        if operacao not in ['1', '2', '3', '4']:
            print ("não valido")
            continue

        numero_1 = float (input("Digite o primeiro numero: "))
        numero_2 = float (input("Digite o segundo numero: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado soma é: ", resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado subtração é: ", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado multi é: ", resultado)
        else :
            if numero_2 == 0:
                print("Divisões por zero não são possiveis")
                continue
            else: 
                resultado = numero_1 / numero_2
                print("o resultado div é: ", resultado)

calculadora()