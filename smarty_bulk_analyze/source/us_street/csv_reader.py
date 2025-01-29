from smarty_bulk_analyze.source.us_street.dictionaries.states import States
from smarty_bulk_analyze.source.us_street.parameters import Parameters
import csv

class CsvReader():
    def __init__(self, parameters):
        self.file_path = parameters.input
        self.stateArg = parameters.state
        self.row_count = None

    def create_records(self):
        records = []
        states = States()
        file_path = self.file_path
        stateArg = self.stateArg
        delimiter = self.detect_delimiter()
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            reader.fieldnames = [field.strip().lower() for field in reader.fieldnames]
            if (stateArg in states.state_abbreviations):
                for row in reader:
                    if (stateArg == row.get('state') or states.abbreviation_to_name[stateArg] == row.get('state') or stateArg == row.get('[state_abbreviation]')):
                        records.append(row)
            if (stateArg == 'All' or (stateArg not in states.state_abbreviations)):
                for row in reader:
                    records.append(row)
        self.row_count = row_count = sum(1 for row in records)
        return records
    
    def detect_delimiter(self):
        delimiters = [',', '|', '\t']
        delimiter_counts = {delimiter: 0 for delimiter in delimiters}

        with open(self.file_path, newline='') as csvfile:
            for i, line in enumerate(csvfile):
                if i >= 10:  # Read only the first ten lines
                    break
                for delimiter in delimiters:
                    delimiter_counts[delimiter] += line.count(delimiter)

        # Choose the delimiter with the highest count
        detected_delimiter = max(delimiter_counts, key=delimiter_counts.get)
        return detected_delimiter