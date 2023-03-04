from coursework3.utils.class_operation import Operation
import pytest


def test_edit_date_format():
    """Изменение даты"""
    test_data = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                          'Visa 1122334455667788')
    assert test_data.edit_date_format() == '26.08.2019'


def test_edit_number_from():
    """Изменение номера отправителя"""
    test_data = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                          'Visa 1122334455667788')
    test_data2 = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                          'Счет 11223344556677889900')
    test_data3 = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                           None)
    assert test_data.edit_number_from() == 'Visa 1122 33** **** 7788'
    assert test_data2.edit_number_from() == 'Счет **9900'
    assert test_data3.edit_number_from() == '****'


def test_edit_number_to():
    """Изменение номера получателя"""
    test_data = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                          'Visa 1122334455667788')
    assert test_data.edit_number_to() == 'Счет **9900'


def test_output_operation():
    """Проверка вывода информации на экран
    P.S. По сути, функция ничего не возвращает, так что все в порядке :)"""
    test_data = Operation('2019-08-26T10:50:58.294041', 'Перевод', 'Счет 11223344556677889900', '100', 'USD',
                          'Visa 1122334455667788')
    date = '26.08.2019'
    num_from = 'Visa 1122 33** **** 7788'
    num_to = 'Счет **9900'
    assert test_data.output_operation(date, num_from, num_to) == None



