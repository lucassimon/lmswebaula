# LMS WebAula

[![CircleCI](https://circleci.com/gh/lucassimon/lmswebaula/tree/master.svg?style=svg)](https://circleci.com/gh/lucassimon/lmswebaula/tree/master)

[![Coverage Status](https://coveralls.io/repos/github/lucassimon/lmswebaula/badge.svg?branch=master)](https://coveralls.io/github/lucassimon/lmswebaula?branch=master)

## Pre requisitos

Instalar as bibliotecas no sistema operacional

`sudo apt install libxml2-dev libxslt-dev`

## Instalar os pacotes do requirements.

`pip install requirements.txt`

## Executar os testes

Conferir as credenciais em cada arquivo de teste

Executar o comando `pytest` para executar todos os testes.

Para executar os testes por recursos faça:

`pytest tests/trail/test_api.py::TrailCustomizedTestCase::test_matricular_aluno_em_disciplina`

Onde, `TrailCustomizedTestCase`, nome da classe de teste e `test_matricular_aluno_em_disciplina` é o nome do teste.

## Como contribuir

`pip install requirements-dev.txt`