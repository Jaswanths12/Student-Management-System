import json
import csv
import os


class Storage:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save(self, students):
        with open(self.filename, "w") as file:
            json.dump(students, file, indent=4)

    def export_csv(self, students, csv_file="students.csv"):
        with open(csv_file, "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["roll", "name", "marks", "grade"]
            )
            writer.writeheader()
            writer.writerows(students)
