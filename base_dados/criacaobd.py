from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(250) NOT NULL,
    Nif VARCHAR(9) NOT NULL UNIQUE,
    Telemovel VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Morada VARCHAR(100) NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Servicos(
    id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeServico VARCHAR(250) NOT NULL,
    Descricao VARCHAR(250) NOT NULL,
    PrecoBase DECIMAL(10,2) NOT NULL,
    Estado TEXT NOT NULL DEFAULT 'Ativo' CHECK (Estado IN ('Ativo','Inativo')),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Orcamento(
    id_orcamento INTEGER PRIMARY KEY AUTOINCREMENT,
    DataOrcamento DATE NOT NULL,
    Estado TEXT NOT NULL DEFAULT 'Pendente' CHECK (Estado IN ('Pendente','Aprovado','Recusado','Cancelado')),
    ValorTotal DECIMAL(10,2) NOT NULL,
    Materiais TEXT NOT NULL DEFAULT 'Empresa' CHECK (Materiais IN ('Cliente','Empresa')),
    id_cliente INT NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Orcamento_Servico(
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10,2) NOT NULL,
    id_orcamento INT NOT NULL,
    id_servico INT NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_orcamento) REFERENCES Orcamento(id_orcamento),
    FOREIGN KEY (id_servico) REFERENCES Servicos(id_servico)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Contratos(
    id_contrato INTEGER PRIMARY KEY AUTOINCREMENT,
    NumeroContrato VARCHAR(50) NOT NULL UNIQUE,
    DataInicio DATE NOT NULL,
    DataFim DATE NULL,
    Estado TEXT NOT NULL DEFAULT 'Ativo' CHECK (Estado IN ('Ativo','Terminado','Cancelado')),
    LinkContrato VARCHAR(500) NULL,
    id_cliente INT NOT NULL,
    id_orcamento INT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_orcamento) REFERENCES Orcamento(id_orcamento)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Pagamentos(
    id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    DataPagamento DATE NOT NULL,
    ValorPago DECIMAL(10,2) NOT NULL,
    MetodoPagamento TEXT NOT NULL CHECK (MetodoPagamento IN ('Dinheiro','Multibanco','Transferencia','MBWay')),
    Estado TEXT NOT NULL DEFAULT 'Pendente' CHECK (Estado IN ('Pendente','Pago','Cancelado')),
    id_orcamento INT NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_orcamento) REFERENCES Orcamento(id_orcamento)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Despesas(
    id_despesa INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao VARCHAR(250) NOT NULL,
    Categoria TEXT NOT NULL CHECK (Categoria IN ('Material','Transporte','Equipamento','Servico','Outros')),
    Valor DECIMAL(10,2) NOT NULL,
    DataDespesa DATE NOT NULL,
    MetodoPagamento TEXT NOT NULL CHECK (MetodoPagamento IN ('Dinheiro','Multibanco','Transferencia','MBWay')),
    Observacoes VARCHAR(500) NULL,
    id_orcamento INT NOT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_orcamento) REFERENCES Orcamento(id_orcamento)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telemovel VARCHAR(15) NULL,
    Assunto VARCHAR(150) NOT NULL,
    Mensagem VARCHAR(1000) NOT NULL,
    Estado TEXT NOT NULL DEFAULT 'Novo' CHECK (Estado IN ('Novo','Em Analise','Respondido','Arquivado')),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Marcacoes(
    id_marcacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telemovel VARCHAR(15) NOT NULL,
    DataPretendida DATE NOT NULL,
    HoraPretendida TIME NULL,
    Observacoes VARCHAR(500) NULL,
    morada varchar (255) null,
    Estado TEXT NOT NULL DEFAULT 'Pendente' CHECK (Estado IN ('Pendente','Confirmada','Concluida','Remarcada', 'Cancelada')),
    id_servico INT NULL,
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_servico) REFERENCES Servicos(id_servico)
);""")

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Administradores(
    id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Senha VARCHAR(255) NULL,
    Telemovel VARCHAR(15) NOT NULL UNIQUE   ,
    Estado TEXT NOT NULL DEFAULT 'Ativo' CHECK (Estado IN ('Ativo','Inativo')),
    criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);""")

conexao.commit()
conexao.close()