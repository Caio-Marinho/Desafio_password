tentativa = 1
password = 'teste'
senha = input(f"{4 - tentativa} de 3 Tentativas - Informe a senha: ")
if senha != password:
    while tentativa < 3 and senha != password:
        print("Senha Incorreta\ntente Novamente!!!")
        tentativa += 1
        senha = input(f"{4-tentativa} de 3 Tentativas - Informe a senha: ")
        if senha == password:
            print("Senha Correta.\nAcesso Autorizado")
        elif tentativa == 3:
            print(f"Senha Incorreta.\n{3-tentativa} de 3 Tentativas\n"
                  f"Número Máxima de tentativas atingidas.\nEssa conta será bloqueada!!!")
else:
    print("Senha correta.\nAcesso Autorizado")