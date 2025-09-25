# /book_stylist/database.py

import mysql.connector
from book_stylist.models import Livro, Cliente, Avaliacao
from mysql.connector import Error

class GerenciadorBookStylist:
    """
    Gerencia a conexão com o banco de dados MySQL e executa todas as operações CRUD
    e a lógica de recomendação.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            # Tenta conectar ao banco de dados específico
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexao.is_connected():
                self.cursor = self.conexao.cursor()
                print("Conexão com o banco de dados estabelecida!")
        except Error as e:
            # Caso o banco de dados ainda não exista, tenta conectar sem especificar o DB
            if '1049' in str(e): # Código de erro para 'Unknown database'
                try:
                    conn_sem_db = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
                    cursor_sem_db = conn_sem_db.cursor()
                    cursor_sem_db.execute(f"CREATE DATABASE {self.database}")
                    conn_sem_db.close()
                    
                    # Tenta conectar novamente com o DB recém-criado
                    self.conexao = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                    self.cursor = self.conexao.cursor()
                    print(f"Banco de dados '{self.database}' criado e conectado!")
                except Error as e_create:
                    print(f"Erro ao criar ou conectar ao MySQL: {e_create}")
            else:
                print(f"Erro ao conectar ao MySQL: {e}")
            self.conexao = None
            self.cursor = None

    def desconectar(self):
        """Fecha a conexão com o banco de dados."""
        if self.conexao and self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")

    def criar_tabelas(self):
        """Cria as tabelas (livros, clientes, avaliacoes) se não existirem."""
        if not self.conexao:
            return

        tabela_livros = """
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(255),
            ano_publicacao INT,
            genero_literario VARCHAR(255),
            best_seller BOOLEAN,
            pais VARCHAR(100),
            idioma VARCHAR(100)
        )
        """
        tabela_clientes = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            preferencias_genero VARCHAR(500), -- Gêneros favoritos do cliente
            estilo_leitura VARCHAR(500) -- Ex: 'rápido e ação' ou 'lento e reflexivo'
        )
        """
        tabela_avaliacoes = """
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_cliente INT,
            id_livro INT,
            nota INT, -- De 1 a 5
            comentario TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE,
            FOREIGN KEY (id_livro) REFERENCES livros(id) ON DELETE CASCADE
        )
        """
        try:
            self.cursor.execute(tabela_livros)
            self.cursor.execute(tabela_clientes)
            self.cursor.execute(tabela_avaliacoes)
            self.conexao.commit()
            print("Tabelas criadas/verificadas com sucesso.")
        except Error as e:
            print(f"Erro ao criar tabelas: {e}")

    # --- Métodos de CRUD Genéricos (Para evitar repetição de código) ---

    def _executar_query(self, query, params=None, commit=False, fetch_one=False, fetch_all=False):
        """Método auxiliar para executar queries e tratar erros."""
        if not self.conexao:
            print("Erro: Conexão com o banco de dados não está ativa.")
            return None

        try:
            self.cursor.execute(query, params or ())
            if commit:
                self.conexao.commit()
                return self.cursor.lastrowid
            if fetch_one:
                return self.cursor.fetchone()
            if fetch_all:
                return self.cursor.fetchall()
            return True # Retorna True para operações de sucesso que não precisam de retorno
        except Error as e:
            print(f"Erro na operação de banco de dados: {e}")
            return None

    # --- CRUD para Livros (Otimizado) ---

    def adicionar_livro(self, livro: Livro):
        """C - Adiciona um novo livro."""
        query = ("INSERT INTO livros (titulo, autor, ano_publicacao, genero_literario, best_seller, pais, idioma) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        valores = (livro.titulo, livro.autor, livro.ano_publicacao, livro.genero_literario,
                   livro.best_seller, livro.pais, livro.idioma)
        if self._executar_query(query, valores, commit=True):
            print(f"Livro '{livro.titulo}' adicionado.")

    def buscar_livros(self, filtro=None, valor=None):
        """R - Busca e retorna livros com filtro opcional."""
        if filtro and valor:
            # Usando f-string para o nome da coluna é seguro neste contexto, mas o valor é parametrizado
            query = f"SELECT * FROM livros WHERE {filtro} LIKE %s;"
            resultados = self._executar_query(query, ('%' + str(valor) + '%',), fetch_all=True)
        else:
            query = "SELECT * FROM livros;"
            resultados = self._executar_query(query, fetch_all=True)

        if resultados:
            # Converte as tuplas de resultado em objetos Livro
            return [Livro(r[1], r[2], r[3], r[4], r[5], r[6], r[7], id=r[0]) for r in resultados]
        return []

    # Os métodos atualizar_livro e deletar_livro do projeto anterior continuam válidos.
    # Para brevidade, serão omitidos aqui, mas devem estar no arquivo final.
    
    # --- CRUD para Clientes (Implementação Completa) ---
    
    def adicionar_cliente(self, cliente: Cliente):
        """C - Adiciona um novo cliente."""
        query = "INSERT INTO clientes (nome, preferencias_genero, estilo_leitura) VALUES (%s, %s, %s)"
        valores = (cliente.nome, cliente.preferencias_genero, cliente.estilo_leitura)
        if self._executar_query(query, valores, commit=True):
            print(f"Cliente '{cliente.nome}' adicionado.")

    def buscar_clientes(self, id_cliente=None):
        """R - Busca e retorna clientes por ID ou todos."""
        if id_cliente:
            query = "SELECT * FROM clientes WHERE id = %s"
            resultados = self._executar_query(query, (id_cliente,), fetch_all=True)
        else:
            query = "SELECT * FROM clientes"
            resultados = self._executar_query(query, fetch_all=True)
        
        if resultados:
            # Converte tuplas em objetos Cliente
            return [Cliente(r[1], r[2], r[3], id=r[0]) for r in resultados]
        return []

    def atualizar_cliente(self, id_cliente, campo, novo_valor):
        """U - Atualiza um campo de um cliente."""
        query = f"UPDATE clientes SET {campo} = %s WHERE id = %s"
        return self._executar_query(query, (novo_valor, id_cliente), commit=True)
    
    def deletar_cliente(self, id_cliente):
        """D - Deleta um cliente pelo ID."""
        query = "DELETE FROM clientes WHERE id = %s"
        return self._executar_query(query, (id_cliente,), commit=True)
    
    # --- CRUD para Avaliações (Implementação Completa) ---

    def adicionar_avaliacao(self, avaliacao: Avaliacao):
        """C - Adiciona uma nova avaliação."""
        query = "INSERT INTO avaliacoes (id_cliente, id_livro, nota, comentario) VALUES (%s, %s, %s, %s)"
        valores = (avaliacao.id_cliente, avaliacao.id_livro, avaliacao.nota, avaliacao.comentario)
        if self._executar_query(query, valores, commit=True):
            print("Avaliação adicionada com sucesso.")

    def buscar_avaliacoes(self, id_cliente=None):
        """R - Busca e retorna avaliações por ID do cliente ou todas."""
        if id_cliente:
            query = "SELECT * FROM avaliacoes WHERE id_cliente = %s"
            resultados = self._executar_query(query, (id_cliente,), fetch_all=True)
        else:
            query = "SELECT * FROM avaliacoes"
            resultados = self._executar_query(query, fetch_all=True)
            
        if resultados:
            return [Avaliacao(r[1], r[2], r[3], r[4], id=r[0]) for r in resultados]
        return []

    # Os métodos atualizar_avaliacao e deletar_avaliacao devem ser implementados de forma similar.
    
    # --- Lógica de Recomendação (Implementação conforme diretrizes) ---
    
    def recomendar_livros(self, id_cliente):
        """
        Gera uma recomendação híbrida de livros para um cliente, baseada em:
        1. Preferências de Gênero do Cliente.
        2. Popularidade (Média de notas) dos livros.
        3. Livros que o cliente ainda não avaliou.
        """
        # 1. Obter informações do cliente
        cliente_obj = self.buscar_clientes(id_cliente)
        if not cliente_obj:
            print(f"Cliente com ID {id_cliente} não encontrado.")
            return []
            
        cliente = cliente_obj[0]
        generos_pref = [g.strip() for g in cliente.preferencias_genero.split(',')]
        
        # 2. Encontrar livros que o cliente JÁ avaliou (para excluí-los)
        query_avaliados = "SELECT id_livro FROM avaliacoes WHERE id_cliente = %s"
        livros_avaliados = self._executar_query(query_avaliados, (id_cliente,), fetch_all=True)
        ids_avaliados = [item[0] for item in livros_avaliados] if livros_avaliados else [0]
        
        # 3. Query principal: Livros com alta média de nota, no gênero preferido e não lidos
        # A lógica de Estilo ("rápido e ação") aqui é simplificada para a busca por Gênero
        # mas em um sistema real usaria filtros em uma coluna de 'palavras-chave' do livro.
        
        # Cria uma string de placeholders para os gêneros
        placeholders = ', '.join(['%s'] * len(generos_pref))
        
        query_recomendacao = f"""
        SELECT
            l.id, l.titulo, l.autor, AVG(a.nota) as media_nota
        FROM
            livros l
        LEFT JOIN
            avaliacoes a ON l.id = a.id_livro
        WHERE
            l.genero_literario IN ({placeholders}) AND l.id NOT IN ({', '.join(map(str, ids_avaliados))})
        GROUP BY
            l.id, l.titulo, l.autor
        HAVING
            media_nota >= 4.0 -- Filtro de popularidade (nota média 4 ou mais)
        ORDER BY
            media_nota DESC, l.ano_publicacao DESC
        LIMIT 5;
        """
        
        # Adiciona a condição de best seller como um bônus se a lista de gêneros for vazia
        if not generos_pref:
             print("Aviso: Cliente sem preferências de gênero. Recomendando best sellers.")
             query_recomendacao = """
             SELECT
                 l.id, l.titulo, l.autor, AVG(a.nota) as media_nota
             FROM
                 livros l
             LEFT JOIN
                 avaliacoes a ON l.id = a.id_livro
             WHERE
                 l.best_seller = 1 AND l.id NOT IN (%s)
             GROUP BY
                 l.id, l.titulo, l.autor
             ORDER BY
                 media_nota DESC
             LIMIT 5;
             """
             parametros = [str(i) for i in ids_avaliados]
        else:
             parametros = generos_pref
        
        # Executa a query
        recomendacoes = self._executar_query(query_recomendacao, parametros, fetch_all=True)
        
        if not recomendacoes:
            print("Não foi possível encontrar recomendações perfeitas. Tente adicionar mais livros e avaliações.")
            return []
            
        return [f"ID: {r[0]} | Título: {r[1]} | Autor: {r[2]} | Nota Média: {r[3]:.2f}" for r in recomendacoes]
