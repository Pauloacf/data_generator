import json


def generate_json():
    json_file = open('./JSON/data.json', 'w')
    data_file = open('names.txt', 'r')
    text = data_file.readlines()
    json_file.write('[  \n')
    count = 0
    for r in text:
        json_file.write('\n   {   \n')
        line = r.split(',')
        json_file.write('\n        "Nome": "{}",\n'.format(str(line[0])))
        json_file.write('\n        "Idade": "{}",\n'.format(str(line[1])))
        json_file.write('\n        "Telefone": "{}",\n'.format(str(line[2])))
        json_file.write('\n        "UF": "{}",\n'.format(str(line[3])))
        json_file.write('\n        "Rua": "{}",\n'.format(str(line[4])))
        json_file.write('\n        "CEP": "{}"'.format(str(line[5]).rstrip()))

        if (count == (len(text)-1)):
            json_file.write('\n   }  \n')
        else:
            json_file.write('\n   },  \n')
        count += 1
    json_file.write('\n]\n')
    json_file.close()
    data_file.close()
