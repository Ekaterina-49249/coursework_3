#Импорт функций загрузки и сортировки
from utils import load_executed_operations_from_file, sorted_operations


#присвоение значения переменной(json file)
executed_operations = load_executed_operations_from_file("data/users_operations.json")

# сортировка последних пяти операций
last_five_operations = sorted_operations(executed_operations)[-5:]

# цикл по каждой из 5 операций, вывод результата
for operation in last_five_operations:
    print(f"{operation.get_date()} {operation.get_description()}\n"
          f"{operation.get_from()} -> {operation.get_to()}\n"
          f"{operation.get_amount_str()}\n")
