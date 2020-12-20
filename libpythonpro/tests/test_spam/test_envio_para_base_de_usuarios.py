from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.tests.test_spam.conftest import sessao


def test_envio_de_spam(sessao):
    enviador_de_span= EnviadorDeSpam(sessao, Enviador())
    enviador_de_span.enviar_emails(
        'leonardo.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
