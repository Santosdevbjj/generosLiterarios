class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero_literario, best_seller, pais, idioma):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero_literario = genero_literario
        self.best_seller = best_seller
        self.pais = pais
        self.idioma = idioma

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero_literario}"

class Cliente:
    def __init__(self, nome, preferencias_genero, estilo_leitura):
        self.nome = nome
        self.preferencias_genero = preferencias_genero
        self.estilo_leitura = estilo_leitura

    def __str__(self):
        return f"Cliente: {self.nome} | Preferências: {self.preferencias_genero}"

class Avaliacao:
    def __init__(self, id_cliente, id_livro, nota, comentario):
        self.id_cliente = id_cliente
        self.id_livro = id_livro
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"Avaliação do cliente {self.id_cliente} para o livro {self.id_livro}: Nota {self.nota}"
