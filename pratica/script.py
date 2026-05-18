import sqlite3

# Conecta (ou cria o arquivo)
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# Cria uma tabela
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)')

# Insere dados
cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', ('Fulano',))

# Salva e fecha
conexao.commit()
conexao.close()