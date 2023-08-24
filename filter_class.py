class Filter:
    """
    Класс, предназначенный фильтрации записей

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
    ______
    def filter(self, record)
        Проверяет, соответствует ли record фильтру
    """
    def __init__(self, surname='', name='', patronymic='', organization='', work_number='', cell_number=''):
        """
        Устанавливает необходимые атрибуты для объекта класса Filter.

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

    def is_suitable_template(self, record):
        """
        Проверяет, соответсвует ли record фильтру по всем ненулевым атрибутам объекта Filter

        Параметры
        ---------

        record: Record
            Запись из справочника

        Возвращаемое значение
        ---------------------
        result: bool
            Соответствует ли запись фильтру
        """
        result = True
        for key in self.__dict__:
            if self.__dict__[key] != '' and self.__dict__[key] != record.__dict__[key]:
                result = False
        return result
