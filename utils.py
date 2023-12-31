#Импорт файла Json и класса Operation
import json
from operation import Operation


def load_executed_operations_from_file(file_name):
    """Функция загрузки файлов из файла"""

    with open(file_name, "r", encoding="utf-8") as file:
        operations_list = json.load(file)

    new_list = []
    for operation in operations_list:
        if operation and operation["state"] == "EXECUTED":
            new_list.append(Operation(operation["date"],
                                      operation["description"],
                                      operation.get("from", None),
                                      operation["to"],
                                      operation["operationAmount"]["amount"],
                                      operation["operationAmount"]["currency"]["name"]))

    return new_list


def sorted_operations(list_operation):
    """Функция сортировки списка"""
    return sorted(list_operation, key=lambda x: x.get_datetime(), reverse=True)
