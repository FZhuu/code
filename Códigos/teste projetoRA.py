print("Bem vindo!")
conta = input("\nDigite 1 para entrar na área do usuário ou digite 2 para entrar na área do administrador: ")
saldo = 0
valor_passagem = 6
if conta == "1":
    print("\nBem vindo a página de usuário.")
    senha0 = input("\nPara continuar,por favor, digite a senha: ")
    if senha0 != "123456":
        print("\nsenha errada, o sistema irá ser encerrado.")
        print("Tente novamente.")
        print("===========================================")
        exit
    if senha0 == "123456":
        print("\nQual recurso deseja utilizar? ")
        opção_menu1 = input("Digite 1 para usar cartão ou 2 para recarregar cartão. ")
        if opção_menu1 == "1":
            if saldo < 6:
                print("\nSaldo insuficiente.")
                print("Sistema encerrado.")
                print("===========================================")
                exit
            if saldo >= 6 :
                saldo -= valor_passagem
            print("saldo restante = ", saldo)
            exit
        if opção_menu1 == "2":
            add_saldo = (input("\nDigite quanto de saldo deseja adicionar ao cartão: "))
            if add_saldo.isdigit():
                saldo += float(add_saldo)
                print("\nSeu saldo é de: ",saldo)
                exit
            else:
                print("\nCaracter não identificado.")
                print("Sistema encerrado.")
                print("===========================================")
                exit
if conta == "2":
    print("\nBem vindo a página de administrador")
    senha1 = input("\nPara continuar,por favor, digite a senha: ")
    if senha1 != "123456":
        print("\nsenha errada, o sistema irá ser encerrado.")
        print("Tente novamente.")
        print("===========================================")
        exit
    if senha1 == "123456":
        opção_menu1 = input("\n Qual recurso deseja utilizar? ")


     