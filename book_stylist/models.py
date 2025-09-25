# /book_stylist/models.py

class Livro:
    """Classe que representa a entidade Livro no banco de dados."""
    def __init__(self, titulo, autor, ano_publicacao, genero_literario, best_seller, pais, idioma, id=None):
        self.id = id  # Adicionado ID para ser usado em operações de CRUD
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero_literario = genero_literario
        # Converte a entrada para booleano ou int (MySQL usa 0 e 1 para BOOLEAN)
        self.best_seller = 1 if best_seller in (True, 1, 's', 'S') else 0
        self.pais = pais
        self.idioma = idioma

    def __str__(self):
        """Retorna uma representação amigável do objeto Livro."""
        best_seller_str = "Sim" if self.best_seller == 1 else "Não"
        return (f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano_publicacao} | "
                f"Gênero: {self.genero_literario} | Best Seller: {best_seller_str} | País: {self.pais} | Idioma: {self.idioma}")


class Cliente:
    """Classe que representa a entidade Cliente (o leitor do Book Stylist)."""
    def __init__(self, nome, preferencias_genero, estilo_leitura, id=None):
        self.id = id
        self.nome = nome
        self.preferencias_genero = preferencias_genero
        self.estilo_leitura = estilo_leitura

    def __str__(self):
        """Retorna uma representação amigável do objeto Cliente."""
        return (f"ID: {self.id} | Cliente: {self.nome} | Pref. Gênero: {self.preferencias_genero} | "
                f"Estilo Leitura: {self.estilo_leitura}")


class Avaliacao:
    """Classe que representa a avaliação de um livro por um cliente."""
    def __init__(self, id_cliente, id_livro, nota, comentario, id=None):
        self.id = id
        self.id_cliente = id_cliente
        self.id_livro = id_livro
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        """Retorna uma representação amigável do objeto Avaliacao."""
        return (f"ID: {self.id} | Cliente ID: {self.id_cliente} | Livro ID: {self.id_livro} | "
                f"Nota: {self.nota}/5 | Comentário: {self.comentario}")
