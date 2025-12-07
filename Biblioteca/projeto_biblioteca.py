import sqlite3


# CONEXÃO COM O BANCO
conexao = sqlite3.connect("banco_biblioteca.db")
cursor = conexao.cursor()


# TABELAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
    FOREIGN KEY (livro_id) REFERENCES livros (id)
)
""")

conexao.commit()


clientes = [
    ("Ana Souza", "ana@email.com", "11987654321"),
    ("Bruno Lima", "bruno@email.com", "11999998888"),
    ("Carla Mendes", "carla@email.com", "11888887777"),
    ("Diego Pereira", "diego@email.com", "11777776666"),
    ("Elaine Rocha", "elaine@email.com", "11666665555"),
    ("Fabio Santos", "fabio@gmail.com", "11555554444"),
    ("Gabriela Alves", "gabriela@gmail.com", "11444443333")
]

cursor.execute("DELETE FROM clientes;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='clientes';")
cursor.executemany("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", clientes)


livros = [
    ("O Alquimista", "Paulo Coelho", 1988, 39.90, 15),
    ("1984", "George Orwell", 1949, 45.50, 10),
    ("Dom Casmurro", "Machado de Assis", 1899, 29.90, 12),
    ("A Revolução dos Bichos", "George Orwell", 1945, 35.00, 8),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 42.00, 9),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 25.00, 20),
    ("A Metamorfose", "Franz Kafka", 1915, 27.50, 10),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 99.00, 5),
    ("O Hobbit", "J.R.R. Tolkien", 1937, 59.90, 7),
    ("A Divina Comédia", "Dante Alighieri", 1320, 49.90, 6),
    ("Hamlet", "William Shakespeare", 1603, 33.00, 11),
    ("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, 38.00, 4)
]
cursor.execute("DELETE FROM livros;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='livros';")
cursor.executemany("""
INSERT INTO livros (titulo, autor, ano, preco, estoque)
VALUES (?, ?, ?, ?, ?);
""", livros)


pedidos = [
    (1, 120.80),
    (2, 235.50),
    (3, 150.90),
    (4, 90.00),
    (5, 199.80),
    (1, 85.40),
    (3, 49.90),
    (5, 89.80),
    (2, 70.00),
    (4, 50.00)
]
cursor.execute("DELETE FROM pedidos;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='pedidos';")
cursor.executemany("INSERT INTO pedidos (cliente_id, total) VALUES (?, ?)", pedidos)


itens_pedido = [
    (1, 1, 2, 39.90),   
    (1, 2, 1, 45.50),  
    (2, 4, 2, 35.00),   
    (3, 10, 3, 49.90),  
    (4, 6, 2, 25.00),   
    (5, 9, 2, 59.90),   
    (5, 3, 1, 29.90),
    (6, 1, 1, 39.90),   
    (6, 5, 1, 42.00),   
    (7, 10, 1, 49.90),  
    (8, 2, 1, 45.50),   
    (8, 7, 1, 27.50),   
    (9, 4, 2, 35.00),   
    (10, 6, 2, 25.00)   
]

cursor.execute("DELETE FROM itens_pedido;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='itens_pedido';")
cursor.executemany("""
INSERT INTO itens_pedido (pedido_id, livro_id, quantidade, preco_unitario)
VALUES (?, ?, ?, ?);
""", itens_pedido)

conexao.commit()



print("\n==========================")
print("CONSULTAS SQL AVANÇADAS")
print("==========================\n")



print("1️  Pedidos com nome do cliente e valor total\n")
cursor.execute("""
SELECT 
    p.id AS pedido_id,
    c.nome AS cliente,
    p.total AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
ORDER BY p.id;
""")
for pedido_id, cliente, total in cursor.fetchall():
    print(f"Pedido {pedido_id:<3} | Cliente: {cliente:<20} | Total: R$ {total:.2f}")
print("\n" + "-"*80 + "\n")


print("2️  Itens de cada pedido com cliente e subtotal\n")
cursor.execute("""
SELECT 
    p.id AS pedido_id,
    c.nome AS cliente,
    l.titulo AS livro,
    ip.quantidade,
    ip.preco_unitario,
    (ip.quantidade * ip.preco_unitario) AS subtotal
FROM itens_pedido ip
JOIN pedidos p ON ip.pedido_id = p.id
JOIN clientes c ON p.cliente_id = c.id
JOIN livros l ON ip.livro_id = l.id
ORDER BY p.id;
""")
for pedido_id, cliente, livro, qtd, preco, subtotal in cursor.fetchall():
    print(f"Pedido {pedido_id:<3} | {cliente:<20} | {livro:<25} | "
          f"Qtd: {qtd:<2} | Preço: R$ {preco:<6.2f} | Subtotal: R$ {subtotal:.2f}")
print("\n" + "-"*80 + "\n")



print("3️  Total de vendas por cliente\n")
cursor.execute("""
SELECT 
    c.nome AS cliente,
    SUM(p.total) AS total_gasto
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
GROUP BY c.nome
ORDER BY total_gasto DESC;
""")
for cliente, total in cursor.fetchall():
    print(f"Cliente: {cliente:<20} | Total gasto: R$ {total:.2f}")
print("\n" + "-"*80 + "\n")



print("4️  Livros mais vendidos\n")
cursor.execute("""
SELECT 
    l.titulo,
    SUM(ip.quantidade) AS total_vendido
FROM itens_pedido ip
JOIN livros l ON ip.livro_id = l.id
GROUP BY l.titulo
HAVING total_vendido > 0
ORDER BY total_vendido DESC;
""")
for titulo, total in cursor.fetchall():
    print(f"{titulo:<30} | Vendidos: {total}")
print("\n" + "-"*80 + "\n")


print("5️  Livros nunca vendidos\n")
cursor.execute("""
SELECT 
    l.titulo
FROM livros l
LEFT JOIN itens_pedido ip ON l.id = ip.livro_id
WHERE ip.livro_id IS NULL;
""")
livros_nunca_vendidos = cursor.fetchall()
if livros_nunca_vendidos:
    for (titulo,) in livros_nunca_vendidos:
        print(f"{titulo}")
else:
    print("Todos os livros foram vendidos pelo menos uma vez.")
print("\n" + "-"*80 + "\n")


print("6  Estatísticas gerais de livros\n")
cursor.execute("""
SELECT
    COUNT(*) AS total_livros,
    SUM(estoque) AS total_em_estoque,
    AVG(preco) AS preco_medio,
    MAX(preco) AS livro_mais_caro,
    MIN(preco) AS livro_mais_barato
FROM livros;
""")
total_livros, total_estoque, media, caro, barato = cursor.fetchone()
print(f"Total de livros cadastrados: {total_livros}")
print(f"Quantidade total em estoque: {total_estoque}")
print(f"Preço médio: R$ {media:.2f}")
print(f"Livro mais caro: R$ {caro:.2f}")
print(f"Livro mais barato: R$ {barato:.2f}")


print("\n==========================")
print("FIM DAS CONSULTAS")
print("==========================\n")

cursor.close()
conexao.close()