# Aplicação de Agendamento de Automações com Django

Esta é uma aplicação desenvolvida em Python utilizando o framework Django. A aplicação tem como objetivo permitir o agendamento de automações.

## Tecnologias Utilizadas

A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- Python: Linguagem de programação utilizada para desenvolver a aplicação.
- Django: Framework web de alto nível que fornece uma arquitetura MVC para desenvolver aplicativos web.
- Docker: Plataforma de código aberto que facilita a criação, o empacotamento e o fornecimento de aplicativos em contêineres.

## Como Executar a Aplicação

Para executar a aplicação localmente, é necessário ter o Docker instalado em sua máquina. Siga os passos abaixo:

1. Clone o repositório para sua máquina local: `git clone https://github.com/arturcavalcantej/django-webscraping.git`

2. Navegue para o diretório do projeto:

```bash
cd django-webscraping
```
Inicie a aplicação usando o Docker Compose:
```bash
docker-compose up
```

O Docker Compose se encarregará de construir e iniciar os contêineres necessários para a aplicação funcionar corretamente. Após a execução do comando acima, a aplicação estará disponível em http://localhost:8000/.

Funcionalidades Principais
A aplicação possui as seguintes funcionalidades principais:

Cadastro de Robôs de Webscrapping: Permite cadastrar informações sobre robôs de webscrapping.

Agendamento de Automações: Permite criar agendamentos para execução dos robôs de webscrapping em horários específicos.

## Utilização

Para utilizar a aplicação acesse o localhost:8000/admin , vá em Executions, crie uma nova Execution e em seguida selecione a action criada e acione o action ' Custom action'
Após isso o execution criado, sera preenchido com os dados retirados da pagina

## Obs: Devido ao curto tempo foi possivel implementar apenas a extração de dados para o PNCP,  porém toda arquitetura foi planejanada para futuras implementações de extrações de dados em outras plataformas


## Configuração do Ambiente de Desenvolvimento
Caso queira contribuir para o desenvolvimento da aplicação, siga os passos abaixo para configurar o ambiente de desenvolvimento:

Navegue para o diretório do projeto:


```	bash
cd django-webscraping
```	

Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```	
A aplicação estará disponível em http://localhost:8000/.
