912345679
# NexoGest - bot de atendimento
# vê pelo número se quem escreve é admin ou cliente e mostra o menu certo

from base_dados.conexao import conectar
from cliente.menu_cliente import menu_cliente
from admin.menu_admin import menu_admin

conexao = conectar()
cursor = conexao.cursor()


print("Olá, como posso lhe ajudar?\n")

# no WhatsApp este número vem na mensagem, aqui escrevo à mão para testar
numero = input("Número de telemóvel: ")

# procura o número na tabela dos admins (None se não for admin)
def admin ():
    cursor.execute("SELECT Nome FROM Administradores WHERE Telemovel = ?", (numero,))
    return cursor.fetchone()

resultado = admin()

if resultado  is None:
    menu_cliente(conexao, cursor, numero)
else:
    menu_admin(conexao, cursor)

conexao.close()
