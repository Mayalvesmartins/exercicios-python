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

    cidade_filtro = "Goiânia"  # altere se quiser demonstrar outra cidade

    try:
        cur.execute("""
            SELECT c.id, c.nome, c.cidade, p.produto, p.valor
            FROM clientes c
            JOIN pedidos p ON c.id = p.id_cliente
            WHERE c.cidade = ?
            ORDER BY c.nome, p.id;
        """, (cidade_filtro,))
        rows = cur.fetchall()

        print(f"\n🧾 Pedidos de clientes da cidade de {cidade_filtro}:\n")
        print(f"{'ID':<3} {'Nome':<20} {'Cidade':<18} {'Produto':<20} {'Valor (R$)':>10}")
        print("-" * 75)

        if not rows:
            print("Nenhum pedido encontrado para essa cidade.")
        else:
            for idc, nome, cidade, produto, valor in rows:
                print(f"{idc:<3} {nome:<20} {cidade:<18} {produto:<20} {valor:>10.2f}")

    except sqlite3.OperationalError as e:
        print("⚠️ Erro na consulta:", e)

    finally:
        con.close()


if __name__ == "__main__":
    main()
