menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> Digite sua opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do deposito desejado: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f} \n"
            print(f"{deposito:.2f} R$ depositado com sucesso!")
            
        else:
            print("Valor de depósito inválido! ")
            

    elif opcao == "2":
        saque = float(input("Digite o valor de saque desejado (limite máx. R$ 500): "))
        
        if (saque > 0) and (saque <= 500) and (saque <= saldo) and (LIMITE_SAQUES > numero_saques):
            saldo -= saque
            extrato += f"Saque de R$ {saque:.2f} \n"
            print(f"R$ {saque:.2f} sacado com sucesso!")
            numero_saques += 1

        elif saque > saldo:
            print("saldo insuficiente para saque...")  
        
        elif saque > 500:
            print("Saque maior que R$ 500 , que é o limite máximo de saque por transação")
        
        elif LIMITE_SAQUES == numero_saques:
            print("Limite de saques diário atingido...")

        else:
            print("Digite um valor válido...")
    
    elif opcao == "3":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print("\n===================== EXTRATO =============================\n")
            print(f"{extrato}")
            print(f"Saldo atual da conta: R$ {saldo:.2f}")
            print("============================================================")
    
    elif opcao == "0":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
