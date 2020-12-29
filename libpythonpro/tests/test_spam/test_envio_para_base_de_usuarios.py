import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Vizagre', email='kimi.vizagre@gmail.com'),
            Usuario(nome='Amanda', email='kimi.vizagre@gmail.com')
        ],
        [
            Usuario(nome='Vizagre', email='kimi.vizagre@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_span = EnviadorDeSpam(sessao, enviador)
    enviador_de_span.enviar_emails(
        'leonardo.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vizagre', email='kimi.vizagre@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_span = EnviadorDeSpam(sessao, enviador)
    enviador_de_span.enviar_emails(
        'amanda.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
    assert enviador.parametros_de_envio == (
        'amanda.vizagre@gmail.com',
        'kimi.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )