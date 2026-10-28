# menu do cliente
# é chamado pelo inicio.py quando o número não é de um admin

def menu_cliente(conexao, cursor, numero):

    # marcação do cliente que está a escrever
    def cliente():
        cursor.execute("SELECT DataPretendida,HoraPretendida,Estado FROM Marcacoes WHERE Telemovel = ?", (numero,))
        return cursor.fetchone()

    opcao =  0
    while opcao != 4:
        print("1- Ver serviços")
        print("2- Ver marcações e alterar estado")
        print("3- Marcar visita para orçamento")
        print("4- Cancelar atendimento")

        opcao = int(input("Selecione uma opção:"))

        if opcao == 1:
            print("Serviços:\n")
            print("Pintura interior e exterior,\n Colocação de pavimentos,\n Estuque,\n Pladur,\n Tetos falso,\n Revestimentos e azulejos,\n Canalização,\n Eletricidade,\n Remodelações;")

        elif opcao == 2:
            marcacao = cliente()   # busca aqui para mostrar sempre o estado atual
            print(marcacao)

            alter = input("Pretende alterar marcação?")
            print(alter)

            if alter.upper() == "SIM":   # aceita sim, Sim ou SIM
                print("\n 1- Confirmar")
                print("\n 2- Remarcar")
                print("\n 3- Cancelar")
                estado = int(input("Deseja alterar para qual estado?"))
                print (estado)
                if estado == 1:
                    cursor.execute("UPDATE Marcacoes Set Estado = 'Confirmada' WHERE Telemovel = ?", (numero,))
                    conexao.commit()
                    print("Sua marcação foi confirmada!")

                elif estado == 2:
                    data = input("Para qual dia pretende remarcar? (AAAA-MM-DD) ")
                    # volta a Pendente porque é o admin que aprova a nova data
                    cursor.execute("UPDATE Marcacoes Set Estado = 'Pendente', DataPretendida = ? WHERE Telemovel = ?", (data, numero))
                    conexao.commit()
                    print("Quando sua remarcação foi aceita ira receber uma mensagem de confirmação")
                elif estado == 3:   
                    cursor.execute("UPDATE Marcacoes Set Estado = 'Cancelada' WHERE Telemovel = ?", (numero,))
                    conexao.commit()
                    print("Sua marcação foi cancelada!")

        elif opcao == 3:
            nome = input("Insira seu nome:")

            email = input("Insira seu email:")
            # só avança quando o email tiver @ e ponto
            while "@" not in email or "." not in email:
                print("Email inválido")
                email = input("Insira seu email:")

            datapretendida = input("Insira a data pretendida (AAAA-MM-DD)")
            hora = input("A que horas? (HH:MM, ou Enter para deixar em aberto) ")
            if hora == "":
                hora = None   # fica NULL na base

            if hora is None:
                texto_hora = "hora a combinar"
            else:
                texto_hora = f"às {hora}"

            morada = input("Insira a morada:")
            obs = input("Insira a descrição do trabalho e observações:")

            # o estado fica Pendente pelo DEFAULT da tabela
            def marcacaoD():
                cursor.execute("INSERT INTO Marcacoes (Nome, Email, Telemovel, DataPretendida, HoraPretendida, Observacoes,morada  ) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, email, numero, datapretendida, hora, obs, morada))
                conexao.commit()
                return cursor.fetchone()

            print(marcacaoD())
            print(f"Resumo: {nome}, dia {datapretendida}, {texto_hora}, {morada}, {obs}")
            print("Sua marcação foi solicitada, assim que for confirmada recebera uma mensagem com esta informação")

        elif opcao == 4:
                print("Atendimento cancelado, Obrigado!")
