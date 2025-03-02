# Desafio Django

Este projeto é um exemplo de aplicação Django que gerencia usuários e permite pesquisar filmes usando a API OMDB.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- requests

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio/desafio
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:

    ```sh
    python manage.py migrate
    ```

5. Colete os arquivos estáticos:

    ```sh
    python manage.py collectstatic
    ```

6. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

## Estrutura do Projeto

- `app_filme/`: Contém a aplicação principal do Django.
  - `models.py`: Define os modelos `Usuario` e `Filme`.
  - `views.py`: Contém as views para registrar, listar, detalhar, atualizar e deletar usuários, além de pesquisar filmes.
  - `forms.py`: Define os formulários `UsuarioForm` e `FilmeForm`.
  - `templates/`: Contém os templates HTML para as views.

## Configuração

Certifique-se de que as seguintes configurações estão corretas no arquivo `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

Uso
Gerenciamento de Usuários
Registrar Usuário: Acesse /register para registrar um novo usuário.
Listar Usuários: Acesse /list para ver a lista de usuários.
Detalhar Usuário: Acesse /detail/<id> para ver os detalhes de um usuário.
Atualizar Usuário: Acesse /update/<id> para atualizar um usuário.
Deletar Usuário: Acesse /delete/<id> para deletar um usuário.
Pesquisa de Filmes
Pesquisar Filme: Acesse /pesquisar_filme para pesquisar um filme usando a API OMDB.
Contribuição
Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/nova-feature).
Commit suas mudanças (git commit -am 'Adiciona nova feature').
Faça um push para a branch (git push origin feature/nova-feature).
Crie um novo Pull Request.
Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
