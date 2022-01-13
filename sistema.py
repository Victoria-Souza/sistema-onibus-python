from classes import *

sistema_onibus = []
sistema_ponto = []
sistema_motorista = []
sistema_fiscal = []


def main():
    sistema_onibus = []
    sistema_ponto = []
    sistema_motorista = []
    sistema_fiscal = []

    print('Bem vindo ao nosso sistema!\nMenu:')
    while True:

        print(' 1 - Criar \n 2 - Mostrar \n 3 - Assignar \n 4 - Adicionar \n 5 - Alterar \n 6 - Deletar \n 7 - Sair do programa')

        opcao1 = input(
            'Digite a opção referente a função que deve ser executada: ')

        if opcao1 not in ['3', '4', '7']:
            print('Escolha para qual você quer fazer a mudança: ')
            print(' 1 - ônibus \n 2 - Ponto de parada \n 3 - motorista \n 4 - fiscal')
            opcao2 = input(
                'Digite a opção referente a função que deve ser executada: ')

        elif opcao1 in ['3', '4']:
            opcao2 = '1'
        elif opcao1 in ['7']:
            break
        else:  #Caso a entrada não esteja no menu
            print('Entrada inválida, selecione outro!')

        if opcao1 == '1': # Criar
            if opcao2 == '1':  # onibus
                novo_onibus = onibus()
                sistema_onibus += [[novo_onibus.linha, [[], '', ''],novo_onibus]]
                print('ônibus criado')
            elif opcao2 == '2':  # ponto de parada
                novo_ponto = ponto()
                sistema_ponto += [[novo_ponto.nome, novo_ponto]]
                print('Ponto de parada criado')
            elif opcao2 == '3':  # motorista
                novo_motorista = motorista()
                sistema_motorista += [[novo_motorista.nome,novo_motorista]]
                print('Motorista criado')
            elif opcao2 == '4':  # fiscal
                novo_fiscal = fiscal()
                sistema_fiscal += [[novo_fiscal.nome,novo_fiscal]]
                print('Fiscal criado')
            else:
                print('Entrada inválida, selecione outro!')

        elif opcao1 == '2': # Mostrar
            if opcao2 == '1':  # onibus
                print('Os ônibus existentes são os: ')
                for i in sistema_onibus:
                    print(i[0],'\n')

            elif opcao2 == '2':  # ponto de parada
                print('Os Pontos existentes são os: ')
                for i in sistema_ponto:
                    print(i[0],'\n')

            elif opcao2 == '3':  # motorista
                print('Os motoristas existentes são os: ')
                for i in sistema_motorista:
                    print(i[0],'\n')

            elif opcao2 == '4':  # fiscal
                print('Os fiscais existentes são os: ')
                for i in sistema_fiscal:
                    print(i[0],'\n')

            else:
                print('Entrada inválida, selecione outro!')

        elif opcao1 == '3': # Assignar
            print('Escolha para qual você quer fazer a mudança: ')
            print(' 1 - motorista ao ônibus \n 2 - Fiscal ao ônibus \n')
            opcao3 = input('Digite a opção referente a função que deve ser executada: ')
            if opcao3 == '1':
                while True:
                    nome_motorista = input('Digite o nome do motorista: ')
                    if nome_motorista == 'sair':
                        break
                    for i in range(len(sistema_motorista)):
                        if nome_motorista == sistema_motorista[i][0]:
                            break
                    print('Motorista não encontrado. Digite outro ou sair!')
                linha_onibus = input('Digite o numero da linha para direcionar o motorista: ')
                for i in range(len(sistema_onibus)):
                    if linha_onibus == sistema_onibus[i][0]:
                        sistema_onibus[i][1][1] = nome_motorista

            elif opcao3 == '2':
                while True:
                    nome_fiscal = input('Digite o nome do fiscal: ')
                    if nome_fiscal == 'sair':
                        break
                    for i in range(len(sistema_fiscal)):
                        if nome_fiscal == sistema_fiscal[i][0]:
                            break
                    print('Fiscal não encontrado. Digite outro ou sair!')
                nome_fiscal = input('Digite o nome do fiscal: ')
                linha_onibus = input('Digite o numero da linha para direcionar o fiscal: ')
                for i in range(len(sistema_onibus)):
                    if linha_onibus == sistema_onibus[i][0]:
                        sistema_onibus[i][1][2] = nome_fiscal
            

        elif opcao1 == '4': # Adicionar
            while True:
                nome_parada = input('Digite o nome da parada: ')
                if nome_parada == 'sair':
                    break
                for i in range(len(sistema_ponto)):
                    if nome_parada == sistema_ponto[i][0]:
                        break
                print('Ponto de parada não encontrado. Digite outro ou sair!')
            nome_parada = input('Digite o nome da parada: ')
            linha_onibus = input('Digite o numero da linha para direcionar a parada: ')
            for i in range(len(sistema_onibus)):
                if linha_onibus == sistema_onibus[i][0]:
                    sistema_onibus[i][1][0] += [nome_parada]

        elif opcao1 == '5': # Alterar
            if opcao2 == '1':
                opcao3 = input('Escolha para qual você quer fazer a mudança: 1 - Dados do ônibus \n 2 - Rota do ônibus')
                if opcao3 == '1':
                    linha_onibus = input('Qual linha que será a mudança? ')
                    for i in range(len(sistema_onibus)):
                        if linha_onibus == sistema_onibus[i][0]: 
                            sistema_onibus[i][2].mudar_linha()
                            sistema_onibus[i][0] = sistema_onibus[i][2].linha
                
                elif opcao3 == '2':
                    linha_onibus = input('Qual linha que será a mudança? ')
                    for i in range(len(sistema_onibus)):
                        if linha_onibus == sistema_onibus[i][0]:
                            lista_parada = sistema_onibus[i][1][0]
                            contador = 0
                            for i in lista_parada:
                                print(f'{contador} - {i}\n')
                            ponto_escolhido = input('Qual número do ponto você quer? ')
                            del lista_parada[ponto_escolhido]
                            sistema_onibus[i][1][0] = lista_parada

            elif opcao2 == '2':
                nome_parada = input('Qual o nome da parada que você quer modificar: ')
                for i in range(len(sistema_ponto)):
                    if nome_parada == sistema_ponto[i][0]:
                        sistema_ponto[i][1].mudar_ponto()
                        for k in sistema_onibus:
                            for j in range(len(sistema_onibus[k][1][0])):
                                if nome_parada == sistema_onibus[k][1][0][j]:
                                    sistema_onibus[k][1][0][j] = sistema_ponto[i][1].nome

            elif opcao2 == '3':
                nome_motorista = input('Qual o nome do motorista que você quer modificar: ')
                for i in range(len(sistema_motorista)):
                    if nome_motorista == sistema_motorista[i][0]:
                        sistema_motorista[i][1].mudar_motorista()
                        for k in sistema_onibus:
                            if nome_motorista == sistema_onibus[k][1][1]:
                                sistema_onibus[k][1][1] = sistema_motorista[i][1].nome
            
            elif opcao2 == '4':
                nome_fiscal = input('Qual o nome do fiscal que você quer modificar: ')
                for i in range(len(sistema_fiscal)):
                    if nome_fiscal == sistema_fiscal[i][0]:
                        sistema_fiscal[i][1].mudar_fiscal()
                        for k in sistema_onibus:
                            if nome_fiscal == sistema_onibus[k][1][2]:
                                sistema_onibus[k][1][2] = sistema_fiscal[i][1].nome

        elif opcao1 == '6': # Deletar
            if opcao2 == '1':
                linha_onibus = input('Qual linha que será deletada? ') 
                for i in range(len(sistema_onibus)):
                    if linha_onibus == sistema_onibus[i][0]:
                        del sistema_onibus[i]

            elif opcao2 == '2':
                nome_parada = input('Qual parada que será deletada? ') 
                for i in range(len(sistema_ponto)):
                    if nome_parada == sistema_ponto[i][0]:
                        del sistema_ponto[i]

            elif opcao2 == '3':
                nome_motorista = input('Qual motorista que será deletado? ') 
                for i in range(len(sistema_motorista)):
                    if nome_motorista == sistema_motorista[i][0]:
                        del sistema_motorista[i]

            elif opcao2 == '4':
                nome_fiscal = input('Qual fiscal que será deletado? ') 
                for i in range(len(sistema_fiscal)):
                    if nome_fiscal == sistema_fiscal[i][0]:
                        del sistema_fiscal[i]

        elif opcao1 == '7': # Sair do programa 
            print('Saindo do programa...')
            break

        else:
            print('Entrada inválida, selecione outro!')


if __name__ == '__main__':
    main()
