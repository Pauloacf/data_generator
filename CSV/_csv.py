import csv


def generate_csv():
    arquivo_csv = open('./CSV/data.csv', 'w')
    arquivo_data = open('names.txt', 'r')
    texto = arquivo_data.readlines()

    for reader in texto:
        linha = reader.split(',')
        for coluna in range(5):
            arquivo_csv.write('{},'.format(linha[coluna]))
        arquivo_csv.write('{}'.format(str(linha[5]).rstrip('\\n')))
    arquivo_csv.close()
    arquivo_data.close()
