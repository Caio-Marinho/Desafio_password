tentativa = 1
password = 'teste'
senha = input(f"{4-tentativa} de 3 Tentativas - Informe a senha: ")
if senha != password:
    while tentativa <= 3 and senha != password:
        tentativa += 1
        if tentativa<4:
            print("Senha Incorreta\ntente Novamente!!!")
            senha = input(f"{4-tentativa} de 3 Tentativas - Informe a senha: ")
        if senha == password:
            print("Senha Correta.\nAcesso Autorizado")
        elif tentativa == 4:
            print(f"Senha Incorreta.\n{4-tentativa} de 3 Tentativas\n"
                  f"Número Máxima de tentativas atingidas.\nEssa conta será bloqueada!!!")
else:
    print("Senha correta.\nAcesso Autorizado")