import csv
from typing import Dict, List


def save_to_csv(data_list: List[Dict], filename: str):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data_list[0].keys()))

        writer.writeheader()  # Write CSV header
        writer.writerows(data_list)


def add_to_csv(data_list: List[Dict], filename: str):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data_list[0].keys()))
        writer.writerows(data_list)
