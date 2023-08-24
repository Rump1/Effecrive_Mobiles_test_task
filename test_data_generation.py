import random

def generate_random_number(n):
    ''' Генерация случайного числа порядка n '''
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def generate_random_data(number_of_rows: 'Количество строк, которое необходимо сгенерировать'):
    ''' Создание файла с тестовыми данными '''
    with open('test_data.txt', 'a') as file:
        for i in range(number_of_rows): # Здесь выбирается размер файла, количество записей
            file.write(f'{random.choice(surname_man_list)}, {random.choice(name_man_list)}, {random.choice(fathername_man_list)}, '
                       f'{random.choice(organization_list)}, 2{generate_random_number(4)}, 89{generate_random_number(9)}\n')
            file.write(f'{random.choice(surname_woman_list)}, {random.choice(name_woman_list)}, {random.choice(fathername_woman_list)}, '
                       f'{random.choice(organization_list)}, 2{generate_random_number(4)}, 89{generate_random_number(9)}\n')



    # Коллекции со строками для генерации тестов:
surname_man_list = ['Тихонов', 'Андреев', 'Потапов',
                    'Носков', 'Попов', 'Озеров', 'Кожевников']

surname_woman_list = ['Давыдова', 'Хохлова', 'Власова',
                      'Иванова', 'Соколова', 'Новикова']

name_man_list = ['Андрей', 'Антон', 'Вадим', 'Михаил',
                 'Евгений', 'Марк', 'Юрий', 'Роман']

name_woman_list = ['Мария', 'Елизавета', 'Анастасия', 'Светлана',
                   'Арина', 'София', 'Полина', 'Надежда', ]

fathername_man_list = ['Иванович', 'Сергеевич', 'Михайлович', 'Евгеньевич',
                       'Петрович', 'Кириллович', 'Всеволодович', 'Ильич', 'Ярославович']

fathername_woman_list = ['Ивановна', 'Сергеевна', 'Михайловна', 'Евгеньевна',
                         'Петровна', 'Кирилловна', 'Ильинична', 'Ярославовна']

organization_list = ['Яндекс', 'Сбербанк', 'Озон', 'ВТБ', 'Тинькофф', 'Mail', 'VK', 'IBS']

