from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
     # insere_usuarios('rafael', '1234')
     # insere_usuarios('galleani', '4321')
     # consulta_todos_usuarios()
     # insere_pessoas()
     consulta_pessoas()
     # altera_pessoa()
     # exclui_pessoa()
