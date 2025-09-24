# Book Stylist System

Este projeto é uma ferramenta didática de gerenciamento e recomendação de livros, desenvolvida em Python e MySQL. O objetivo é simular as funcionalidades de um "book stylist", um profissional que faz a curadoria de leituras personalizadas para seus clientes.

---

## Funcionalidades
- **CRUD (Create, Read, Update, Delete)** de livros, clientes e avaliações.
- **Recomendação de Livros**: O sistema pode sugerir leituras com base nas preferências e avaliações de cada cliente.

## Tecnologias Utilizadas
- **Python 3**
- **MySQL**
- **mysql-connector-python**: Biblioteca para conexão com o banco de dados.

## Estrutura do Projeto

- `main.py`: Ponto de entrada do sistema. Contém o menu interativo.
- `book_stylist/`: Pasta que contém a lógica do sistema.
    - `database.py`: Gerencia a conexão com o MySQL e as operações de CRUD.
    - `models.py`: Define as classes de dados (`Livro`, `Cliente`, `Avaliacao`).

## Como Rodar o Projeto

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure o MySQL:**
    Certifique-se de que o MySQL esteja instalado e rodando em sua máquina. Crie um banco de dados e um usuário com permissões. Altere as credenciais no arquivo `database.py`.




3.  **Execute o script:**
    ```bash
    python main.py
    ```
O menu interativo será exibido no seu terminal.
