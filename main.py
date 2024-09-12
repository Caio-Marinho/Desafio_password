tentativa = 1
password = 'teste'
senha = input(f"{tentativa}º Tentativa - Informe a senha: ")
if senha != password:
    while tentativa < 3 and senha != password:
        print("Senha Incorreta\ntente Novamente!!!")
        tentativa += 1
        senha = input(f"{tentativa}º Tentativa - Informe a senha: ")
        if senha == password:
            print("Senha Correta.\nAcesso Autorizado")
        elif tentativa == 3:
            print("Senha Incorreta.\nNúmero Máxima de tentativas atingidas.\nEssa conta será bloqueada!!!")
else:
    print("Senha correta.\nAcesso Autorizado")