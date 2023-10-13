# Projeto de Rest-API com Flask, Sqlalchemy, Marshmallow, PostgreSQL e Docker

![projeto_com_flask](projeto_com_flask.png)

## Descrição do Projeto

O projeto proposto visa criar uma Rest-API altamente eficiente, segura e facilmente escalável, utilizando uma combinação de tecnologias de ponta. A API será desenvolvida com o objetivo de fornecer um serviço robusto que possa ser facilmente expandido e mantido no futuro.

## Tecnologias Principais

- Flask
- Sqlalchemy
- Marshmallow
- PostgreSQL
- Docker

## Objetivos

- Desenvolver uma API robusta e segura.
- Implementar operações CRUD (Create, Read, Update, Delete) para manipulação de dados.
- Usar o PostgreSQL como banco de dados para armazenar informações de forma segura.
- Implementar validação de entrada e saída de dados com o Marshmallow.
- Utilizar contêineres Docker para facilitar a implantação e escalabilidade da aplicação.

## Como Iniciar

1. Clone este repositório.
2. Instale o Docker na maquina local.
3. Crie um arquivo .env com as variaveis:
   
   ```bash
   API_KEY = ""
   DATABASE_IP=
   DATABASE_NAME=
   DATABASE_PORT=
   DATABASE_USER=
   DATABASE_PASS=
   
4. Execute a aplicação.
  ```bash
    docker-compose up
