import datetime


def remove_empty_dict(file):
    """Удаление пустых словарей"""
    file.remove({})

    return file


def sort_file(file):
    """Сортировка операций по дате и времени"""
    for operation in file:
        operation['date'] = operation['date'].split('.')[0]

    sort = sorted(
        file,
        key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S'), reverse=True
    )

    return sort


def get_five_executed_operations(file):
    """Берем из файла 5 первых операций"""
    five_operations = []

    for operation in file:
        if len(five_operations) < 5:
            if operation['state'] == 'EXECUTED':
                five_operations.append(operation)

    return five_operations


def get_necessary_data(operation):
    """Отсеиваем лишнюю для отображения информацию"""
    if 'from' in operation:
        data = operation['date'], operation['description'], operation['to'], operation['operationAmount']['amount'], \
            operation['operationAmount']['currency']['name'], operation['from']
    else:
        data = operation['date'], operation['description'], operation['to'], operation['operationAmount']['amount'], \
            operation['operationAmount']['currency']['name']

    return list(data)
