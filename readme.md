# CodeLeap Backend Test

Este repositório implementa a API para o teste de backend usando Django e Django REST Framework (DRF). A aplicação foi desenvolvida para gerenciar posts conforme descrito no teste.

## Requisitos

- Python 3.10+
- Django 4.0+
- Django REST Framework
- Um ambiente virtual (recomendado)

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone <url_do_repositorio>
   cd codeleap_project
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações para configurar o banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Estrutura da API

A API gerencia os posts com os seguintes endpoints:

### Criar um Post
**Endpoint:** `POST /careers/`

**Body:**
```json
{
  "username": "string",
  "title": "string",
  "content": "string"
}
```

**Resposta:**
```json
{
  "id": "number",
  "username": "string",
  "created_datetime": "datetime",
  "title": "string",
  "content": "string"
}
```

### Listar Posts
**Endpoint:** `GET /careers/`

**Resposta:**
```json
[
  {
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
  }
]
```

### Atualizar um Post
**Endpoint:** `PATCH /careers/{id}/`

**Body:**
```json
{
  "title": "string",
  "content": "string"
}
```

**Resposta:**
```json
{
  "id": "number",
  "username": "string",
  "created_datetime": "datetime",
  "title": "string",
  "content": "string"
}
```

### Deletar um Post
**Endpoint:** `DELETE /careers/{id}/`

**Resposta:**
Nenhum conteúdo retornado.

## Estrutura do Projeto

```
codeleap_project/
├── codeleap_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
├── manage.py
└── requirements.txt
```

## Dependências

As dependências principais do projeto são:

- Django
- Django REST Framework

Para instalar todas as dependências, execute:
```bash
pip install -r requirements.txt
```

## Observações
- Certifique-se de adicionar uma barra ("/") ao final dos endpoints para evitar problemas de CORS, devido ao funcionamento do Django.
- O campo `username` é imutável após a criação de um post.

