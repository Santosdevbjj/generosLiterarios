import mysql.connector
from book_stylist.database import GerenciadorBookStylist
from book_stylist.models import Livro, Cliente, Avaliacao

def exibir_menu():
    """Exibe o menu principal de opções para o usuário."""
    print("\n--- Sistema Book Stylist ---")
    print("1. Gerenciar Livros (CRUD)")
    print("2. Gerenciar Clientes (CRUD)")
    print("3. Gerar Recomendação para um Cliente")
    print("4. Sair")

def menu_livros(gerenciador):
    # Lógica para o menu de gerenciamento de livros (Adicionar, Listar, Buscar, Atualizar, Deletar)
    pass

def menu_clientes(gerenciador):
    # Lógica para o menu de gerenciamento de clientes
    pass

def main():
    """Função principal do programa."""
    gerenciador = GerenciadorBookStylist(
        host="localhost",
        user="usuario_crud",
        password="senha123",
        database="book_stylist_db"
    )
    gerenciador.conectar()
    if not gerenciador.conexao:
        print("Não foi possível conectar ao banco de dados. Encerrando o programa.")
        return

    gerenciador.criar_tabelas()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_livros(gerenciador)
        elif escolha == '2':
            menu_clientes(gerenciador)
        elif escolha == '3':
            # Implementação da lógica de recomendação
            print("Lógica de recomendação será implementada aqui.")
        elif escolha == '4':
            print("Saindo do sistema...")
            gerenciador.desconectar()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
