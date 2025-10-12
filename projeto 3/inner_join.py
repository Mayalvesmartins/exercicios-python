import sqlite3
import sys

DB = "banco_ficticio.db"

def tables_exist(cur):
    cur.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' 
        AND name IN ('clientes', 'pedidos');
    """)
    found = [r[0] for r in cur.fetchall()]
    return 'clientes' in found and 'pedidos' in found


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    # Verifica se as tabelas existem
    if not tables_exist(cur):
        print("❌ ERRO: tabelas 'clientes' e/ou 'pedidos' não encontradas.")
        print("➡️ Rode primeiro o script: setup_db.py")
        con.close()
        sys.exit(1)

    try:
        cur.execute("""
            SELECT c.id, c.nome, c.cidade,COALESCE (p.produto,0), COALESCE (p.valor,0)
            FROM clientes c
            LEFT JOIN pedidos p ON c.id = p.id_cliente
            ORDER BY c.id, p.id;
        """)

        rows = cur.fetchall()

        print("\n📦 Tabela de pedidos (INNER JOIN):\n")
        print(f"{'ID':<3} {'Nome':<20} {'Cidade':<18} {'Produto':<20} {'Valor (R$)':>10}")
        print("-" * 75)

        for idc, nome, cidade, produto, valor in rows:
            print(f"{idc:<3} {nome:<20} {cidade:<18} {produto:<20} {valor:>10.2f}")

    except sqlite3.OperationalError as e:
        print("⚠️ Erro na consulta:", e)
        print("Verifique o esquema do banco (colunas esperadas: clientes(id,nome,cidade) e pedidos(id,id_cliente,produto,valor)).")

    finally:
        con.close()


if __name__ == "__main__":
    main()
