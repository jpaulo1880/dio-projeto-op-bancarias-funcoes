# Nesse exemplo, tomei a liberdade de mesclar a função de registrar usuário
# e a função abrir conta corrente pois, apesar de serem funções separadas,
# elas são usadas em conjunto. Exemplo: Normalmente uma pessoa não se
# registra num banco sem a intenção de abrir uma conta.

# Dicionário contendo as contas abertas
contas = {}

# Função abrir conta corrente


def op_abre_conta():
    num_conta = 0
    nome = input("Digite seu nome: ")
    data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite seu CPF: ")
    endereco = input(
        "Digite seu endereço (Logradouro, Nº, Bairro, Cidade/Estado): ")
    num_conta += 1

    # Verifica se o CPF já está em uso
    if cpf in contas:
        print("CPF já cadastrado.")
        return

    # Dados pré-definidos da conta do usuário
    contas[cpf] = {
        "Agência": "0001",
        "Número CC": num_conta,
        "Saldo": 5000,
        "Saques na sessão": 0,
        "Saque máximo por sessão": 500,
        "Lista de depósitos": [],
        "Lista de saques": [],
        "Usuário": {
            "Nome": nome,
            "Data nasc": data_nasc,
            "Endereço": endereco,
            "Nº CPF": cpf
        }
    }

    print(f"Usuário {nome} cadastrado com sucesso.")

# Função depósito


def op_deposito(cpf):
    if cpf not in contas:
        print("Conta não encontrada. Retornando ao menu.")
        return

    conta = contas[cpf]

    while True:
        try:
            deposito = float(input("Insira o valor de depósito: R$ "))

            if deposito > 0:
                conta["Saldo"] += deposito
                conta["Lista de depósitos"].append(deposito)
                print(f"Depósito realizado. Seu Saldo é R$ {
                      conta['Saldo']:.2f}")
            else:
                print("O valor do depósito deve ser positivo. Tente novamente.")
                continue

            fim_op_deposito = int(
                input("Tecle 0 para retornar ou 1 para continuar: "))
            if fim_op_deposito == 0:
                break
            elif fim_op_deposito != 1:
                print("Opção inválida. Tente novamente.")
                break

        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

# Função saque


def op_saque(cpf):
    if cpf not in contas:
        print("Conta não encontrada. Retornando ao menu.")
        return

    conta = contas[cpf]

    while True:
        try:
            saque = float(input("Insira o valor do saque: R$ "))

            if saque > conta["Saldo"]:
                print("Saldo insuficiente. Tente novamente.")
                continue
            elif saque > conta["Saque máximo por sessão"]:
                print("Saque excede o limite. Tente novamente.")
                continue
            elif conta["Saques na sessão"] == 3:
                print("Limite de saques na sessão atingido.")
                return
            elif saque <= 0:
                print("Não é possível sacar valores negativos. Tente novamente.")
                continue

            conta["Saldo"] -= saque
            conta["Lista de saques"].append(saque)
            conta["Saques na sessão"] += 1
            print(f"Saque realizado. O Saldo restante é R$ {
                  conta['Saldo']:.2f}")

            fim_op_saque = int(
                input("Tecle 0 para retornar ou 2 para continuar: "))
            if fim_op_saque == 0:
                break

        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

# Função extrato


def op_extrato(cpf):
    if cpf not in contas:
        print("Conta não encontrada. Retornando ao menu.")
        return

    conta = contas[cpf]

    if conta["Lista de depósitos"] or conta["Lista de saques"]:
        print("Lista de depósitos realizados:")
        for deposito in conta["Lista de depósitos"]:
            print(f" - R$ {deposito:.2f}")

        print("Lista de saques realizados:")
        for saque in conta["Lista de saques"]:
            print(f" - R$ {saque:.2f}")

        print(f"Seu Saldo atual é R$ {conta['Saldo']:.2f}.")
    else:
        print("Sem movimentações no período.")

# Função principal


def main():
    while True:
        try:
            print(
                """
=================
1 - Abrir conta
2 - Depósito
3 - Saque
4 - Extrato
0 - Sair
=================
""")
            menu_op_selecionada = int(input("Selecione a opção desejada: "))

            if menu_op_selecionada == 1:
                op_abre_conta()

            elif menu_op_selecionada == 2:
                cpf = input("Digite o CPF associado a conta corrente: ")
                op_deposito(cpf)

            elif menu_op_selecionada == 3:
                cpf = input("Digite o CPF associado a conta corrente: ")
                op_saque(cpf)

            elif menu_op_selecionada == 4:
                cpf = input("Digite o CPF associado a conta corrente: ")
                op_extrato(cpf)

            elif menu_op_selecionada == 0:
                print("Obrigado por usar nossos serviços.")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Escolha uma opção válida.")


# Chama a função principal
main()
