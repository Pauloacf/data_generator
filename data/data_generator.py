"""
name_gen
"""
from random import randrange, uniform

# Módulos de criação de dados


def read_file(file):  # Lê arquivo e transforma em lista
    values = []
    for line in file:
        values.append(line.split())
    return values


def create_a_name(letters, gender):  # Seleciona um dos 260 nomes
    name = ''
    i = randrange(0, 52)
    if gender == 1:  # Para nomes femininos
        if ((i + 1) % 2 != 0):  # Verifica se o nome é feminino
            name = letters[i][randrange(0, 4)]
            return name
        else:  # Caso não seja...
            i -= 1
            name = letters[i][randrange(0, 4)]
            return name

    if gender == 2:  # Para nomes masculinos
        if ((i + 1) % 2 == 0):  # Verifica se o nome é masculino
            name = letters[i][randrange(0, 4)]
            return name
        else:  # Caso não seja...
            i += 1
            name = letters[i][randrange(0, 4)]
            return name


def create_a_surename(letters):  # Seleciona um dos 130 sobrenomes
    surename = ''
    surename = letters[randrange(52, 78)][randrange(0, 4)]
    return surename


def create_a_local():  # Cria uma casa e cep
    road_file = open('./data/roads.txt', 'r')
    road_parts = read_file(road_file)
    road_file.close
    road = 'Rua'
    cep = str(randrange(0, 10)) + (
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) + '-' +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)))
    type_of_road = (randrange(1, 91))  # cria o número que gera o nome da rua

    if (type_of_road <= 15):
        road += ' dos '
        road += ''.join(road_parts[randrange(0, 8)][randrange(0, 5)]) + (
            ' N-' + str(randrange(0, 1000)) + ', ' + cep)
        return road

    if (type_of_road <= 30):
        road += ' das '
        road += ''.join(road_parts[randrange(8, 16)][randrange(0, 5)]) + (
            ' N-' + str(randrange(0, 1000)) + ', ' + cep)
        return road

    if (type_of_road <= 45):
        road += ' dos '
        road += ''.join(road_parts[randrange(0, 4)][randrange(0, 5)]) + (
            ' ' + ''.join(road_parts[randrange(4, 8)][randrange(0, 5)]) + (
                ' N-') + (str(randrange(0, 1000)) + ', ' + cep))
        return road

    if (type_of_road <= 60):
        road += ' das '
        road += ''.join(road_parts[randrange(8, 13)][randrange(0, 5)]) + (
            ' ' + ''.join(road_parts[randrange(13, 16)][randrange(0, 5)]) + (
                ' N-') + (str(randrange(0, 1000)) + ', ' + cep))
        return road

    if (type_of_road <= 75):
        road += ' dos '
        road += ''.join(road_parts[randrange(0, 4)][randrange(0, 5)]) + (
            ' e ' + ''.join(road_parts[randrange(13, 16)][randrange(0, 5)]) + (
                ' N-') + (str(randrange(0, 1000)) + ', ' + cep))
        return road

    if (type_of_road <= 90):
        road += ' das '
        road += ''.join(road_parts[randrange(13, 16)][randrange(0, 5)]) + (
            ' e ' + ''.join(road_parts[randrange(0, 4)][randrange(0, 5)]) + (
                ' N-') + (str(randrange(0, 1000)) + ', ' + cep))
        return road


def create_DDD():  # Cria um número de celular e localização
    ddd_file = open('./data/ddd.txt', 'r')
    ddd_parts = read_file(ddd_file)
    ddd_file.close
    ddd = randrange(0, 89)

    phone_stt = '(0' + str(ddd+10) + ')'
    phone_stt += '9' + (  # Gera o número
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) +
        str(randrange(0, 10)) + ', ' +
        ' '.join(ddd_parts[ddd]))
    return phone_stt


def persona(data_number):  # Cria um txt das informações de cada indivíduo
    names_list = list()  # Lista que receberá os nomes
    f_data_gen = open('./data/generation.txt', 'r')  # Abrindo banco de nomes
    name_parts = read_file(f_data_gen)  # Passando as partes dos nomes
    f_data_gen.close()
    f_data_gen = open('names.txt', 'w')  # Abrindo o txt dos DB's
    i = 0
    number_of_data = data_number

    while i < int(number_of_data):
        cep_and_adress = create_a_local()
        phone_and_state = create_DDD()
        g = randrange(1, 3)  # gênero para filtro de nomes
        age = randrange(1, 101)  # idade entre 1 e 100
        number_type = randrange(1, 23)  # Número do tipo de nome
        i += 1

        if number_type < 11:  # Cria uma persona simples
            names_list.append(
                create_a_name(
                    name_parts, g) + ' ' + (create_a_surename(
                        name_parts)) + ' ' + (create_a_surename(
                            name_parts)) + ', ' + str(age) + ' anos, ' + (
                                (phone_and_state)) + ', ' + (
                                    cep_and_adress))

        elif number_type <= 20:  # Cria uma persona composta
            names_list.append(
                create_a_name(
                    name_parts, g) + ' ' + (create_a_name(
                        name_parts, g)) + ' ' + (create_a_surename(
                            name_parts)) + ' ' + (create_a_surename(
                                name_parts)) + ', ' + str(age) + ' anos, ' + (
                                    phone_and_state) + ', ' + (
                                        cep_and_adress))

        elif number_type == 21:  # Cria uma persona composta + von
            names_list.append(
                create_a_name(
                    name_parts, g) + ' ' + (create_a_name(
                        name_parts, g)) + ' ' + (create_a_surename(
                            name_parts)) + ' von ' + (create_a_surename(
                                name_parts)) + ', ' + str(age) + ' anos, ' + (
                                    phone_and_state) + ', ' + (
                                        cep_and_adress))

        elif number_type == 22:  # Cria uma persona composta + de
            names_list.append(
                create_a_name(
                    name_parts, g) + ' ' + (create_a_name(
                        name_parts, g)) + ' ' + (create_a_surename(
                            name_parts)) + ' de ' + (create_a_surename(
                                name_parts)) + ', ' + str(age) + ' anos, ' + (
                                    phone_and_state) + ', ' + (
                                        cep_and_adress))

    f_data_gen.write('\n'.join(names_list))
    f_data_gen.close()
