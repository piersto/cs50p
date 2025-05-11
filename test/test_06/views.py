import csv
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image


def main():
    with open("C:\PROJECTS\PYTHON\CX50P\/views.csv", "r", encoding='utf-8') as views,\
            open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        # reader in it has the fieldnames (as a list), so we can get them at this way
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = calculate_brightness(f"C:/PROJECTS/PYTHON/CX50P/{row['id']}.jpeg")
            row["brightness"] = round(row["brightness"], 2)
            writer.writerow(row)


def calculate_brightness(file_name):
    with Image.open(file_name) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness


main()
