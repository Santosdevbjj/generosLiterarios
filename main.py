# /main.py

import mysql.connector
from book_stylist.database import GerenciadorBookStylist
from book_stylist.models import Livro, Cliente, Avaliacao
import sys

# --- Funções Auxiliares de Menu ---

def _input_int(prompt):
    """Função auxiliar para garantir que a entrada seja um número inteiro."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def _input_sim_nao(prompt):
    """Função auxiliar para garantir que a entrada seja 's' ou 'n'."""
    while True:
        valor = input(prompt).lower()
        if valor in ('s', 'n'):
            return valor == 's'
        print("Entrada inválida. Digite 's' para Sim ou 'n' para Não.")


# --- Menus de Gerenciamento ---

def menu_livros(gerenciador: GerenciadorBookStylist):
    """Menu para operações de CRUD de Livros."""
    while True:
        print("\n--- Gerenciamento de Livros ---")
        print("1. Adicionar Livro")
        print("2. Listar Todos")
        print("3. Buscar por Título/Autor/Gênero")
        print("4. Deletar Livro")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            try:
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = _input_int("Ano de Publicação: ")
                genero = input("Gênero Literário: ")
                best_seller = _input_sim_nao("É um Best Seller? (s/n): ")
                pais = input("País: ")
                idioma = input("Idioma: ")
                novo_livro = Livro(titulo, autor, ano, genero, best_seller, pais, idioma)
                gerenciador.adicionar_livro(novo_livro)
            except Exception as e:
                print(f"Erro ao adicionar livro: {e}")

        elif escolha == '2':
            print("\n--- Todos os Livros ---")
            livros = gerenciador.buscar_livros()
            for livro in livros:
                print(livro)
        
        elif escolha == '3':
            filtro = input("Buscar por (titulo/autor/genero_literario): ")
            valor = input(f"Valor a buscar em {filtro}: ")
            livros = gerenciador.buscar_livros(filtro, valor)
            if livros:
                 print("\n--- Livros Encontrados ---")
                 for livro in livros:
                     print(livro)
            else:
                print("Nenhum livro encontrado.")
        
        elif escolha == '4':
            id_deletar = _input_int("Digite o ID do livro para deletar: ")
            if gerenciador.deletar_livro(id_deletar):
                print(f"Livro ID {id_deletar} deletado com sucesso.")
            else:
                print(f"Falha ao deletar livro ID {id_deletar}.")

        elif escolha == '5':
            break

def menu_clientes(gerenciador: GerenciadorBookStylist):
    """Menu para operações de CRUD de Clientes e Avaliações."""
    while True:
        print("\n--- Gerenciamento de Clientes e Avaliações ---")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes")
        print("3. Adicionar Avaliação (Vínculo Cliente-Livro)")
        print("4. Listar Avaliações de um Cliente")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do Cliente: ")
            # Simulação da entrevista do Book Stylist
            generos = input("Gêneros Favoritos (separados por vírgula): ")
            estilo = input("Estilo de Leitura (Ex: rápido e ação, lento e reflexivo): ")
            novo_cliente = Cliente(nome, generos, estilo)
            gerenciador.adicionar_cliente(novo_cliente)
            
        elif escolha == '2':
            print("\n--- Clientes Cadastrados ---")
            clientes = gerenciador.buscar_clientes()
            for cliente in clientes:
                print(cliente)
        
        elif escolha == '3':
            id_cliente = _input_int("ID do Cliente que está avaliando: ")
            id_livro = _input_int("ID do Livro avaliado: ")
            nota = _input_int("Nota (1 a 5): ")
            comentario = input("Comentário: ")
            
            if 1 <= nota <= 5:
                nova_avaliacao = Avaliacao(id_cliente, id_livro, nota, comentario)
                gerenciador.adicionar_avaliacao(nova_avaliacao)
            else:
                print("Nota inválida. Deve ser entre 1 e 5.")

        elif escolha == '4':
            id_cliente = _input_int("ID do Cliente para ver avaliações: ")
            avaliacoes = gerenciador.buscar_avaliacoes(id_cliente)
            if avaliacoes:
                print(f"\n--- Avaliações do Cliente ID {id_cliente} ---")
                for av in avaliacoes:
                    print(av)
            else:
                print(f"Cliente ID {id_cliente} não possui avaliações.")

        elif escolha == '5':
            break

# --- Função Principal ---

def main():
    """Função principal que inicia e gerencia o loop do programa."""
    print("Iniciando o Sistema Book Stylist...")
    
    # IMPORTANTE: Use as credenciais do seu MySQL local/servidor
    gerenciador = GerenciadorBookStylist(
        host="localhost",
        user="usuario_crud",
        password="senha123",
        database="book_stylist_db" # Novo banco de dados para o projeto
    )

    gerenciador.conectar()
    if gerenciador.conexao is None:
        print("Falha na conexão inicial com o banco de dados. Verifique suas credenciais e o serviço MySQL.")
        sys.exit(1) # Sai do programa se não conectar

    gerenciador.criar_tabelas()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Livros (CRUD)")
        print("2. Gerenciar Clientes e Avaliações")
        print("3. Gerar Recomendação (Inteligência Book Stylist)")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_livros(gerenciador)
        
        elif escolha == '2':
            menu_clientes(gerenciador)

        elif escolha == '3':
            print("\n--- Gerar Recomendação ---")
            id_cliente = _input_int("Digite o ID do Cliente para recomendação: ")
            recomendacoes = gerenciador.recomendar_livros(id_cliente)
            
            if recomendacoes:
                print("\n✅ As 5 Melhores Recomendações Book Stylist:")
                for i, rec in enumerate(recomendacoes):
                    print(f"{i+1}. {rec}")
            else:
                print("⚠️ Não foi possível gerar recomendações no momento. O banco de dados pode estar vazio, ou o cliente não tem preferências claras.")

        elif escolha == '4':
            print("Encerrando o Sistema. Até logo!")
            gerenciador.desconectar()
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
