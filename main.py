from disco import *

dic = {}
opcao = 0
cont = 0
resp = int(input('Se voce deseja adicionar um DVD digite 1, mas se deseja adicionar um CD digite 0 \n'))
if resp == 1:
    print('Catalogo de dvd')

    while(opcao != 4):


        print('Bem vindo ao menu')
        print(" ----------------------------------- \n")
        print("1 --- INSERIR INFORMAÇÕES DO DVD\n")
        print("2 --- IMPRIMIR LISTA DE TODOS OS DVDS\n")
        print("3 --- REMOVER DVDS\n")
        print("4 --- SAIR\n")
        opcao = int(input('Digite a opção desejada\n'))

        if opcao == 1:
            cont = cont + 1
            titulo = input('Insira o titulo\n')
            tempo_reproducao = input('Insira o tempo de reprodução\n')
            diretor = input('Insira o nome do diretor\n')
            possuo = input('Você possui esse DVD?\n')
            comentario = input('Deixar um comentário\n')
            P1 = Dvd(diretor)
            P1 = Disco(titulo, tempo_reproducao, possuo, comentario)
            P1.inserirDisco(dic, cont)

        if (opcao == 2):
            P1.exibirDisco()

        if (opcao == 3):
            resp = int(input('coloque o numedo do indice do dvd que vc deseja deletar'))
            P1.localizarDisco(resp)
if resp == 0:
    print('Catalogo de Cd')

    while (opcao != 4):

        print('Bem vindo ao menu')
        print(" ----------------------------------- \n")
        print("1 --- INSERIR INFORMAÇÕES DO CD \n")
        print("2 --- IMPRIMIR LISTA DE TODOS OS CDS \n")
        print("3 --- REMOVER CDS \n")
        print("4 --- SAIR\n")
        opcao = int(input('Digite a opção desejada\n'))

        if opcao == 1:
            cont = cont + 1
            titulo = input('Insira o titulo\n')
            tempo_reproducao = input('Insira o tempo de reprodução\n')
            artista = input('Insira o nome do artista\n')
            numero_trilhas = input('Insira o numeor de trilhas\n')
            possuo = input('Você possui esse DVD?\n')
            comentario = input('Deixar um comentário\n')
            P1 = Cd(artista, numero_trilhas)
            P1 = Disco(titulo, tempo_reproducao, possuo, comentario)
            P1.inserirDisco(dic, cont)

        if (opcao == 2):
            P1.exibirDisco(cont)
            P1 = Cd(artista,numero_trilhas)

        if (opcao == 3):
            resp = int(input('Insira o número do indice do Cd od Dvd que vc deseja deletar'))
            P1.localizarDisco(resp)
