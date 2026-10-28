# menu do administrador 
# é chamado pelo inicio.py quando o número está na tabela Administradores

import pandas as pd

def menu_admin(conexao, cursor):
    select = 0

    while select != 5:
        print("1- Ver marcações")
        print("2- Ver contactos novos")
        print("3- Pagamentos")
        print("4- Orçamentos ")
        print("5- Sair")

        select = int(input("Selecione uma opção:"))

        if select == 1:
            # marcações à espera de resposta
            def marcP():
                cursor.execute("SELECT id_marcacao, Nome, Telemovel, DataPretendida, HoraPretendida, Observacoes, Morada FROM Marcacoes WHERE Estado = 'Pendente'")
                return cursor.fetchall()

            pendentes = marcP()
            tabela = pd.DataFrame(pendentes, columns=["ID", "Nome", "Telemóvel", "Data", "Hora", "Observações", "Morada"])

            print("Marcações pendentes:")
            print(tabela.to_string(index=False))   # sem a numeração do pandas

            # o admin escolhe a marcação pelo id e confirma ou cancela
            def status():
                escolha = input("Insira um id que pretanda alterar (Enter para voltar):")
                if escolha == "":
                    return   # volta ao menu
                id_marc = int(escolha)
                cursor.execute("SELECT * FROM Marcacoes Where id_marcacao = ? ", (id_marc,))
                ver = cursor.fetchone()

                print("A marcação selecionada foi:")
                print(ver)

                print("\n1- Confirmar")
                print("\n2- Cancelar")
                change = int(input("Deseja alterar para qual estado?"))

                if change == 1:
                    cursor.execute("UPDATE marcacoes SET Estado = 'Confirmada' WHERE id_marcacao = ?", (id_marc,))
                    conexao.commit()
                    print("O estado da marcação foi alterada para Confirmada!")
                    # mostra a mensagem que o cliente receberia
                    def confirmar():
                        cursor.execute("SELECT Nome, Telemovel,DataPretendida, HoraPretendida FROM Marcacoes WHERE id_marcacao = ? ", (id_marc,))
                        dados = cursor.fetchone()   # 0 nome, 1 telemóvel, 2 data, 3 hora
                        texto = (f"Olá {dados[0]}! A sua visita foi confirmada para {dados[2]} às {dados[3]}. Até breve! ")
                        print(f"Mensagem para {dados[1]}: {texto}")

                    confirmar()

                elif change == 2:
                    cursor.execute("UPDATE marcacoes SET Estado = 'Cancelada' WHERE id_marcacao = ?", (id_marc,))
                    conexao.commit()
                    print("O estado da marcação foi alterada para Cancelada!")
                    # mostra a mensagem que o cliente receberia
                    def cancelar():
                        cursor.execute("SELECT Nome, Telemovel,DataPretendida, HoraPretendida FROM Marcacoes WHERE id_marcacao = ? ", (id_marc,))
                        dados1 = cursor.fetchone()
                        texto1 = (f"Olá {dados1[0]}! A sua visita no dia {dados1[2]}  às {dados1[3]} foi cancelada: Brevemente entraremos em conctato para efetuar remarcação . Até breve! ")
                        print(f"Mensagem para {dados1[1]}: {texto1}")

                    cancelar()
            status()

        elif select == 2:
            # ainda por fazer
            def novo():
                cursor.execute("SELECT ")
            print("Em construção")
            # def marc():

        elif select == 3:
            # pagamentos por receber, com o nome do cliente
            # (o pagamento só tem o id do orçamento, por isso junto as 3 tabelas)
            def pagP():
                cursor.execute("""SELECT Pagamentos.id_pagamento, Clientes.Nome, Pagamentos.DataPagamento, Pagamentos.ValorPago, Pagamentos.MetodoPagamento FROM Pagamentos JOIN Orcamento ON Pagamentos.id_orcamento = Orcamento.id_orcamento JOIN Clientes ON Orcamento.id_cliente = Clientes.id_cliente WHERE Pagamentos.Estado = 'Pendente'""")
                return cursor.fetchall()

            pagamentos = pagP()
            tabela_pag = pd.DataFrame(pagamentos, columns=["ID", "Cliente", "Data", "Valor (€)", "Método"])

            print("Pagamentos pendentes:")
            print(tabela_pag.to_string(index=False))

        elif select == 4:
            # todos os orçamentos com o nome do cliente
            def orcP():
                cursor.execute("""SELECT Orcamento.id_orcamento, Clientes.Nome, Orcamento.DataOrcamento, Orcamento.ValorTotal, Orcamento.Materiais, Orcamento.Estado FROM Orcamento JOIN Clientes ON Orcamento.id_cliente = Clientes.id_cliente""")
                return cursor.fetchall()

            orcamentos = orcP()
            tabela_orc = pd.DataFrame(orcamentos, columns=["ID", "Cliente", "Data", "Valor (€)", "Materiais", "Estado"])

            print("Orçamentos:")
            print(tabela_orc.to_string(index=False))

            # mostra a mensagem do orçamento escolhido, como o cliente a receberia
            escolha = input("ID do orçamento para enviar ao cliente (Enter para voltar): ")
            if escolha != "":
                id_orc = int(escolha)

                # dados do orçamento e do cliente: 0 nome, 1 telemóvel, 2 data, 3 valor, 4 materiais
                cursor.execute("""SELECT Clientes.Nome, Clientes.Telemovel, Orcamento.DataOrcamento, Orcamento.ValorTotal, Orcamento.Materiais FROM Orcamento JOIN Clientes ON Orcamento.id_cliente = Clientes.id_cliente WHERE Orcamento.id_orcamento = ?""", (id_orc,))
                orc = cursor.fetchone()

                if orc is None:
                    print("Não existe nenhum orçamento com esse ID.")
                else:
                    # serviços do orçamento: 0 serviço, 1 quantidade, 2 preço
                    cursor.execute("""SELECT Servicos.NomeServico, Orcamento_Servico.Quantidade, Orcamento_Servico.PrecoUnitario FROM Orcamento_Servico JOIN Servicos ON Orcamento_Servico.id_servico = Servicos.id_servico WHERE Orcamento_Servico.id_orcamento = ?""", (id_orc,))
                    itens = cursor.fetchall()

                    texto_orc = f"Olá {orc[0]}! Segue o seu orçamento n.º {id_orc} ({orc[2]}):\n"
                    subtotal = 0
                    for item in itens:
                        total = item[1] * item[2]
                        subtotal = subtotal + total
                        texto_orc = texto_orc + f"\n- {item[0]}: {item[1]} x {item[2]:.2f} € = {total:.2f} €"

                    if len(itens) == 0:   # sem serviços, usa o valor guardado no orçamento
                        subtotal = orc[3]

                    iva = subtotal * 0.23
                    texto_orc = texto_orc + f"\n\nSubtotal: {subtotal:.2f} €\nIVA 23%: {iva:.2f} €\nTOTAL: {subtotal + iva:.2f} €"

                    if orc[4] == "Cliente":
                        texto_orc = texto_orc + "\n\nMateriais fornecidos pelo cliente."
                    else:
                        texto_orc = texto_orc + "\n\nMateriais fornecidos pela empresa."
                    texto_orc = texto_orc + "\nVálido por 30 dias.\nTiago Tessarolo Lda"

                    print(f"Mensagem para {orc[1]}:")
                    print(texto_orc)
