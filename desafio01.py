menu = """
[c] Criar Conta
[l] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas = []
clientes = []

while True:

    opcao = input(menu)
    
    if opcao == "c":
        def criar_conta():
            nome_cliente = input("Digite o nome do cliente: ")
            cpf_cliente = input("Digite o CPF do cliente: ")
            if cpf_cliente != "":
                print("Vamos cadstrar o seu endereço:")
                rua_cliente = input("Digite o nome da rua: ")
                numero_cliente = input("Digite o número: ")
                
                clientes.append({
                    "nome": nome_cliente,
                    "cpf": cpf_cliente,
                    "endereco": {
                        "rua": rua_cliente,
                        "numero": numero_cliente
                    }
                })
                
                contas.append({
                    "cpf": cpf_cliente,
                    "saldo": 0
                })
        criar_conta()
        
    if opcao == "l":
        def listar_contas():
            for conta in contas:
                if conta == "":
                    print("Nenhuma conta cadastrada.")
                else:    
                    print(f"CPF: {conta['cpf']}")
                    print(f"Saldo: R$ {conta['saldo']:.2f}")
                    print("-------------------")
        listar_contas()        
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")