from src.service.service_user import ServiceUser


class TestServiceUser:

#   TESTANDO MÉTODO ADD_USER
    def test_add_user_sucesso(self):
        #SetUp
        service = ServiceUser()
        resultado_esperado = "Usuário adicionado"
        #Chamada
        resultado = service.add_user("Gildo", "Analista")
        #Avaliação
        assert resultado == resultado_esperado

    def test_add_user_falha_tipo(self):
        # SetUp
        service = ServiceUser()
        resultado_esperado = "Um dos parametros não são do tipo string"

        # Chamada
        resultado = service.add_user([], "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_falha_none(self):
        # SetUp
        service = ServiceUser()
        resultado_esperado = "Um dos parâmetros está vazio"

        # Chamada
        resultado = service.add_user(None, "Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_falha_nome_repetido(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02") #Adicionando um usuário igual antes
        resultado_esperado = "Usuario já existe"

        # Chamada
        resultado = service.add_user("Gildo", "Analista")

        # Avaliação
        assert resultado == resultado_esperado

#TESTANDO MÉTODO REMOVE_USER
    def test_remove_user_sucesso(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02")
        resultado_esperado = "Usuário removido!"

        # Chamada
        resultado = service.remove_user("Gildo")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_falha_tipo(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02")
        resultado_esperado = "Erro de tipo no nome"

        # Chamada
        resultado = service.remove_user([])

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_falha_none(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02")
        resultado_esperado = "Um dos parâmetros está vazio"

        # Chamada
        resultado = service.remove_user(None)

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_falha_nao_repetido(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02")
        resultado_esperado = "Usuário não existe!"

        # Chamada
        resultado = service.remove_user("Gildo 02")

        # Avaliação
        assert resultado == resultado_esperado

#TESTANDO MÉTODO UPDATE_USER
    def test_update_user_sucesso(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista")
        resultado_esperado_mensagem = "Profissão atualizada"

        # Chamada
        resultado_mensagem = service.update_user("Gildo", "Analista de Testes")

        # Avaliação
        assert resultado_mensagem == resultado_esperado_mensagem

    def test_update_user_falha_tipo(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista")
        resultado_esperado = "Um dos parametros não são do tipo string"

        # Chamada
        resultado = service.update_user([],"Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_falha_none(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista")
        resultado_esperado = "Um dos parâmetros está vazio"

        # Chamada
        resultado = service.update_user(None,"Analista")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_falha_nao_repetido(self):
        # SetUp
        service = ServiceUser()
        service.add_user("Gildo", "Analista02")
        resultado_esperado = "Usuário não existe!"

        # Chamada
        resultado = service.update_user("Gildo 02", "Analista")

        # Avaliação
        assert resultado == resultado_esperado