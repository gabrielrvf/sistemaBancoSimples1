# Definição de variáveis iniciais
saldo = 5000  # Saldo inicial da conta

tesouro_direto = 5.75  # Taxa de rendimento do Tesouro Direto (% ao mês)
poupanca = 1.30  # Taxa de rendimento da Poupança (% ao mês)
cdb = 20.52  # Taxa de rendimento do CDB (% ao mês)

resposta = "s"  # Variável de controle para continuar ou encerrar o programa
limite_saque = 2000  # Limite diário de saque
nome = "Gabriel Rosa"  # Nome do cliente

# Exibição das informações iniciais do banco e do cliente
print("\n------------------------------------\n")
print("-- BANCO DA UDF --\n\nCliente: ", nome, "\nSaldo: R$", saldo, "\nLimite de Saque: R$", limite_saque)

# Loop principal para permitir múltiplas operações
while resposta == "s" or resposta == "S":
    print("\n------------------------------------\n")
    # Pergunta ao usuário qual operação deseja realizar
    pergunta = input("Você deseja fazer saque, deposito ou investimento? (s/d/i) ")

    # Opção de saque
    if pergunta == "s" or pergunta == "S":
        saque = float(input(f"Escreva o valor do saque (LIMITE R${limite_saque} / SALDO R${saldo}): "))
        
        # Verifica se o saldo é suficiente
        if saldo - saque < 0:
            print("! OPERAÇÃO INVÁLIDA, SALDO INSUFICIENTE")
        # Verifica se o valor do saque está dentro do limite permitido
        elif saque > limite_saque:
            print("! OPERAÇÃO INVÁLIDA, LIMITE DE SAQUE DIÁRIO ATINGIDO")
        else:
            saldo -= saque  # Atualiza o saldo
            limite_saque -= saque  # Reduz o limite de saque diário
            print("\nSUCESSO AO SACAR.\nSEU NOVO SALDO É DE R$", saldo, "\nLIMITE PARA SAQUE: R$", limite_saque)
    
    # Opção de depósito
    elif pergunta == "d" or pergunta == "D":
        deposito = float(input("Escreva o valor do deposito: "))
        saldo += deposito  # Atualiza o saldo com o depósito
        print("\nSUCESSO AO DEPOSITAR.\nSEU NOVO SALDO É DE R$", saldo)
    
    # Opção de investimento
    elif pergunta == "i" or pergunta == "I":
        print("\n------------------------------------\n")
        # Pergunta ao usuário onde deseja investir
        investir = input(f"Para qual área deseja fazer investimento de 1 mês?\nSALDO: R${saldo}\n\n1 - Tesouro Direto ({tesouro_direto}% /mês)\n2 - Poupança ({poupanca}% /mês)\n3 - CDB ({cdb}% /mês)\n0 - CANCELAR\n")
        
        # Aplicação no Tesouro Direto
        if investir == "1":
            saldo *= (1 + (tesouro_direto / 100))  # Atualiza o saldo aplicando os juros
            print("\nSUCESSO COM SEU INVESTIMENTO NO TESOURO DIRETO.\nSALDO ATUALIZADO: R$", saldo)
        # Aplicação na Poupança
        elif investir == "2":
            saldo *= (1 + (poupanca / 100))  # Atualiza o saldo aplicando os juros
            print("\nSUCESSO COM SEU INVESTIMENTO NA POUPANÇA.\nSALDO ATUALIZADO: R$", saldo)
        # Aplicação no CDB
        elif investir == "3":
            saldo *= (1 + (cdb / 100))  # Atualiza o saldo aplicando os juros
            print("\nSUCESSO COM SEU INVESTIMENTO NO CDB.\nSALDO ATUALIZADO: R$", saldo)
        else:
            print("! RESPOSTA DE INVESTIMENTO INVÁLIDA")
    
    # Caso o usuário digite uma opção inválida
    else:
        print("! RESPOSTA INVÁLIDA")
    
    # Pergunta se o usuário deseja continuar utilizando o programa
    resposta = input("\nDeseja fazer outra operação? (s/n) ")

# Finaliza o programa
print("\nPROGRAMA FINALIZADO COM SUCESSO!")
