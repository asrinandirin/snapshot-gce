import csv

def read_csv_and_generate_tf_variables(csv_file_path):
    variables = []

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            disk_config = {
                "name": row["name"],
                "project": row["project"],
                "zone": row["zone"]
            }
            variables.append(disk_config)

    return variables

def generate_tf_variables(variables):
    tf_code = 'variable "disk_configs" {\n'
    tf_code += '  type    = list(map(string))\n'
    tf_code += '  default = [\n'

    for disk_config in variables:
        tf_code += '    {\n'
        tf_code += f'      "name"    = "{disk_config["name"]}",\n'
        tf_code += f'      "project" = "{disk_config["project"]}",\n'
        tf_code += f'      "zone"    = "{disk_config["zone"]}",\n'
        tf_code += '    },\n'

    tf_code += '  ]\n'
    tf_code += '}\n'

    return tf_code

csv_file_path = "input.csv"

variables = read_csv_and_generate_tf_variables(csv_file_path)

tf_code = generate_tf_variables(variables)

print(tf_code)

with open("variables.tf", 'w') as tf_file:
    tf_file.write(tf_code)

