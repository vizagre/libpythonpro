from unittest.mock import Mock

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
    enviador = Mock()
    enviador_de_span = EnviadorDeSpam(sessao, enviador)
    enviador_de_span.enviar_emails(
        'leonardo.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vizagre', email='kimi.vizagre@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_span = EnviadorDeSpam(sessao, enviador)
    enviador_de_span.enviar_emails(
        'amanda.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
    enviador.enviar.assert_called_once_with == (
        'amanda.vizagre@gmail.com',
        'kimi.vizagre@gmail.com',
        'Curso Python Pro',
        'Módulo PyTools'
    )
