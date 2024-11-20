from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if type(name) != str or type(job) != str:
                return "Um dos parametros não são do tipo string"
            user = User(name, job)

            for db_user in self.store.bd:
                if user.name == db_user.name:
                    return "Usuario já existe"

            self.store.bd.append(user)
            return "Usuário adicionado"

        return "Um dos parâmetros está vazio"

    def remove_user(self, name):
        if name is not None:
            if type(name) != str:
                return "Erro de tipo no nome"

            for db_user in self.store.bd:
                if name == db_user.name:
                    self.store.bd.remove(db_user)
                    return "Usuário removido!"
            else:
                return "Usuário não existe!"

        return "Um dos parâmetros está vazio"


    def update_user(self, name, job):
        if name is not None and job is not None:
            if type(name) != str or type(job) != str:
                return "Um dos parametros não são do tipo string"
            user = User(name, job)

            for db_user in self.store.bd:
                if user.name == db_user.name:
                    indice = self.store.bd.index(db_user)
                    self.store.bd[indice].job = user.job
                    return "Profissão atualizada"

            return "Usuário não existe!"

        return "Um dos parâmetros está vazio"

    def get_user_by_name(self, name):

        if name is not None:
            if type(name) != str:
                return "Nome não é do tipo string"

            for db_user in self.store.bd:
                if name == db_user.name:
                    return db_user
            return "Usuário não existe!"

        return "Nome está vazio"