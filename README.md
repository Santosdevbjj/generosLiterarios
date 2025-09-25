# Book Stylist System: Curadoria de Livros Personalizada

Este projeto é uma ferramenta de gerenciamento e recomendação de livros, desenvolvida para simular o trabalho de um **Book Stylist** – um profissional que faz a curadoria de leituras personalizadas para seus clientes.

O sistema utiliza a **Programação Orientada a Objetos (POO)** em **Python** e um banco de dados **MySQL** para fornecer uma solução completa, modular e inteligente.

---

### Execução Alternativa (Google Colab)

O **Google Colab** foi o ambiente inicial de desenvolvimento e permite testar rapidamente o projeto sem a necessidade de uma configuração local completa do Python.

Para iniciar o notebook com o ambiente pré-configurado e os passos iniciais de instalação, clique no botão abaixo:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Santosdevbjj/generosLiterarios/blob/main/GenerosLivros.ipynb)

**Caminho do Notebook:** `generosLiterarios/GenerosLivros.ipynb`

---

### 📚 Visão Geral e Funcionalidades do Sistema

| Funcionalidade | Descrição | Especialidade |
| :--- | :--- | :--- |
| **CRUD Completo (3 Entidades)** | Implementação das operações **Create, Read, Update e Delete** para **Livros**, **Clientes** e **Avaliações**. | Banco de Dados e POO |
| **Lógica de Recomendação Híbrida** | Geração de recomendações inteligentes baseadas em **1) Preferências de Gênero**, **2) Popularidade** (nota média) e **3) Exclusão de livros já lidos/avaliados**. | Algoritmos e SQL Avançado |
| **Arquitetura Modular** | Separação clara de responsabilidades em módulos (`models`, `database`, `main`), ideal para desenvolvimento profissional. | Engenharia de Software |
| **Tratamento de Erros** | Uso de blocos `try...except` e validação para garantir a robustez do sistema contra *inputs* inválidos. | Robustez de Código |

---

### 📂 Estrutura Detalhada do Repositório

| Arquivo/Pasta | Caminho Completo | Função Principal e Especialidade |
| :--- | :--- | :--- |
| **`main.py`** | `/main.py` | **Ponto de Entrada e Interface de Usuário.** Contém o **Menu Interativo**, o tratamento de *inputs* e a orquestração do sistema. |
| **`GenerosLivros.ipynb`** | `/GenerosLivros.ipynb` | **Notebook Google Colab** para testes rápidos. |
| **`requirements.txt`** | `/requirements.txt` | Lista as dependências Python necessárias (`mysql-connector-python`). |
| **`book_stylist/`** | `/book_stylist` | **Pacote Principal da Lógica de Negócio.** |
| **`database.py`** | `/book_stylist/database.py` | **Camada de Acesso a Dados (DAO).** Contém a classe `GerenciadorBookStylist`, responsável pela conexão MySQL, CRUD e pela lógica de Recomendação. |
| **`models.py`** | `/book_stylist/models.py` | **Camada de Modelos de Dados (Entidades).** Classes `Livro`, `Cliente` e `Avaliacao`, seguindo o princípio da POO. |

---

### 🛠️ Pré-Requisitos e Configuração do Ambiente

#### Requisitos de Software

| Componente | Requisito | Notas |
| :--- | :--- | :--- |
| **Python** | Versão 3.6 ou superior | Linguagem de desenvolvimento principal. |
| **MySQL Server** | Versão 5.7 ou superior | **Obrigatoriamente** necessário para armazenar os dados e rodar o projeto. |
| **Dependência Python** | `mysql-connector-python` | Biblioteca para a conexão com o MySQL. |

#### Requisitos de Hardware

* **Processador:** CPU de 1.0 GHz ou superior.
* **Memória RAM:** Mínimo de 2 GB.

---

### 🚀 Passo a Passo Completo para Execução

#### 1. Clonar o Repositório e Instalar Dependências

```bash
git clone [https://github.com/Santosdevbjj/generosLiterarios.git](https://github.com/Santosdevbjj/generosLiterarios.git)
cd generosLiterarios
pip install -r requirements.txt

```
---


2. Configurar o MySQL
 * Inicie o Servidor MySQL: Garanta que o seu servidor MySQL esteja rodando.
 * Credenciais: O projeto está configurado no arquivo /book_stylist/database.py para:
   * Host: localhost
   * Usuário: usuario_crud
   * Senha: senha123
   * O DB book_stylist_db será criado automaticamente.

     
3. Executar o Script Principal
python main.py

O sistema tentará se conectar, criar as tabelas e exibirá o menu interativo.
✅ Como Testar e Validar as Funcionalidades
Para validar a inteligência do sistema de recomendação:
 * Carga Inicial: Adicione Livros (Opção 1) e um Cliente com preferências claras (Opção 2 > Opção 1).

 * Registro de Interações: Adicione Avaliações (Opção 2 > Opção 4) para o cliente. Dê Nota 4 ou 5 para livros que correspondam às suas preferências, mas NÃO avalie os livros que você deseja que sejam recomendados.

 * Teste de Recomendação: Use a Opção 3 e digite o ID do seu cliente. O sistema deve sugerir os livros de Gênero preferido que o cliente NÃO avaliou, priorizando a maior nota média.



