# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    a = []
    with open(INPUT_FILENAME) as input_f:
        csv_file = csv.DictReader(input_f)
        for row in csv_file:
            a.append(dict(row))
    with open(OUTPUT_FILENAME,'w') as output_f:
        output_f = (json.dumps(a, indent=4))
        print(output_f)








if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
