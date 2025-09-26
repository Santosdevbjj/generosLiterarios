# 📚 Book Stylist System: Curadoria de Livros Personalizada

Bem-vindo ao projeto **Book Stylist**!  
Este sistema foi desenvolvido em **Python** com **Programação Orientada a Objetos (POO)** e integra um banco de dados **MySQL** para simular o trabalho de um *Book Stylist*: um profissional que faz a curadoria e recomenda livros de forma personalizada.

---

## 🚀 Para quem é este projeto?

Este repositório foi pensado especialmente para:

- **Iniciantes em Python**, que desejam aprender com um projeto prático e didático.
- Estudantes de **POO (Programação Orientada a Objetos)**.
- Interessados em conhecer como funciona a integração entre **Python e MySQL**.
- Pessoas que querem criar um sistema **CRUD** completo (*Create, Read, Update, Delete*).
- Curiosos que amam livros e tecnologia! 📖💻

---

## 🔎 Funcionalidades do Sistema

- **CRUD Completo (3 Entidades):**  
  Gerenciamento de **Livros**, **Clientes** e **Avaliações**.

- **Recomendação de Livros Inteligente:**  
  Baseada em:
  1. Preferências de gênero do cliente.  
  2. Popularidade (nota média das avaliações).  
  3. Exclusão automática de livros já lidos/avaliados.

- **Arquitetura Modular:**  
  Separação do código em camadas (modelos, banco de dados e execução principal).  

- **Robustez:**  
  Uso de `try...except` para tratamento de erros e entradas inválidas.

---

## 📂 Estrutura do Repositório

generosLiterarios ├── .gitignore ├── README.md ├── main.py                # Ponto de entrada do sistema (menu interativo) ├── requirements.txt       # Dependências do projeto ├── book_stylist/          # Pacote principal da lógica │   ├── init.py │   ├── database.py        # Conexão com o MySQL + CRUD + recomendação │   └── models.py          # Classes Livro, Cliente e Avaliacao ├── GenerosLivros.ipynb    # Notebook para testes no Google Colab ├── spyder.md              # Guia de instalação e uso da IDE Spyder └── vsCode.md              # Guia de instalação e uso da IDE VSCode

---

## 🛠️ Pré-Requisitos

Antes de rodar o projeto, você precisará ter:

- **Python** 3.6 ou superior  
- **MySQL Server** 5.7 ou superior  
- Biblioteca Python: `mysql-connector-python`

Instale as dependências com:

```bash
pip install -r requirements.txt

```
---

🖥️ **Como Executar o Projeto Localmente**

1. Clone o repositório:



git clone https://github.com/Santosdevbjj/generosLiterarios.git
cd generosLiterarios

**2. Configure o MySQL:**



**Inicie o servidor MySQL.**

O projeto está configurado no arquivo book_stylist/database.py com os parâmetros:

Host: localhost

Usuário: usuario_crud

Senha: senha123



> ⚠️ O banco book_stylist_db será criado automaticamente.



**3. Execute o sistema:**



python main.py

O menu interativo será exibido para você navegar entre as funcionalidades.


---

🎓 **Execução Alternativa (Google Colab)**

Você também pode rodar o projeto sem instalar nada localmente.
Abra o notebook no Google Colab:

ggg## 🎓 Execução Alternativa (Google Colab)

Você também pode rodar o projeto sem instalar nada localmente.  
Abra o notebook diretamente no Google Colab clicando na badge abaixo:


[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Santosdevbjj/generosLiterarios/blob/main/GenerosLivros.ipynb)

**Caminho do Notebook:** `generosLiterarios/GenerosLivros.ipynb`



---

✅ **Como Testar a Recomendação**

1. Adicione Livros (Opção 1).


2. Cadastre um Cliente com preferências claras (Opção 2 > Opção 1).


3. Registre Avaliações para alguns livros (Opção 2 > Opção 4).

Dê notas altas (4 ou 5) para livros que correspondam ao gosto do cliente.

Não avalie livros que você deseja que sejam recomendados.



**4. Teste a Recomendação (Opção 3) digitando o ID do cliente.**

O sistema irá sugerir livros do gênero favorito, ainda não avaliados, priorizando os mais bem avaliados por outros leitores.




---

💡 **Aprendizados com este Projeto**

Estruturar um sistema em POO com Python.

Usar MySQL para persistência de dados.

Criar um CRUD completo em Python.

Implementar uma lógica simples de sistema de recomendação.

Configurar IDEs (VSCode e Spyder) para Python.



---

📜 **Licença**

Este projeto está licenciado sob a MIT License.


---

👨‍💻 **Desenvolvido por** Sérgio Santos
🌟 Se este repositório te ajudou, não esqueça de deixar uma star no projeto!

---



