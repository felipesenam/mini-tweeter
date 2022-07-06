
# Mini-Tweeter

Mini-Tweeter é uma aplicação desenvolvida em Python Django, que implementa uma mini rede social se utilizando do conceito de API REST com Django restframework.

## Instalação

### Criação do ambiente virtual

É altamente recomendado para todo projeto, que este seja executado em um ambiente virtual. Para criar um novo ambiente virtual, você precisa ter instalado o `python-virtualenv` ou similar.

```bash
$ sudo apt update
$ sudo apt install python-virtualenv
```

E então, entre no diretório desejado, crie e ative o ambiente virtual

```bash
$ virtualenv _env
$ source _env/bin/activate
```

Feito isso, instale as dependências do projeto que estão descritas em `requirements.txt`

```bash
(_env) $ pip install -r requirements.txt
```

### Preparando o banco de dados

No primeiro uso, nem o banco (SQLite) nem suas respectivas tabelas foram criadas, portanto, realize as migrações do Django

```bash
(_env) $ python manage.py makemigrations
(_env) $ python manage.py migrate
```

### Coletando arquivos estáticos (produção)

Assim como o banco, os arquivos estáticos da aplicação ainda não estão prontos para uso, e portanto, mantidos nos diretórios de seus respectivos aplicativos.

```bash
(_env) $ python manage.py collectstatic
```

Feito isso, os arquivos estarão disponíveis em `tweeter/public/static`

### Criando um superusuário

Tendo o ambiente virtual ativado e com as dependências instaladas, agora podemos criar um superusuário.

```bash
(_env) $ cd tweeter
(_env) $ python manage.py createsuperuser
```

## Uso

### Executando o servidor de desenvolvimento

Tendo tudo pronto, agora podemos executar o servidor de desenvolvimento

```bash
(_env) $ python manage.py runserver
```

Você também pode especificar o endereço e a porta diferentes da padrão (`127.0.0.1:8000`) usando a opção `--bind`

## API

### Cadastro

Para realizar o cadastro via API, você precisa fazer uma requisição via **POST** em `/api/users`, informando seu nome, nome de usuário (username), email, data de nascimento (opcional) e senha.

### Autenticação

A API do Mini-Tweeter usa autenticação por token por meio da biblioteca `simple-jwt`.

A geração dos tokens é feita por meio de uma requisição informando nome de usuário e senha válidos via **POST** em `/api/token`. Feito isso, o usuário deverá receber como resposta dois tokens: `access` e `refresh`.

Para estar autenticado, a chave *Authentication* deve estar presente no cabeçalho da requisição contendo a chave de acesso no seguinte formato:

> Bearer `SUA_CHAVE_AQUI`

Dado um tempo, o token de acesso deve expirar. É possível recuperar um novo token de acesso válido fazendo uma requisição via **POST** em `/api/token/refresh`, apenas informando o token `refresh`, obtido anteriormente.

### Feed

Para receber o feed com os últimos Tweets feitos, basta fazer uma requisição por **GET** em `/api/feed`. Caso a requisição seja feita com o usuário autenticado, serão mostrados os 10 últimos Tweets que não são de sua autoria.

## Interface

O Mini-Tweeter também possui uma interface feita em HTML5 com CSS3, que torna o uso da aplicação mais intuitivo, organizado e prático, além de gerenciar automaticamente o uso de tokens.