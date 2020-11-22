import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['leonardo.vizagre@gmail.com', 'foo@bar.com.br']
)
def test_rementente(remetente):
    enviador = Enviador()
    resultado=enviador.enviar(
        remetente,
        'amanda.vizagre@gmail.com',
        'Teste de envio',
        'Testando envio de e-mail.'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)


def test_rementente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'amanda.vizagre@gmail.com',
            'Teste de envio',
            'Testando envio de e-mail.'
        )
