# To-Do List Application

Uma aplicação simples e eficiente para gerenciamento de tarefas, construída com React no frontend e FastAPI no backend.

## Visão Geral

Este projeto é uma aplicação de lista de tarefas que permite aos usuários:
- Criar novas tarefas com título e descrição
- Marcar tarefas como concluídas
- Excluir tarefas
- Visualizar data de criação de cada tarefa

## Stack Tecnológica

### Frontend
- React 19
- Axios para requisições HTTP
- CSS para estilização

### Backend
- FastAPI
- SQLAlchemy ORM
- MySQL

## Configuração e Instalação

### Pré-requisitos
- Node.js
- Python 3.8+
- MySQL

### Instalação do Frontend

1. Navegue até a pasta do frontend:
   ```
   cd frontend
   ```

2. Instale as dependências:
   ```
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```
   npm start
   ```

4. Acesse a aplicação em [http://localhost:3000](http://localhost:3000)

### Instalação do Backend

1. Navegue até a pasta do backend:
   ```
   cd backend
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:
   - Certifique-se de que o MySQL está em execução
   - Crie um banco de dados chamado `todo_db`
   - Ajuste as credenciais em `database.py` se necessário

4. Inicie o servidor FastAPI:
   ```
   uvicorn main:app --reload
   ```

5. O backend estará disponível em [http://localhost:8000](http://localhost:8000)

## Uso da API

### Endpoints disponíveis:

- `GET /todos` - Lista todas as tarefas
- `POST /todos` - Cria uma nova tarefa
- `PUT /todos/{id}` - Atualiza uma tarefa existente
- `DELETE /todos/{id}` - Exclui uma tarefa

## Recursos e Funcionalidades

- Adição de tarefas com título e descrição opcional
- Marcação de tarefas como concluídas
- Exclusão de tarefas
- Interface responsiva para desktop e dispositivos móveis
- Persistência de dados em banco de dados MySQL
- API RESTful para comunicação entre frontend e backend

## Possíveis Melhorias Futuras

- Autenticação de usuários
- Categorização de tarefas
- Definição de prioridades
- Lembretes e notificações
- Compartilhamento de tarefas entre usuários
