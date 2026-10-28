from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

# cursor.execute("ALTER TABLE Marcacoes ADD COLUMN morada varchar (255) null")
cursor.execute("UPDATE Marcacoes SET Telemovel = '351936392161' WHERE id_marcacao = 3")
# [(1, 'Admin', 'admin@nexogest.pt', None, '912345679', 'Ativo', '2026-10-19 11:46:34', '2026-10-19 11:46:34')]
conexao.commit()
conexao.close()