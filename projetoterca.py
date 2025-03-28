saldo = 5000
tesouro_direto = 5.75
poupanca = 1.30
cdb = 20.52
resposta = "s"
limite_saque = 2000
nome = "Gabriel Rosa"

print("\n------------------------------------\n")
print("-- BANCO DA UDF --\n\nCliente: ", nome, "\nSaldo: R$", saldo, "\nLimite de Saque: R$", limite_saque)

while resposta == "s" or resposta == "S":

  print("\n------------------------------------\n")
  pergunta = input("Você deseja fazer saque, deposito ou investimento? (s/d/i) ")

  if pergunta == "s" or pergunta == "S":
     saque = float(input(f"Escreva o valor do saque (LIMITE R${limite_saque} / SALDO R${saldo}): "))
     if saldo - saque < 0:
        print("! OPERAÇÃO INVÁLIDA, SALDO INSUFICIENTE")
     elif saque > limite_saque:
        print("! OPERAÇÃO INVÁLIDA, LIMITE DE SAQUE DIÁRIO ATINGIDO")
     else:
        saldo = saldo - saque
        limite_saque -= saque
        print("\nSUCESSO AO SACAR.\nSEU NOVO SALDO É DE R$", saldo, "\nLIMITE PARA SAQUE: R$", limite_saque)
  elif pergunta == "d" or pergunta == "D":
     deposito = float(input("Escreva o valor do deposito: "))
     saldo = saldo + deposito
     print("\nSUCESSO AO DEPOSITAR.\nSEU NOVO SALDO É DE R$", saldo)
  elif pergunta == "i" or pergunta == "I":
      print("\n------------------------------------\n")
      investir = input(f"Para qual área deseja fazer investimento de 1 mês?\nSALDO: R${saldo}\n\n1 - Tesouro Direto ({tesouro_direto}% /mês)\n2 - Poupança ({poupanca}% /mês)\n3 - CDB ({cdb}% /mês)\n0 - CANCELAR\n")
      if investir == "1":
        saldo = saldo * (1 + (tesouro_direto / 100))
        print("\nSUCESSO COM SEU INVESTIMENTO NO TESOURO DIRETO.\nSALDO ATUALIZADO: R$", saldo)
      elif investir == "2":
        saldo = saldo * (1 + (poupanca / 100))
        print("\nSUCESSO COM SEU INVESTIMENTO NA POUPANÇA.\nSALDO ATUALIZADO: R$", saldo)
      elif investir == "3":
        saldo = saldo * (1 + (cdb / 100))
        print("\nSUCESSO COM SEU INVESTIMENTO NO CDB.\nSALDO ATUALIZADO: R$", saldo)
      else:
        print("! RESPOSTA DE INVESTIMENTO INVÁLIDA")
  else:
     print("! RESPOSTA INVÁLIDA")
  resposta = input("\nDeseja fazer outra operação? (s/n) ")

print("\nPROGRAMA FINALIZADO COM SUCESSO!")
