from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

# cursor.execute("""
# INSERT INTO Marcacoes (Nome, Email, Telemovel, DataPretendida, HoraPretendida, Observacoes, Estado, Morada)
# VALUES
# ('Ricardo Martins', 'ricardo.martins@email.pt', '912345671', '2026-10-22', '10:00', 'Pintura de sala e corredor', 'Pendente', 'Rua das Flores 12, Barreiro'),
# ('Carla Gomes', 'carla.gomes@email.pt', '912345672', '2026-10-23', '14:30', 'Remodelação da casa de banho', 'Pendente', 'Av. da Liberdade 45, Lisboa'),
# ('Tiago Ferreira', 'tiago.ferreira@email.pt', '912345673', '2026-10-27', NULL, 'Infiltração no teto', 'Pendente', 'Rua do Sol 7, Seixal'),
# ('Ana Rodrigues', 'ana.rodrigues@email.pt', '912345674', '2026-10-20', '09:00', 'Colocação de piso flutuante', 'Confirmada', 'Praça da República 3, Almada'),
# ('Pedro Sousa', 'pedro.sousa@email.pt', '912345675', '2026-10-10', '11:00', 'Estuque na cozinha', 'Concluida', 'Rua Nova 88, Moita'),
# ('Inês Carvalho', 'ines.carvalho@email.pt', '912345676', '2026-10-25', '16:00', 'Pladur para dividir quarto', 'Cancelada', 'Rua da Escola 21, Barreiro');
# """)

# cursor.execute("""
# INSERT INTO Administradores (Nome, Email, Telemovel)
# VALUES ('Admin', 'admin@nexogest.pt', '912345679');
# """)

# serviços (ficam com id 1 a 6)
# cursor.execute("""
# INSERT INTO Servicos (NomeServico, Descricao, PrecoBase)
# VALUES
# ('Pintura interior', 'Pintura de paredes e tetos interiores', 15.00),
# ('Acabamento de estuque e barramento geral', 'Estuque e barramento de paredes', 20.00),
# ('Betumilha', 'Aplicação de betumilha', 12.00),
# ('Instalação de azulejo no chão', 'Assentamento de azulejo/mosaico', 25.00),
# ('Revestimento de WC', 'Revestimento cerâmico de casa de banho', 40.00),
# ('Pintura exterior', 'Pintura de fachadas', 18.00);
# """) 

# itens: quantidade, preço, orçamento, serviço
# as contas batem com o ValorTotal: 1250, 480 e 3200
# cursor.execute("""
# INSERT INTO Orcamento_Servico (Quantidade, PrecoUnitario, id_orcamento, id_servico)
# VALUES
# (50, 15.00, 1, 1),
# (25, 20.00, 1, 2),
# (40, 12.00, 2, 3),
# (80, 25.00, 3, 4),
# (30, 40.00, 3, 5);
# """)
# (1, 'Admin', 'admin@nexogest.pt', None, '912345679', 'Ativo', '2026-10-19 11:46:34', '2026-10-19 11:46:34')
conexao.commit()
conexao.close()

print("Dados de teste inseridos!")