import pytest
from coursework3.utils.operations_file_edit import *


@pytest.fixture
def operations():
    return [{'date': '2018-09-30T12:00:00.123', 'state': 'EXECUTED'},
            {'date': '2019-09-20T12:00:00.123', 'state': 'EXECUTED'},
            {'date': '2018-04-30T12:00:00.123', 'state': 'EXECUTED'},
            {'date': '2018-09-30T12:30:00.123', 'state': 'EXECUTED'},
            {'date': '2018-09-30T12:00:00.123', 'state': 'EXECUTED'},
            {'date': '2018-09-30T13:00:00.123', 'state': 'CANCELED'}]


def test_remove_empty_dict():
    """Удаление пустого словаря"""
    assert remove_empty_dict([{}]) == []


def test_sort_file(operations):
    """Сортировка данных по дате"""
    assert sort_file(operations) == [{'date': '2019-09-20T12:00:00', 'state': 'EXECUTED'},
                                     {'date': '2018-09-30T13:00:00', 'state': 'CANCELED'},
                                     {'date': '2018-09-30T12:30:00', 'state': 'EXECUTED'},
                                     {'date': '2018-09-30T12:00:00', 'state': 'EXECUTED'},
                                     {'date': '2018-09-30T12:00:00', 'state': 'EXECUTED'},
                                     {'date': '2018-04-30T12:00:00', 'state': 'EXECUTED'}]


def test_get_five_executed_operations(operations):
    """Берем пять выполненных операций"""
    assert get_five_executed_operations(operations) == [{'date': '2018-09-30T12:00:00.123', 'state': 'EXECUTED'},
                                                        {'date': '2019-09-20T12:00:00.123', 'state': 'EXECUTED'},
                                                        {'date': '2018-04-30T12:00:00.123', 'state': 'EXECUTED'},
                                                        {'date': '2018-09-30T12:30:00.123', 'state': 'EXECUTED'},
                                                        {'date': '2018-09-30T12:00:00.123', 'state': 'EXECUTED'}]


def test_get_necessary_data():
    """Отсеивание ненужной информации, преобразование в список"""
    """Если в словаре есть 'from'"""
    assert get_necessary_data({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                'to': 'Счет 64686473678894779589'}) == \
           ['2019-08-26T10:50:58.294041', 'Перевод организации', 'Счет 64686473678894779589', '31957.58', 'руб.',
            'Maestro 1596837868705199']

    """Если 'from' отсутствует"""
    assert get_necessary_data({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                                'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                                'description': 'Перевод организации', 'to': 'Счет 35383033474447895560'}) == \
           ['2019-07-03T18:35:29.512364', 'Перевод организации', 'Счет 35383033474447895560', '8221.37', 'USD']
