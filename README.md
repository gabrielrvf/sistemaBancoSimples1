# Banco da UDF - PYTHON

## Descrição
Este é um programa simples de simulação bancária em Python que permite ao usuário realizar operações básicas como saque, depósito e investimento. O programa inicia com um saldo predefinido e um limite de saque diário, interagindo com o usuário por meio de entradas no console.

## Funcionalidades
- **Saque:** O usuário pode sacar um valor, desde que esteja dentro do saldo e do limite de saque diário.
- **Depósito:** O usuário pode adicionar fundos ao saldo.
- **Investimento:** Opções de investimento em Tesouro Direto, Poupança e CDB, com rendimentos aplicados ao saldo.
- **Controle de saldo e limite de saque:** O programa impede operações inválidas devido a falta de saldo ou ultrapassagem do limite.
- **Execução em loop:** O usuário pode realizar múltiplas operações até decidir encerrar.

## Como Usar
1. Execute o script em um ambiente Python.
2. Escolha entre as opções de saque (s), depósito (d) ou investimento (i).
3. Para saques, informe um valor dentro do saldo e do limite permitido.
4. Para depósitos, informe o valor a ser adicionado ao saldo.
5. Para investimentos, escolha uma das opções e veja o saldo atualizado após o rendimento mensal.
6. Ao final de cada operação, escolha se deseja continuar ou encerrar o programa.

## Exemplo de Uso
```
-- BANCO DA UDF --

Cliente: Gabriel Rosa
Saldo: R$ 5000
Limite de Saque: R$ 2000

------------------------------------
Você deseja fazer saque, deposito ou investimento? (s/d/i) s
Escreva o valor do saque (LIMITE R$2000 / SALDO R$5000): 1000

SUCESSO AO SACAR.
SEU NOVO SALDO É DE R$ 4000
LIMITE PARA SAQUE: R$ 1000

Deseja fazer outra operação? (s/n) n

PROGRAMA FINALIZADO COM SUCESSO!
```

## Requisitos
- Python 3.x

## Autor
Gabriel Rosa Vilarouca Farias
Desenvolvido para o Centro Universitário do Distrito Federal (UDF), turma de Ciências da Computação, matéria Programação de Computadores com a docente Karla Roberto Sartin.
