class Disco:
    def __init__(self, titulo, tempo_reproducao, possuo, comentario):
        self.titulo = titulo
        self.tempo_reproducao = tempo_reproducao
        self.possuo = possuo
        self.comentario = comentario
        self.lista = [self.titulo, self.tempo_reproducao, self.possuo, self.comentario]
        self.info_dicionario = None

    def inserirDisco(self, dic, cont):
        dic['CD/DVD - ' + str(cont)] = self.lista[:]
        self.info_dicionario = dic

    def exibirDisco(self):
        print('-------- [Titulo>Tempo_de_reprodução>possuo>comentario] --------')
        print(self.info_dicionario)

    def localizarDisco(self, resp):
        self.info_dicionario['CD/DVD - ' + str(resp)] = ''


class Dvd(Disco):
    def __init__(self,diretor):
        self.diretor = diretor
    #def inserirDisco(self, dic, cont):
        #self.lista.append(self.diretor)
        #dic['Dvd - ' + str(cont)] = self.lista[:]
        #self.info_dicionario = dic
        #print(self.info_dicionario)


class Cd(Disco):
    def __init__(self, artista,numero_trilhas):
        self.artista = artista
        self.numero_trilhas = numero_trilhas

    #def inserirDisco(self, dic, cont):
        #self.lista.append(self.artista,self.numero_trilhas)
        #dic['Cd - ' + str(cont)] = self.lista[:]
        #self.info_dicionario = dic
        #print(self.info_dicionario)