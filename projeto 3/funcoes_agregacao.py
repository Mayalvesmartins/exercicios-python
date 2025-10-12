import sqlite3
import sys

DB = "banco_ficticio.db"

def tables_exist(cur):
    cur.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' 
        AND name='pedidos';
    """)
    found = [r[0] for r in cur.fetchall()]
    return 'pedidos' in found


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    # Verifica se a tabela existe
    if not tables_exist(cur):
        print("❌ ERRO: tabela 'pedidos' não encontrada. Rode primeiro: setup_db.py")
        con.close()
        sys.exit(1)

    try:
        cur.execute("""
            SELECT
                COUNT(*) AS total_pedidos,
                SUM(valor) AS soma_valores,
                AVG(valor) AS media_valores,
                MAX(valor) AS maior_valor,
                MIN(valor) AS menor_valor
            FROM pedidos;
        """)

        total, soma, media, maior, menor = cur.fetchone()

        print("\n📊 Funções de agregação sobre 'pedidos':\n")
        print(f"Total de pedidos  : {total}")
        print(f"Soma dos valores  : R$ {soma if soma is not None else 0:.2f}")
        print(f"Média dos valores : R$ {media if media is not None else 0:.2f}")
        print(f"Maior valor       : R$ {maior if maior is not None else 0:.2f}")
        print(f"Menor valor       : R$ {menor if menor is not None else 0:.2f}")

    except sqlite3.OperationalError as e:
        print("⚠️ Erro na consulta:", e)

    finally:
        con.close()


if __name__ == "__main__":
    main()
