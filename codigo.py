import sys

conta = []
saldo = []
acumSaldo = 0

for x in range(3):
    codigo = int(input("Informe um código de conta: "))
    conta.append(codigo)

    cash = float(input("Informe o saldo da conta: "))
    saldo.append(cash)

    acumSaldo = cash + acumSaldo

menu = 0

while menu <= 0:

    print(f"<__-MENU-__>")

    print(f"1 - Realizar Depósito")
    print(f"2 - Realizar Saque")
    print(f"3 - Consultar ativo bancário")
    print(f"4 - Finalizar Programa.")

    print(f"<__-MENU-__>")

    menuCode = int(input("Informe o código de menu: "))

    if menuCode == 1:
        varCode = int(input("Informe seu código de conta: "))

        if varCode in conta:
            newCash = float(input("Valor do deposito: "))
            if varCode == conta[0]:
                deposito = saldo[0]
                somCash = deposito + newCash
                saldo[0] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[1]:
                 deposito = saldo[1]
                 somCash = deposito + newCash
                 saldo[1] = somCash
                 print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[2]:
                 deposito = saldo[2]
                 somCash = deposito + newCash
                 saldo[2] = somCash
                 print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[3]:
                deposito = saldo[3]
                somCash = deposito + newCash
                saldo[3] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[4]:
                deposito = saldo[4]
                somCash = deposito + newCash
                saldo[4] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[5]:
                deposito = saldo[5]
                somCash = deposito + newCash
                saldo[5] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[6]:
                deposito = saldo[6]
                somCash = deposito + newCash
                saldo[6] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[7]:
                deposito = saldo[7]
                somCash = deposito + newCash
                saldo[7] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[8]:
                deposito = saldo[8]
                somCash = deposito + newCash
                saldo[8] = somCash
                print(f"Seu novo saldo é de: {somCash}")
            if varCode == conta[9]:
                deposito = saldo[9]
                somCash = deposito + newCash
                saldo[9] = somCash
                print(f"Seu novo saldo é de: {somCash}")
        else:
            print("Conta não encontrada!")

    if menuCode == 2:
        varCode = int(input("Informe seu código de conta: "))

        if varCode in conta:
            saqCash = float(input("Informe o valor do saque: "))
            if saqCash < cash:
                if varCode == conta[0]:
                    saque = saldo[0]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[1]:
                    saque = saldo[1]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[2]:
                    saque = saldo[2]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[3]:
                    saque = saldo[3]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[4]:
                    saque = saldo[4]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[5]:
                    saque = saldo[5]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[6]:
                    saque = saldo[6]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[7]:
                    saque = saldo[7]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[8]:
                    saque = saldo[8]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
                if varCode == conta[9]:
                    saque = saldo[9]
                    subCash = saque - saqCash
                    print(f"Você depositou: {saqCash} e agora seu novo saldo é de: {subCash}")
            else:
                print("Saldo Insuficiente!")

    if menuCode == 3:
        print(f"O total de ativos do banco é: {acumSaldo}")
    if menuCode == 4:
        menu = 1
