from utils import get_file, operations_file_edit
from utils.class_operation import Operation


def main():
    url = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-' \
          '4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=167794' \
          '5092922&signature=3gWPqGHgEIsuti5gO-etOZlRFb6eyrHEIMashdLP3ko&downloadName=operations.json'
    json_file = get_file.get_file(url)
    normal_file = get_file.get_json(json_file)

    normal_file = operations_file_edit.remove_empty_dict(normal_file)
    sorted_file = operations_file_edit.sort_file(normal_file)
    operations = operations_file_edit.get_five_executed_operations(sorted_file)

    for operation in operations:
        print(operations_file_edit.get_necessary_data(operation))
        operation_output = Operation(*operations_file_edit.get_necessary_data(operation))
        date = operation_output.edit_date_format()
        num_from = operation_output.edit_number_from()
        num_to = operation_output.edit_number_to()

        operation_output.output_operation(date, num_from, num_to)


main()
