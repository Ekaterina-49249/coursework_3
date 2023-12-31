from datetime import datetime


class Operation:

    def __init__(self, date, description, from_op, to_op, amount, currency_name):
        """Инициализация класса Operation"""
        self.__date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        self.__amount = amount
        self.__description = description
        self.__from_op = from_op
        self.__to_op = to_op
        self.__currency_name = currency_name

    def __repr__(self):
        """Информация об объектах класса Operation"""
        return (
            f"Время-{self.__date},описание операции-{self.__description}\nОткуда{self.__from_op} -> куда {self.__to_op}\n"
            f"Сколько-{self.__amount}Денежная единица{self.__currency_name}")

    @staticmethod
    def __mask(str_imput: str):
        """Функция преобразования номеров счета и карты в нужный вид"""
        list1 = str_imput.split()
        number = list1[-1]
        name = " ".join(list1[:-1])
        if len(number) == 16:
            return f"{name} {number[0:4]} {number[4:6]}** **** {number[-4:]}"
        else:
            return f"Счет **{number[-4:]}"

    def get_from(self):
        """Метод возвращает откуда был сделан перевод(номер счета или карты при их наличии)"""
        if self.__from_op:
            return Operation.__mask(self.__from_op)
        return "Нет данных"

    def get_to(self):
        """Метод возвращает куда был сделан перевод(номер счета или карты)"""
        return Operation.__mask(self.__to_op)

    def get_date(self):
        """Метод возвращает дату перевода в нужном формате"""
        return self.__date.strftime("%d.%m.%Y")

    def get_amount_str(self):
        """Метод суммы перевода и валюты"""
        return f"{self.__amount} {self.__currency_name}"

    def get_description(self):
        """Метод описания опирации"""
        return self.__description

    def get_datetime(self):
        return self.__date
