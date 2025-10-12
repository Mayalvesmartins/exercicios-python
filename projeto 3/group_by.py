import sqlite3
import sys

DB = "banco_ficticio.db"

def tables_exist(cur):
    cur.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' 
        AND name IN ('clientes','pedidos');
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
            SELECT
                c.cidade,
                COUNT(p.id) AS total_pedidos,
                COALESCE(SUM(p.valor), 0) AS total_valor
            FROM clientes c
            LEFT JOIN pedidos p ON c.id = p.id_cliente
            GROUP BY c.cidade
            ORDER BY total_valor DESC;
        """)

        rows = cur.fetchall()

        print("\n🏙️ Total de pedidos e valor por cidade:\n")
        print(f"{'Cidade':<20} {'Pedidos':>7} {'Valor total (R$)':>18}")
        print("-" * 50)

        for cidade, total_pedidos, total_valor in rows:
            print(f"{cidade:<20} {total_pedidos:>7} {total_valor:>18.2f}")

    except sqlite3.OperationalError as e:
        print("⚠️ Erro na consulta:", e)

    finally:
        con.close()


if __name__ == "__main__":
    main()
