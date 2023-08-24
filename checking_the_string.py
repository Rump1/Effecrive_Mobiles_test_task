import re


class Checkliner:
    """
    Класс, отвечающий за проверку строк по шаблонам. Состоит только из методов

    Методы
    ------
    def checking_the_record(line)
        Проверяет запись по шаблону
    def checking_page_command(line)
        Проверяет, соответствует ли ввод команде "page N"
    def checking_edit_command(line)
        Проверяет, соответствует ли ввод команде "edit N"
    def checking_find_command_template(line)
        Проверяет, соответствует ли шаблон для команды "find" нужному
    """
    @staticmethod
    def checking_the_record(line):
        """
        Проверяет строку по шаблону

        Параметры
        ---------
        line: string
            Входящая строка

        """
        pattern = r'[а-яА-Я]+, [а-яА-Я]+, [а-яА-Я]+, [а-яА-Яa-zA-Z]+, \d+, \d+$'
        return re.fullmatch(pattern, line)

    @staticmethod
    def checking_page_command(line):
        """
        Проверяет, соответствует ли ввод команде "page N"

        Параметры
        ---------
        line: string
            Входящая строка
        """
        pattern = r'page [-]?\d+$'
        return re.fullmatch(pattern, line)

    @staticmethod
    def checking_edit_command(line):
        """
            Проверяет, соответствует ли ввод команде "edit N"

            Параметры
            ---------
            line: string
                Входящая строка
        """
        pattern = r'edit [-]?\d+$'
        return re.fullmatch(pattern, line)

    @staticmethod
    def checking_find_command_template(line):
        """
            Проверяет, соответствует ли шаблон для команды "find" нужному

            Параметры
            ---------
            line: string
                Входящая строка
        """
        pattern = r'[а-яА-Я]+=\w+'
        return re.fullmatch(pattern, line)

