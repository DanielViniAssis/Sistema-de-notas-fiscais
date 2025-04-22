# Sistema-de-notas-fiscais
Este é um sistema de controle de notas fiscais desenvolvido em Python utilizando o framework Flask. O objetivo do sistema é permitir o gerenciamento de notas fiscais, incluindo o cadastro, visualização e armazenamento de informações relacionadas.

![image](https://github.com/user-attachments/assets/de1c6bfa-8b56-420e-bdbd-52114de64446)
![image](https://github.com/user-attachments/assets/21d4c97b-7b67-4f49-b30d-7f4fc5156c18)

## Funcionalidades

- **Login e Autenticação**:
  - Sistema de login com validação de e-mail e senha.
  - Hashing de senhas utilizando a biblioteca `bcrypt`.

- **Cadastro de Notas Fiscais**:
  - Formulário para cadastro de notas fiscais com campos como:
    - Categoria do item.
    - Número da nota fiscal.
    - Nome do produto/serviço.
    - Quantidade, valor e descrição.
    - CPF/CNPJ do fornecedor.
    - Nome da empresa e endereço.
    - Data de emissão e data de pagamento.
  - Validação de dados no backend.

- **Mensagens de Feedback**:
  - Exibição de mensagens de sucesso ou erro ao usuário utilizando o `flash` do Flask.

- **Banco de Dados**:
  - Gerenciamento de dados utilizando o ORM `Peewee`.
  - Suporte para SQLite como banco de dados.

## Tecnologias Utilizadas

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) - Framework web.
  - [Peewee](http://docs.peewee-orm.com/) - ORM para gerenciamento do banco de dados.
  - [bcrypt](https://pypi.org/project/bcrypt/) - Hashing de senhas.

- **Frontend**:
  - HTML5, CSS3 e Bootstrap para estilização.
  - Templates Jinja2 para renderização dinâmica.

- **Outras Bibliotecas**:
  - `Flask-SQLAlchemy` para integração com o banco de dados.
  - `webargs` para validação de dados.

## Estrutura do Projeto
### controle-de-inventario/ ├── app.py 
### Arquivo principal do aplicativo Flask ├── config.py 
### Configuração do aplicativo e banco de dados ├── requirements.txt 
### Dependências do projeto ├── .gitignore
### Arquivos e pastas ignorados pelo Git ├── routes/ 
### Rotas do aplicativo │ ├── login_page.py 
### Rotas relacionadas ao login │ ├── invoice_registration.py
### Rotas para cadastro de notas fiscais ├── templates/ 
### Templates HTML │ ├── login_page.html
### Página de login │ ├── invoice_registration.html 
### Página de cadastro de notas fiscais ├── static/
### Arquivos estáticos (CSS, imagens, etc.) │ ├── login_page.css 
### Estilo da página de login │ ├── invoice_registration.css
### Estilo da página de cadastro │ ├── image.png 
### Imagem usada no projeto └── models/ 
### Modelos do banco de dados ├── user.py 
### Modelo para usuários ├── invoice_registration.py 

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Ambiente virtual configurado.
