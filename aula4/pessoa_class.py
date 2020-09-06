class Pessoa():

    def __init__(self, nome, idade, cor_cabelo, numero_celular):
        self.nome = nome
        self.idade = idade
        self.cor_cabelo = cor_cabelo
        self.numero_celular = numero_celular

    def respirar(self):
        print("{} está RESPIRANDO! ".format(self.nome))

    def saber_cabelo(self):
        print("A cor do cabelo é {}".format(self.cor_cabelo))

    def saber_idade(self):
        print("{} tem {} anos!".format(self.nome, self.idade))
    
    def saber_nome(self):
        print("Essa pessoa se chama {}".format(self.nome))
    
    def saber_numero(self):
        print("O numero para contato é {}".format(self.numero_celular))


class Aluno(Pessoa):

    def __init__(self, nome, idade, cor_cabelo, numero_celular, disciplina, numero_matricula):
        super().__init__(nome, idade, cor_cabelo, numero_celular)
        self.disciplina = disciplina
        self.numero_matricula = numero_matricula
    
    def estudar(self):
        print("O aluno {} está estudando {}!".format(self.nome, self.disciplina))

    def saber_disciplina(self):
        print("A disciplina é {}".format(self.disciplina))

    def saber_matricula(self):
        print("A matricula do aluno {} é {} ".format(self.nome, self.numero_matricula))


class Responsavel(Pessoa):

    def __init__(self, nome, idade, cor_cabelo, numero_celular, responsavel_por_quem):
        super().__init__(nome, idade, cor_cabelo, numero_celular)
        self.responsavel_por_quem = responsavel_por_quem
    
    def verificar(self):
        print("{} está responsavel por verificar as ações do(a) jovem {}".format(self.nome, self.responsavel_por_quem))
    
    def saber_responsavel(self):
        print("{} é responsavel por {}".format(self.nome, self.responsavel_por_quem))


class Professor(Pessoa):

    def __init__(self, nome, idade, cor_cabelo, numero_celular, disciplica_ministrada):
        super().__init__(nome, idade, cor_cabelo, numero_celular)
        self.disciplica_ministrada = disciplica_ministrada

    def ministrar_aula(self):
        print("O professor {} esta ministrando a aula de {} nesse momento!".format(self.nome, self.disciplica_ministrada))

    def saber_disciplina_ministrada(self):
        print("A disciplina que esse professor ministra é {}".format(self.disciplica_ministrada))

class Coordenador(Pessoa):
    
    def __init__(self, nome, idade, cor_cabelo, numero_celular, curso_cordenado):
        super().__init__(nome, idade, cor_cabelo, numero_celular)
        self.curso_cordenado = curso_cordenado
    
    def coordenar(self):
        print("O coordenador(a) {}, está gerindo o curso de {}".format(self.nome, self.curso_cordenado))

    def saber_curso_cordenado(self):
        print("O curso coordenado é {}".format(self.curso_cordenado))

class Diretor(Pessoa):

    def __init__(self, nome, idade, cor_cabelo, numero_celular, nome_escola):
        super().__init__(nome, idade, cor_cabelo, numero_celular)
        self.nome_escola = nome_escola
    
    def gerir(self):
        print("O diretor(a) {}, está gerindo esta a escola {}".format(self.nome, self.nome_escola))

    def saber_escola(self):
        print("A escola que esta sendo regida é {} ".format(self.nome_escola))






