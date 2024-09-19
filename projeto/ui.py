import view

class UI:
    @staticmethod
    def menu():
        print("Cadastro de Jogadores")
        print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("Cadastro de Times")
        print("  5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("Gerenciamento de Times e Jogadores")
        print("  9 - Adicionar Jogador ao Time")
        print("Cadastro de Campeonatos")
        print("  10 - Inserir, 11 - Listar, 12 - Atualizar, 13 - Excluir")
        print("Gerenciamento de Campeonatos e Times")
        print("  14 - Adicionar Time ao Campeonato")
        print("Outras opções")
        print("  15 - Fim")

        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 15:
            op = UI.menu()
            if op == 1: UI.jogador_inserir()
            if op == 2: UI.jogador_listar()
            if op == 3: UI.jogador_atualizar()
            if op == 4: UI.jogador_excluir()
            if op == 5: UI.time_inserir()
            if op == 6: UI.time_listar()
            if op == 7: UI.time_atualizar()
            if op == 8: UI.time_excluir()
            if op == 9: UI.adicionar_jogador_ao_time()
            if op == 10: UI.campeonato_inserir()
            if op == 11: UI.campeonato_listar()
            if op == 12: UI.campeonato_atualizar()
            if op == 13: UI.campeonato_excluir()
            if op == 14: UI.adicionar_time_ao_campeonato()

    # Jogadores
    @staticmethod
    def jogador_inserir():
        nome = input("Informe o nome do jogador: ")
        numeroCam = int(input("Informe o número da camisa: "))
        idade = int(input("Informe a idade do jogador: "))
        view.jogador_inserir(nome, numeroCam, idade)
        print("Jogador inserido com sucesso!")

    @staticmethod
    def jogador_listar():
        jogadores = view.jogador_listar()
        if jogadores:
            for j in jogadores:
                print(j)
        else:
            print("Nenhum jogador cadastrado.")

    @staticmethod
    def jogador_atualizar():
        UI.jogador_listar()
        id = int(input("Informe o ID do jogador a ser atualizado: "))
        nome = input("Informe o novo nome (ou pressione Enter para manter o atual): ")
        numeroCam = input("Informe o novo número da camisa (ou pressione Enter para manter o atual): ")
        idade = input("Informe a nova idade (ou pressione Enter para manter a atual): ")

        numeroCam = int(numeroCam) if numeroCam else None
        idade = int(idade) if idade else None

        atualizado = view.jogador_atualizar(id, nome or None, numeroCam, idade)
        if atualizado:
            print("Jogador atualizado com sucesso!")
        else:
            print("Jogador não encontrado.")

    @staticmethod
    def jogador_excluir():
        UI.jogador_listar()
        id = int(input("Informe o ID do jogador a ser excluído: "))
        view.jogador_excluir(id)
        print("Jogador excluído com sucesso!")

    # Times
    @staticmethod
    def time_inserir():
        nome = input("Informe o nome do time: ")
        view.time_inserir(nome)
        print("Time inserido com sucesso!")

    @staticmethod
    def time_listar():
        times = view.time_listar()
        if times:
            for t in times:
                print(t)
        else:
            print("Nenhum time cadastrado.")

    @staticmethod
    def time_atualizar():
        UI.time_listar()
        id = int(input("Informe o ID do time a ser atualizado: "))
        nome = input("Informe o novo nome (ou pressione Enter para manter o atual): ")
        
        jogadores = input("Informe os IDs dos jogadores separados por vírgula (ou pressione Enter para manter os atuais): ")
        jogadores_list = [int(j.strip()) for j in jogadores.split(",")] if jogadores else None
        
        atualizado = view.time_atualizar(id, nome or None, jogadores_list)
        if atualizado:
            print("Time atualizado com sucesso!")
        else:
            print("Time não encontrado.")

    @staticmethod
    def time_excluir():
        UI.time_listar()
        id = int(input("Informe o ID do time a ser excluído: "))
        view.time_excluir(id)
        print("Time excluído com sucesso!")

    @staticmethod
    def adicionar_jogador_ao_time():
        UI.time_listar()
        time_id = int(input("Informe o ID do time: "))
        UI.jogador_listar()
        jogador_id = int(input("Informe o ID do jogador a ser adicionado ao time: "))

        adicionado = view.adicionar_jogador_ao_time(time_id, jogador_id)
        if adicionado:
            print("Jogador adicionado ao time com sucesso!")
        else:
            print("Falha ao adicionar jogador ao time.")

    # Campeonatos
    @staticmethod
    def campeonato_inserir():
        nome = input("Informe o nome do campeonato: ")
        descricao = input("Informe a descrição do campeonato: ")
        patrocinadores = input("Informe os patrocinadores separados por vírgula (ou pressione Enter para nenhum): ")
        patrocinadores_list = [p.strip() for p in patrocinadores.split(",")] if patrocinadores else []
        
        view.campeonato_inserir(nome, descricao, patrocinadores_list)
        print("Campeonato inserido com sucesso!")

    @staticmethod
    def campeonato_listar():
        campeonatos = view.campeonato_listar()
        if campeonatos:
            for c in campeonatos:
                print(c)
        else:
            print("Nenhum campeonato cadastrado.")

    @staticmethod
    def campeonato_atualizar():
        UI.campeonato_listar()
        id = int(input("Informe o ID do campeonato a ser atualizado: "))
        nome = input("Informe o novo nome (ou pressione Enter para manter o atual): ")
        descricao = input("Informe a nova descrição (ou pressione Enter para manter a atual): ")
        patrocinadores = input("Informe os novos patrocinadores separados por vírgula (ou pressione Enter para manter os atuais): ")
        times = input("Informe os IDs dos times separados por vírgula (ou pressione Enter para manter os atuais): ")
        
        patrocinadores_list = [p.strip() for p in patrocinadores.split(",")] if patrocinadores else None
        times_list = [int(t.strip()) for t in times.split(",")] if times else None

        atualizado = view.campeonato_atualizar(id, nome or None, descricao or None, patrocinadores_list, times_list)
        if atualizado:
            print("Campeonato atualizado com sucesso!")
        else:
            print("Campeonato não encontrado.")

    @staticmethod
    def campeonato_excluir():
        UI.campeonato_listar()
        id = int(input("Informe o ID do campeonato a ser excluído: "))
        view.campeonato_excluir(id)
        print("Campeonato excluído com sucesso!")

    @staticmethod
    def adicionar_time_ao_campeonato():
        UI.campeonato_listar()
        campeonato_id = int(input("Informe o ID do campeonato: "))
        UI.time_listar()
        time_id = int(input("Informe o ID do time a ser adicionado ao campeonato: "))

        adicionado = view.adicionar_time_ao_campeonato(campeonato_id, time_id)
        if adicionado:
            print("Time adicionado ao campeonato com sucesso!")
        else:
            print("Falha ao adicionar time ao campeonato.")

UI.main()
