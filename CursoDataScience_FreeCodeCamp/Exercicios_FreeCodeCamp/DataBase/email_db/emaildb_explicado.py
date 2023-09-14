import sqlite3

# Conecta-se ao banco de dados "emaildb.sqlite"
conn = sqlite3.connect('emaildb.sqlite')

# Cria um objeto cursor para executar comandos SQL
cur = conn.cursor()

# Exclui a tabela "Counts" se ela já existir
cur.execute('DROP TABLE IF EXISTS Counts')

# Cria a tabela "Counts" com as colunas "email" e "count"
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# Solicita ao usuário que insira o nome do arquivo ou usa um arquivo padrão "mbox-short.txt"
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

# Itera sobre cada linha do arquivo
for line in fh:
    # Verifica se a linha começa com "From: ", caso contrário, continua para a próxima linha
    if not line.startswith('From: '): continue

    # Divide a linha em palavras separadas
    pieces = line.split()
    # Extrai o email que está na segunda posição
    email = pieces[1]

    # Executa uma consulta para verificar se o email já existe na tabela
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    # Recupera a primeira linha de resultado da consulta
    row = cur.fetchone()

    # Se não houver resultado, insere uma nova linha com o email e count 1
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    # Caso contrário, atualiza a linha existente incrementando o count em 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))

    # Confirma as alterações no banco de dados
    conn.commit()

# Executa uma consulta para selecionar os 10 emails com a maior contagem (ordenados por count decrescente)
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Itera sobre cada linha de resultado da consulta e imprime o email e a contagem correspondente
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Fecha o cursor e a conexão com o banco de dados
cur.close()
