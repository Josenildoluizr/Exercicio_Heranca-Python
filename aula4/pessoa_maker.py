from pessoa_class import Pessoa
from pessoa_class import Aluno
from pessoa_class import Professor
from pessoa_class import Responsavel
from pessoa_class import Coordenador
from pessoa_class import Diretor

pessoa = Pessoa("Kiara", 15, "loiro", 6526531337)
pessoa.saber_nome()
pessoa.saber_numero()
pessoa.saber_idade()
pessoa.saber_cabelo()

aluno = Aluno("Marcos", 18, "castanho escuro", 3125374710, "Matematica", 66574)
aluno.saber_nome()
aluno.saber_numero()
aluno.saber_idade()
aluno.saber_cabelo()
aluno.saber_matricula()

professor = Professor("João", 34, "branco", 40026315, "Educação fisica")
professor.saber_nome()
professor.saber_numero()
professor.saber_idade()
professor.saber_cabelo()
professor.ministrar_aula()
professor.saber_disciplina_ministrada()

responsavel = Responsavel("Antonio", 35, "azul", 5341283100, "Marcos")
responsavel.saber_nome()
responsavel.saber_numero()
responsavel.saber_idade()
responsavel.saber_cabelo()
responsavel.saber_responsavel()
responsavel.verificar()

coordenador = Coordenador("José", 40, "escuro", 351371930,"Enfermagem")
coordenador.saber_nome()
coordenador.saber_numero()
coordenador.saber_idade()
coordenador.saber_cabelo()
coordenador.coordenar()
coordenador.saber_curso_cordenado()


diretor = Diretor("Ana", 45, "preto", 625103841, "ETEEAMMMA")
diretor.saber_nome()
diretor.saber_numero()
diretor.saber_idade()
diretor.saber_cabelo()
diretor.gerir()
