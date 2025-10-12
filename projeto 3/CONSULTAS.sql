SELECT * FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id

SELECT * FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id WHERE pedidos.valor > 2000

SELECT * FROM clientes LEFT JOIN pedidos ON pedidos.id_cliente = clientes.id

SELECT * FROM clientes RIGHT JOIN pedidos ON pedidos.id_cliente = clientes.id

SELECT * FROM clientes FULL OUTER JOIN pedidos ON pedidos.id_cliente = clientes.id

SELECT cidade, COUNT(*) as Quantidade FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY cidade

SELECT cidade, SUM(valor) as valor FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY cidade

SELECT cidade, AVG(valor) as valor FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY cidade

SELECT cidade, MIN(valor) as valor FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY cidade

SELECT nome, MAX(valor) as valor FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY nome

SELECT cidade, COUNT(*) as Quantidade FROM clientes INNER JOIN pedidos ON pedidos.id_cliente = clientes.id GROUP BY cidade HAVING COUNT(*) <= 4

