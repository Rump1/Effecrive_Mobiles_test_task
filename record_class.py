class Record:
    """
    Класс для хранения данных из записей

    Атрибуты
    --------

    surname : str
        Фамилия
    name: str
        Имя
    patronymic: str
        Отчество
    organization: str
        Название организации
    work_number: int
        Рабочий телефон
    cell_number: int
        Сотовый телефон

    Методы
    ------
    def as_list(self)
        Возвращает данные записи в виде списка

    def as_string(self):
        Возвращает данные записи в виде строки

    """
    def __init__(self, surname, name, patronymic, organization, work_number, cell_number):
        """
        Устанавливает необходимые атрибуты для объекта класса Record.

        Параметры
        ---------
        surname : str
            Фамилия
        name: str
            Имя
        patronymic: str
            Отчество
        organization: str
            Название организации
        work_number: int
            Рабочий телефон
        cell_number: int
            Сотовый телефон
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.organization = organization
        self.work_number = work_number
        self.cell_number = cell_number

    def as_list(self):
        """
        Возвращает данные записи в виде списка

        Возвращаемое значение
        ---------------------
        record_as_list: list
            Запись в виде списка атрибутов
        """
        record_as_list = [self.surname, self.name, self.patronymic, self.organization, self.work_number, self.cell_number]
        return record_as_list

    def as_string(self):
        """
        Возвращает данные записи в виде строки

        Возвращаемое значение
        ---------------------
        record_as_string: list
            Запись в виде строки атрибутов через запятую
        """
        record_as_string = ', '.join(self.as_list())
        return record_as_string
