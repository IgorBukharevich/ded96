import ast
from datetime import datetime

from app.models import DataJson


def check_data(data):
    # Отлавливаем исключения
    try:
        # преобразование данных для обработки
        data = data.decode('utf-8')
        data = ast.literal_eval(data)
    except:
        return False
    return check_json(data)


def check_datetime(date) -> bool:
    """
    Проверка валидности даты в json-файле
    :param date: строка в формате - '2012-06-11_12:00'
    :return: True or False
    """
    # формат даты которую провремяем ключ("data")
    format_date = '%Y-%m-%d_%H:%M'
    try:
        datetime.strptime(date, format_date)
    except:
        return False
    return True


def check_json(data) -> bool:
    """
    Обработка данных из JSON-файла, для добавления в базу PostgreSQL
    :param data: даннные которые пришли из json-файла
    :return: True или False
    """
    key_n = 'name'
    key_d = 'date'

    for val in range(len(data)):
        # получение словаря из списка
        data_dict = data[val]

        # проверка валидности данных
        # ключ/значение, фильтрация нужных данных
        if (key_n in data_dict and key_d in data_dict) and (
                len(data_dict[key_n]) <= 50) and (
                check_datetime(data_dict[key_d])
        ):

            name_str = data_dict[key_n]
            date_str = data_dict[key_d].replace('_', ' ')
            # проверка данных ключа
            # key_n = 'name' и key_d = 'date' (есть ли там данные)
            if name_str and date_str != '':
                add_data = DataJson(name=name_str, date=date_str)
                add_data.save()
            else:
                return False
        else:
            return False
    return True
