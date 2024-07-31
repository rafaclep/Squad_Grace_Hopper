'''6. Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
'''
def verificar_acesso(login, senha):
    if login == "admin" and senha == "admin123":
        return True
    else:
        return False

login_usuario = input("Digite o login: ")
senha_usuario = input("Digite a senha: ")

if verificar_acesso(login_usuario, senha_usuario):
    print("Acesso permitido.")
else:
    print("Erro: Login ou senha incorretos.")
