from test_data_generation import generate_random_data
from app import App
from record_class import Record
filename = 'test_data.txt'      # Имя файла, из которого берутся данные

if __name__ == '__main__':
    """Если нужно добавить строки в тестовый файл, 
    раскоментируйте следующую строку и укажите количество строк в качестве аргумента метода: """
    # generate_random_data(1000)
    with open(filename, 'r') as f:   # Заполнение коллекции записями из файла
        records = []
        for line in f:     # Для каждой строки в файле
            try:
                # Считываем информацию:
                surname, name, patronymic, organization, work_phone, cell_phone = line.strip().split(sep=', ')
                # Создаем объект класса Record:
                record = Record(surname, name, patronymic, organization, work_phone, cell_phone)
                records.append(record)    # Запихиваем его в коллекцию
            except:    # Если строка невалидная, пропускаем
                pass
    app = App(records, 1)  # Создаем объект класса App
    app.app_loop()    # Запускаем программу
