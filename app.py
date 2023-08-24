from math import ceil
from checking_the_string import Checkliner
from display import Display
from record_class import Record
from filter_class import Filter
filename = 'test_data.txt'
page_size = 10  # Количество строк, умещающихся в страницу


class App:
    """
    Основной класс программы. Обрабатывает команды пользователя,
    мониторит текущую страницу и редактирует содержимое списка records

    Атрибуты
    --------
    records: list[Record]
        список строк из файла с данными
    current_page: int
        текущая страница, которую видит пользователь
    is_worked: bool
        проверяет, запущена ли программа

    Методы
    ------
    def prev()
        Перемещает пользователя на предыдущую страницу
    def next(self):
        Перемещает пользователя на следующую страницу
    def page(self, page_number: int):
        Перемещает пользователя на страницу с номером page_number
    def new(self):
        Создает новую запись
    def edit(self, record_number: int):
        Редактирует запись с номером record_number
    def find(self)
        Поиск записей по введенным характеристикам
    def exit(self)
        Завершение работы программы
    def manual(self, first_time=False)
        Вывод инструкции
    def app_loop(self)
        Цикл обработки команд, введенных пользователем

    """
    def __init__(self, records: list[Record], current_page: int, is_worked: bool = True):
        """
        Устанавливает необходимые атрибуты для объекта Command_list.

        Параметры
        ---------
        records: list[Record]
            список строк из файла с данными
        current_page: int
            текущая страница, которую видит пользователь
        is_worked: bool
            проверяет, запущена ли программа
        """
        self.records = records
        self.current_page = current_page
        self.is_worked = is_worked

    def prev(self):
        """ Уменьшает current_page на единицу и печатает страницу """
        self.current_page -= 1
        Display.show_page(page_size, self.current_page, self.records)  # Печать страницы справочника
        number_of_pages = ceil(len(self.records) / page_size)  # Количество существующих страниц
        # Если текущая страница стала меньше минимума, возвращаем к нижней границе
        if self.current_page <= 0:
            self.current_page = 1

    def next(self):
        """ Увеличивает current_page на единицу и печатает страницу """
        self.current_page += 1
        Display.show_page(page_size, self.current_page, self.records)  # Печать страницы справочника
        number_of_pages = ceil(len(self.records) / page_size)  # Количество существующих страниц
        # Если текущая страница стала больше максимума, возвращаем к верхней границе
        if self.current_page > number_of_pages:
            self.current_page = number_of_pages

    def page(self, page_number: int):
        """
        Перемещает пользователя на страницу, которую он ввел

        Параметры
        ---------
        page_number: int
            Требуемая страница
        """
        self.current_page = page_number
        Display.show_page(page_size, self.current_page, self.records)  # Печать страницы справочника
        number_of_pages = ceil(len(self.records) / page_size)  # Количество существующих страниц
        # Если текущая страница стала больше максимума, возвращаем к верхней границе
        if self.current_page > number_of_pages:
            self.current_page = number_of_pages
        # Если текущая страница стала меньше минимума, возвращаем к нижней границе
        if self.current_page <= 0:
            self.current_page = 1

    def new(self):
        """ Создает новую запись, запрашивает у пользователя данные """
        Display.clear()
        Display.new_command_helper()    # Печатаем инструкцию по вводу новой записи
        correct_input = False
        while not correct_input:     # Пока пользователь не введет корректную строку
            new_line = input()
            if new_line == 'back':     # Если пользователь передумал что-то вводить
                correct_input = True      # Завершаем цикл
                Display.show_page(page_size, self.current_page, self.records)   # Показываем страницу справочника
            elif Checkliner.checking_the_record(new_line):   # Если запись корректна
                # Достаем данные из записи
                surname, name, patronymic, organization, work_phone, cell_phone = new_line.strip().split(sep=', ')
                # Создаем объект класса Record:
                record = Record(surname, name, patronymic, organization, work_phone, cell_phone)
                self.records.append(record)   # Добавляем ее в коллекцию
                with open(filename, 'a') as f:   # И в файл
                    f.write('\n' + new_line)
                correct_input = True    # Завершаем цикл
                Display.show_page(page_size, self.current_page, self.records,
                                  ender=f'Запись добавлена под номером {len(self.records)}')   # Показываем страницу справочника
            else:
                # Выводим уведомление, подсказку
                Display.clear()
                print('Введенная строка некорректна! Попробуйте еще раз:')
                Display.new_command_helper()

    def edit(self, record_number: int):
        """
        Редактирует запись, запрашивает у пользователя данные

        Параметры
        ---------

        record_number: int
            Номер редактируемой записи
        """
        Display.clear()
        if record_number > len(self.records) or record_number <= 0:     # Если некорректный номер записи
            Display.show_page(page_size, self.current_page, self.records,
                              ender="Записи с таким номером не существует! Попробуйте еще раз.")
        else:
            Display.edit_command_helper()   # Показываем справку о работе команды
            correct_input = False
            while not correct_input:    # Пока пользователь не введет корректную строку для замены:
                new_line = input()
                if new_line == 'back':  # Если пользователь передумал что-то вводить
                    correct_input = True  # Завершаем цикл
                    Display.show_page(page_size, self.current_page, self.records)  # Показываем страницу справочника
                elif Checkliner.checking_the_record(new_line):  # Если запись корректна
                    # Достаем данные из записи
                    surname, name, patronymic, organization, work_phone, cell_phone = new_line.strip().split(sep=', ')
                    # Создаем объект класса Record:
                    record = Record(surname, name, patronymic, organization, work_phone, cell_phone)
                    self.records[record_number-1] = record  # Заменяем запись в коллекции
                    with open(filename, 'w') as f:  # Переписываем файл
                        for record in self.records:
                            f.write(record.as_string() + '\n')
                    correct_input = True  # Завершаем цикл
                    Display.show_page(page_size, self.current_page, self.records,
                                      ender=f'Запись под номером {record_number} была изменена.')  # Показываем страницу справочника
                else:
                    # Выводим уведомление, подсказку
                    Display.clear()
                    print('Введенная строка некорректна! Попробуйте еще раз:')
                    Display.edit_command_helper()

    def find(self):
        """ Производит поиск записей с параметрами, введенными пользователем. """
        characteristic_dict = {'ФАМИЛИЯ': 'surname',
                               'ИМЯ': 'name',
                               'ОТЧЕСТВО': 'patronymic',
                               'ОРГАНИЗАЦИЯ': 'organization',
                               'СОТОВЫЙ': 'cell_number',
                               'РАБОЧИЙ': 'work_number'}
        Display.clear()
        Display.find_command_helper()   # Показываем инструкцию
        correct_input = False
        while not correct_input:    # Пока не будет введен корректный ввод
            search_template = input()
            if search_template == 'back':     # Если пользователь передумал что-то вводить
                correct_input = True      # Завершаем цикл
                Display.show_page(page_size, self.current_page, self.records)   # Показываем страницу справочника
            else:
                filters = search_template.strip().split(',')    # Разбиваем фильтры через запятую
                correct_filters = True
                for item in filters:    # Проверяем, все ли корректны
                    if not Checkliner.checking_find_command_template(item.strip()):
                        correct_filters = False
                if not correct_filters:
                    # Выводим уведомление, подсказку
                    Display.clear()
                    print('Введенная строка некорректна! Попробуйте еще раз:')
                    Display.find_command_helper()
                else:   # Если все в порядке
                    filter = Filter()   # Создаем объект Filter
                    for item in filters:     # Для каждого фильтра по характеристике
                        key, value = item.split('=')   # Достаем из равенства название характеристики и ее значение
                        key = key.strip().upper()
                        if key in characteristic_dict:     # Если характеристика есть в нашем словаре
                            setattr(filter, characteristic_dict[key], value.strip())    # Заполняем значение фильтра
                    filtered_records = []   # Список для хранения подходящих по фильтру записей
                    for i in range(len(self.records)):     # Пробегаем по всем записям и смотрим, проходят ли по фильтру
                        if filter.is_suitable_template(self.records[i]):    # Если да
                            filtered_records.append([i+1] + self.records[i].as_list())  # То добавляем в коллекцию
                    Display.show_find_results(filtered_records)     # Выводим результаты
                    correct_input = True    # Завершаем цикл
                    Display.show_page(page_size, self.current_page, self.records)   # Возвращаем на рабочую страницу

    def exit(self):
        """ Завершает работу программы, выводит соответсвтующее сообщение"""
        self.is_worked = False
        Display.clear()
        print("Программа завершена")

    def manual(self, first_time=False):
        """ Выводит мануал. Если эта функция вызывается из работающей программы, а не перед ее запуском,
        то после мануала возвращает на страницу справочника
        """
        Display.manual()
        if not first_time:
            Display.show_page(page_size, self.current_page, self.records)

    def app_loop(self):
        """
        Цикл программы, ждет ввода команд и реагирует на них
        """
        command_dict = {'prev': lambda: self.prev(),  # Список возможных команд
                        'next': lambda: self.next(),
                        'new': lambda: self.new(),
                        'exit': lambda: self.exit(),
                        'find': lambda: self.find(),
                        'manual': lambda: self.manual()}

        self.manual(True)  # Печать мануала
        Display.show_page(page_size, self.current_page, self.records)   # Печать страницы справочника
        while self.is_worked:   # Пока не вышли из программы
            correct_command = False
            while not correct_command:
                command = input().strip()  # Ждем ввода команды
                if Checkliner.checking_page_command(command):    # Если ввели page N
                    correct_command = True  # Завершаем цикл
                    page_number = int(command.split()[1])   # Вычленяем номер строки
                    self.page(page_number)
                elif Checkliner.checking_edit_command(command):
                    correct_command = True  # Завершаем цикл
                    page_number = int(command.split()[1])   # Вычленяем номер строки
                    self.edit(page_number)
                elif command in command_dict:  # Иначе, если команда присутствует в словаре
                    correct_command = True  # Завершаем цикл
                    command_dict[command]()  # Вызываем команду
                else:
                    # Если введена некорректная команда, обновляем страницу и выводим сообщение, пока не введут корректную
                    Display.show_page(page_size, self.current_page, self.records,
                                      ender='Введена неверная команда, попробуйте еще раз')
