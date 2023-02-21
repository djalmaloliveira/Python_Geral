#https://www.youtube.com/watch?v=_q3j25ACmQ4


import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'inicio',
    database = 'bd_youtube'
)
cursor = conexao.cursor()

nome_produto = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: '))
# nome_produto = "Todinho"
# valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()
print(f'Produto {nome_produto}, Valor: {valor} adicionado com sucesso!')



cursor.close()
conexao.close()