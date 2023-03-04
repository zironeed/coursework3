class Operation:
    def __init__(self, date, description, card_to, amount, currency, card_from=None):
        self.date = date
        self.description = description
        self.card_from = card_from
        self.card_to = card_to
        self.amount = amount
        self.currency = currency

    def edit_date_format(self):
        """Изменяем формат времени"""
        date = self.date.split("T")[0]
        date = date.split('-')
        date = list(reversed(date))
        date = '.'.join(date)

        return date

    def edit_number_from(self):
        """Прячем номер счета отправителя и добавляем пробелы"""
        if self.card_from is None:
            num_from = "****"
            return num_from
        else:
            num_from = self.card_from.split()

            if len(num_from[1]) == 16:
                num_from[1] = num_from[1][:6] + ('*' * 6) + num_from[1][11:]
                num_from[1] = num_from[1][:4] + ' ' + num_from[1][4:8] + ' ' + num_from[1][8:12] + ' ' \
                            + num_from[1][13:]
            else:
                num_from[1] = '**' + num_from[1][16:]

            num_from = ' '.join(num_from)

            return num_from

    def edit_number_to(self):
        """Прячем номер счета получателя"""
        num_to = self.card_to.split()
        num_to[1] = '**' + num_to[1][16:]
        num_to = ' '.join(num_to)

        return num_to

    def output_operation(self, date, num_from, num_to):
        """Вывод информации об операции"""
        print(f"""{date} {self.description}
{num_from} -> {num_to}
{self.amount} {self.currency}\n""")
