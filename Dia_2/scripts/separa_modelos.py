#!/usr/bin/env python3
# Scripts para separar los modelos con el fin de poder usar el codigo principal "prog3.1.py"

import os

input_file = "data/foldmason.pdb"
output_dir = "data"

with open(input_file, "r") as f:
    lines = f.readlines()

model_data = []
model_name = None

for line in lines:
    if line.startswith("MODEL"):
        model_data = []
        model_name = None

    elif line.startswith("REMARK") and "Name:" in line:
        # Extrae el nombre real del modelo
        model_name = line.split("Name:")[1].strip()

    elif line.startswith("ENDMDL"):
        if model_name is None:
            model_name = "modelo_desconocido"

        filename = os.path.join(output_dir, f"{model_name}.pdb")

        with open(filename, "w") as out:
            out.writelines(model_data)
            out.write("TER\n")

        print(f"Escrito: {filename}")

    else:
        model_data.append(line)
