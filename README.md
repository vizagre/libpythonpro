# libpythonpro
Módulo para exemplificar a construção de projetos python no curso PyTools

Link do curso [Python Pro](https://www.python.pro.br/)

[![Build Status](https://travis-ci.org/vizagre/libpythonpro.svg?branch=main)](https://travis-ci.org/vizagre/libpythonpro)
[![Updates](https://pyup.io/repos/github/vizagre/libpythonpro/shield.svg)](https://pyup.io/repos/github/vizagre/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/vizagre/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/vizagre/libpythonpro/)
[![codecov](https://codecov.io/gh/vizagre/libpythonpro/branch/main/graph/badge.svg?token=2RK86E6R1R)](https://codecov.io/gh/vizagre/libpythonpro)

Suportada a versão 3 de Python.

Para instalar:

```Console
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Para habilitar e desabilitar o virtualenv:

```Console
source .venv/bin/activate
which python

deactivate
```

Para executar os testes com cobertura:

```Console
pytest libpythonpro --cov=libpythonpro
```

Tópicos a serem abordados:
 1. Git;
 2. Virtualenv;
 3. Pip.