import sqlite3

DB = "banco_ficticio.db"

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    # Apaga tabelas antigas
    cur.execute("DROP TABLE IF EXISTS pedidos;")
    cur.execute("DROP TABLE IF EXISTS clientes;")
    con.commit()

    # Cria tabela clientes
    cur.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        cidade TEXT
    );
    """)

    # Cria tabela pedidos
    cur.execute("""
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        produto TEXT NOT NULL,
        valor REAL NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id)
    );
    """)
    con.commit()

    # Inserir clientes
    clientes = [
        ("Ana Silva", "ana@email.com", "(62)99999-1111", "Goiânia"),
        ("Bruno Santos", "bruno@email.com", "(62)98888-2222", "Anápolis"),
        ("Carlos Oliveira", "carlos@email.com", "(21)98888-3333", "Rio de Janeiro"),
        ("Mariana Costa", "mariana@email.com", "(31)97777-4444", "Belo Horizonte"),
        ("Fernanda Lima", "fernanda@email.com", "(64)95555-5555", "Rio Verde"),
        ("Fábio Mendes", "fabio@email.com", "(62)96666-5555", "Goiânia")
    ]
    cur.executemany(
        "INSERT INTO clientes (nome, email, telefone, cidade) VALUES (?, ?, ?, ?);",
        clientes
    )
    con.commit()

    # Inserir pedidos
    pedidos = [
        (1, "Notebook", 3500.00),
        (1, "Mouse", 120.00),
        (2, "Cadeira Gamer", 950.00),
        (3, "Celular", 2500.00),
        (4, "Teclado", 220.00),
        (5, "Monitor", 890.00),
        (6, "Headset", 310.00),
        (6, "Pen Drive 64GB", 50.00)
    ]
    cur.executemany(
        "INSERT INTO pedidos (id_cliente, produto, valor) VALUES (?, ?, ?);",
        pedidos
    )
    con.commit()

    print("✅ Banco 'banco_ficticio.db' criado e populado com sucesso!\n")

    # Exibir clientes formatados com traços
    print("👥 CLIENTES")
    print("-" * 60)
    print(f"{'ID':<5} {'Nome':<20} {'Cidade':<20}")
    print("-" * 60)
    cur.execute("SELECT id, nome, cidade FROM clientes ORDER BY id;")
    for id_, nome, cidade in cur.fetchall():
        print(f"{id_:<5} {nome:<20} {cidade:<20}")
    print("-" * 60)

    # Exibir pedidos formatados com traços
    print("\n📦 PEDIDOS")
    print("-" * 60)
    print(f"{'ID':<5} {'Cliente':<10} {'Produto':<20} {'Valor (R$)':>10}")
    print("-" * 60)
    cur.execute("SELECT id, id_cliente, produto, valor FROM pedidos ORDER BY id;")
    for id_, id_cliente, produto, valor in cur.fetchall():
        print(f"{id_:<5} {id_cliente:<10} {produto:<20} {valor:>10.2f}")
    print("-" * 60)

    con.close()



if __name__ == "__main__":
    main()
