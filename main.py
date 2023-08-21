from utils import load_executed_operations_from_file, sorted_operations

executed_operations = load_executed_operations_from_file("data/users_operations.json")

last_five_operations = sorted_operations(executed_operations)[-5:]

for operation in last_five_operations:
    print(f"{operation.get_date()} {operation.get_description()}\n"
          f"{operation.get_from()} -> {operation.get_to()}\n"
          f"{operation.get_amount_str()}\n")


