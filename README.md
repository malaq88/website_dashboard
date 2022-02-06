# Website Dashboard API

Este repositório contem a base para execução de uma APIs Rest desenvolvida usando Django Rest Framework.

A API se chama **Website Dashboard** e basicamente detêm o trabalho de gerir o cadastro de *usuários*, *posts* e *services* no sistema e administrar que os mesmos possam ser visualizados, editados, escluidos e listados de acordo com seu path de execução e método enviado via post.

### Tecnologias Utilizadas

» Python

» Django

» Django Rest FrameWork

» Pytest

» Swagger

» Redoc

» Docker

» Docker Compose

» PostgreSQL

### Requisitos

Este projeto foi pensado para executar sobre o Docker, embora esteja numa versão inicial e itens relacionados à segurança do ambiente podem ser incrementados. 

## Serão necessários:

» Docker

» Docker Compose

» Git

## Instruções para execução

Após realizar o clone deste repositório, você deverá navegar até ele e digitar o seguinte comando (ambiente Linux ou Mac):

$ docker-compose up --build

O docker irá baixar as imagens e gerar os contêineres necessários ao processo.

## Instruções para execução de testes

Com o servidor executando em servidor de desenvolvimento http://localhost:8000

* Crie um ambiente virtual com: $ python -m venv venv_name
* Ative-o: $ source venv_name/bin/activate
* Instale as dependências do projeto: $ pip install -r requirements.txt
* Execute o comando *pytest*

## APIs e Endpoints

### Website Dashboard API
O acesso base a esta API se dará por meio da porta 8000 no localhost. Basicamente o acesso deverá ser feito em:

http://localhost:8000

## Users

#### Cadastro, listagem e detalhamento individual de usuários (endpoints públicos*)

* **[POST]   /user/**: JSON Body: (username, first_name, last_name, email, password, is_active)
* **[GET]    /user**: Listagem de todos os usuários cadastrados
* **[GET]    /user/:id**: Detalhes do usuário com ID informado na rota
* **[DELETE] /user/:id**: Remove um usuário do banco

## Posts
#### Cadastro, listagem e detalhamento individual de Publicações (endpoints públicos*)

* **[POST]   /posts/**: JSON Body: (_id, title, content, author)
* **[GET]    /posts**: Listagem de posts cadastrados
* **[GET]    /posts/:_id**: Detalhes do post com _id informado na rota
* **[DELETE] /posts/:_id**: Remove um post do banco
## Services

#### Cadastro, listagem e detalhamento individual de usuários (endpoints públicos*)

* **[POST]   /services/**: JSON Body: ('_id', 'title', 'description', 'price')
* **[GET]    /services**: Listagem de todos os serviços cadastrados
* **[GET]    /services/:id**: Detalhes do serviços com ID informado na rota
* **[DELETE] /services/:_id**: Remove um serviço do banco


#### Documentação

* **[POST] /api/swagger/**: Documentação Swagger
* **[POST] /api/redoc/**: Documentação Redoc