# SUPERMARKET API — Django Rest Framework

> [PT-BR] SUPERMARKET é um sistema simples para genrencia um estoque de supermecado.

> [EN-US] SUPERMARKET is a simple system for to manager a supermarket inventory

### Descrição / Description

> [PT-BR]

Esta API oferece autenticação por JWT (Bearer Token) e funcionalidades completas de gestão de Usuários e gestão de Produtos em estoque.

Considere executar as primeiras requisições com pelo menos com 1 superuser já inserido no Banco de Dados para gerar o Token.

##

> [EN-US]

This API provides JWT (Bearer Token) authentication and full functionalities for user management and management of products.

Consider making the initial requests with at least 1 superuser already inserted into the Database to generate the Token.


## Documentação da API / API Documentation

* [Link Postman](https://documenter.getpostman.com/view/32095562/2sA3JT1xKh#intro)


### Preparando ambiente Python / Preparing Python Environment

* [PT-BR] Criando Ambiente Virtual da API
* [EN-US] Creating Virtual Environment for the API
```bash
  cd api_supermarket
  python -m venv venv
  cd venv/scripts
  .\activate
  cd ../..
```

##

* [PT-BR] Instalando dependências
* [EN-US] Installing dependencies
```bash
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
```
##

* [PT-BR] Executando API Server
* [EN-US] Running API Server
```bash
  python manage.py runserver
```

## Stack utilizada / used

### Back-end:
* Python Django Rest Framework
