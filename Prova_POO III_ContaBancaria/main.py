from OpetadoresConta import ContaBancaria

while True:
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar Saldo")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do titular: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        conta = ContaBancaria(nome, saldo_inicial)
        print("Conta criada com sucesso!")
    elif opcao == 2:
        valor = float(input("Digite o valor a ser depositado: "))
        conta.deposito(valor)
        print("Depósito realizado com sucesso!")
    elif opcao == 3:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > conta.saldo:
            print("Saldo insuficiente!")
            continue
        conta.saque(valor)
        print("Saque realizado com sucesso!")
    elif opcao == 4:
        print("Saldo atual: ", conta.exibir_saldo())
    elif opcao == 5:
        break
    else:
        print("Opção inválida!")


