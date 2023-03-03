from utils import get_file, operations_file_edit
from utils.class_operation import Operation


def main():
    json_file = get_file.get_file()
    normal_file = get_file.get_json(json_file)

    normal_file = operations_file_edit.remove_empty_dict(normal_file)
    sorted_file = operations_file_edit.sort_file(normal_file)
    operations = operations_file_edit.get_five_executed_operations(sorted_file)

    for operation in operations:
        operation_output = Operation(*operations_file_edit.get_necessary_data(operation))
        date = operation_output.edit_date_format()
        num_from = operation_output.edit_number_from()
        num_to = operation_output.edit_number_to()

        operation_output.output_operation(date, num_from, num_to)


main()
