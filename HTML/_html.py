import html5lib


def generate_html():
    html_file = open('./HTML/data.html', 'w')
    data_file = open('names.txt', 'r')
    text = data_file.readlines()
    titles = ['Nome', 'Idade', 'Telefone', 'Rua', 'UF', 'CEP']

    html_file.write('<!DOCTYPE html>\n')
    html_file.write('<html lang="pt-br">\n')
    html_file.write('<head>\n')
    html_file.write('\t<title>Database</title>\n')
    html_file.write('\t<meta charset="utf-8">\n')
    html_file.write('\t<style>\n')
    html_file.write('\tbody { margin: 10px; }\n')
    html_file.write('\ttable, th, td, li, dl { font-family: "lucida grande",'
                    ' arial; font-size: 8pt; }\n')
    html_file.write('\tdt { font-weight: bold; }\n')
    html_file.write('\ttable { background-color: #efefef; border:'
                    '2px solid #dddddd; width: 100%; }\n')
    html_file.write('\tth { background-color: #efefef; }\n')
    html_file.write('\ttd { background-color: #ffffff; }\n')
    html_file.write('\t</style>\n')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    html_file.write('\n<table>\n')

    html_file.write('<tr>\n')
    for title in titles:
        html_file.write('\t<th>{}</th>\n'.format(title))
    html_file.write('</tr>\n')

    for reader in text:
        line = reader.split(',')
        html_file.write('<tr>\n')
        for coluna in range(5):
            html_file.write('\t<td>{}</td>\n'.format(line[coluna]))
        html_file.write('\t<td>{}</td>\n'.format(line[5].replace('\n', '')))
        html_file.write('</tr>\n')

    html_file.write('\n</table>\n')
    html_file.write('\n</body>\n')
    html_file.write('</html>')
