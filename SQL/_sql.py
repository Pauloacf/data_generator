import sqlite3


def generate_sql():
    conn = sqlite3.connect('./SQL/tabela.sql')
    cursor = conn.cursor()

    # lendo a quantidade de linhas do arquivo
    arquivo = open('names.txt', 'r')
    linhas = len(arquivo.readlines())

    # adicionando os dados em uma lista de tuplas
    lista = []
    arquivo = open('names.txt', 'r')
    for i in range(linhas):
        a = arquivo.readline().rstrip('\n').split()
        nome = ''
        cont = 0
        for i in a:
            if ',' in i:
                nome += i.rstrip(',')
                cont += 1
                break
            else:
                nome += i+' '
                cont += 1
        idade = a[cont]
        telefone = a[cont+2].rstrip(',')
        cont = cont+3
        rua = ''
        for i in a[cont::]:
            if ',' in i:
                rua += i.rstrip(',')
                cont += 1
                break
            else:
                rua += i+' '
                cont += 1

        uf = ''
        for i in a[cont::]:
            if ',' in i:
                uf += i.rstrip(',')
                cont += 1
                break
            else:
                uf += i+' '
                cont += 1
        cep = a[cont]
        tupla = (nome, idade, telefone, rua, uf, cep)
        lista.append(tupla)
    arquivo.close()

    # inserindo os dados da lista na tabela criada

    cursor.executemany("""
    INSERT INTO tabela (nome, idade, telefone, rua, uf, cep)
    VALUES (?,?,?,?,?,?)
    """, lista)

    conn.commit()

    print('dados inseridos')

    conn.close()
