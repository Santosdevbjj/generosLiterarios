## Book Stylist System: Curadoria de Livros Personalizada.

Este projeto é uma ferramenta de gerenciamento e recomendação de livros, desenvolvida para simular o trabalho de um Book Stylist – um profissional que faz a curadoria de leituras personalizadas para seus clientes.

O sistema utiliza a Programação Orientada a Objetos (POO) em Python e um banco de dados MySQL para fornecer uma solução completa, modular e inteligente.

Execução Alternativa (Google Colab)
O Google Colab foi o ambiente inicial de desenvolvimento e permite testar rapidamente o projeto sem a necessidade de uma configuração local completa do Python.

Para iniciar o notebook com o ambiente pré-configurado e os passos iniciais de instalação, clique no botão abaixo:
Caminho do Notebook: generosLiterarios/GenerosLivros.ipynb
📚 Visão Geral e Funcionalidades do Sistema
| Funcionalidade | Descrição | Especialidade |
|---|---|---|
| CRUD Completo (3 Entidades) | Implementação das operações Create, Read, Update e Delete para Livros, Clientes e Avaliações, garantindo a gestão total dos dados. | Banco de Dados e POO |
| Lógica de Recomendação Híbrida | Geração de recomendações inteligentes baseadas em 1) Preferências de Gênero (do cliente), 2) Popularidade (livros com alta nota média), e 3) Exclusão de livros já lidos/avaliados. | Algoritmos e SQL Avançado |
| Arquitetura Modular | Separação clara de responsabilidades em módulos (models, database, main), ideal para desenvolvimento profissional. | Engenharia de Software |
| Tratamento de Erros | Uso de blocos try...except e funções auxiliares de validação para garantir a robustez do sistema contra inputs inválidos do usuário (Ex: digitar texto onde se espera um número). | Robustez de Código |
📂 Estrutura Detalhada do Repositório
O projeto segue uma arquitetura modular clara, onde cada arquivo tem uma responsabilidade única.
| Arquivo/Pasta | Caminho Completo | Função Principal e Especialidade |
|---|---|---|
| main.py | /main.py | Ponto de Entrada e Interface de Usuário. Contém o Menu Interativo, o tratamento de inputs e a orquestração do sistema. |
| GenerosLivros.ipynb | /GenerosLivros.ipynb | Notebook Google Colab para testes rápidos e execução em ambientes de nuvem. |
| requirements.txt | /requirements.txt | Lista as dependências Python necessárias para o projeto (mysql-connector-python). |
| book_stylist/ | /book_stylist | Pacote Principal da Lógica de Negócio. |
| database.py | /book_stylist/database.py | Camada de Acesso a Dados (DAO). Contém a classe GerenciadorBookStylist, responsável pela conexão MySQL, CRUD e pela lógica de Recomendação. |
| models.py | /book_stylist/models.py | Camada de Modelos de Dados (Entidades). Classes Livro, Cliente e Avaliacao, seguindo o princípio da POO. |
🛠️ Pré-Requisitos e Configuração do Ambiente
Requisitos de Software
| Componente | Requisito | Notas |
|---|---|---|
| Python | Versão 3.6 ou superior | Linguagem de desenvolvimento principal. |
| MySQL Server | Versão 5.7 ou superior | Obrigatoriamente necessário para armazenar os dados e rodar o projeto. |
| Dependência Python | mysql-connector-python | Biblioteca para a conexão com o MySQL. |
Requisitos de Hardware
O projeto é muito leve e didático, exigindo recursos mínimos para execução:
 * Processador: CPU de 1.0 GHz ou superior.
 * Memória RAM: Mínimo de 2 GB.
 * Espaço em Disco: Cerca de 100 MB.
🚀 Passo a Passo Completo para Execução
1. Clonar o Repositório e Instalar Dependências
Abra seu terminal e prepare o ambiente:
# Clone o repositório
git clone https://github.com/Santosdevbjj/generosLiterarios.git

# Acesse a pasta do projeto
cd generosLiterarios

# Instale as dependências (ambiente virtual é recomendado, mas opcional)
pip install -r requirements.txt

2. Configurar o MySQL
 * Inicie o Servidor MySQL: Certifique-se de que o seu servidor MySQL esteja rodando em sua máquina.
 * Verifique as Credenciais: O projeto está configurado para usar as seguintes credenciais, que você deve configurar em seu servidor ou alterar diretamente no construtor da classe GerenciadorBookStylist no arquivo /book_stylist/database.py:
   * Host: localhost
   * Usuário: usuario_crud
   * Senha: senha123
   * Nome do DB: book_stylist_db (Será criado automaticamente se não existir).
3. Executar o Script Principal
Inicie o sistema a partir do terminal:
python main.py

O sistema tentará se conectar, criar as tabelas e, em seguida, exibirá o menu interativo.
✅ Como Testar e Validar as Funcionalidades
Para validar a inteligência do sistema de recomendação, siga estes passos:
 * Carga Inicial:
   * Opção 1: Adicione pelo menos 5 livros, variando os gêneros (Ficção, Romance, Suspense) e o status best_seller.
   * Opção 2 > Opção 1: Adicione um cliente, preenchendo o campo Preferências de Gênero com valores separados por vírgula (Ex: "Suspense, Thriller").
 * Registro de Interações (Avaliações):
   * Opção 2 > Opção 4: Adicione avaliações para o cliente recém-criado.
     * Dê Nota 4 ou 5 para livros que correspondam aos seus gêneros preferidos.
     * NÃO avalie os livros que você espera que sejam recomendados.
 * Teste de Recomendação:
   * Opção 3: Digite o ID do seu cliente.
   * Validação: O sistema deve sugerir os livros de Gênero preferido que o cliente NÃO avaliou, priorizando aqueles com a maior nota média (popularidade), comprovando o funcionamento da lógica híbrida do book stylist.
