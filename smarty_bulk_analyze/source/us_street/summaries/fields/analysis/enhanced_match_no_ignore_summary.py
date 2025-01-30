class EnhancedMatchNoIgnoreSummary:
    def __init__(self):
        self.name = "Enhanced Match No Ignore Summary"
        self.display_name = "Enhanced Match Summary"
        self.count = {}
        self.dict = {
            "none":"No address match was found.",
            "non-postal-match":"A match was found within additional, non-postal address data.",
            "postal-match":"A match was found within postal address data.",
            "missing-secondary":"The address should have a secondary (e.g., apartment), but none was found in the input.",
            "unknown-secondary":"The provided secondary information did not match a known secondary within the address data.",
        }

        self.examples = {}

        self.final = {}
        self.csv_dict = {}

    def process_row(self, row):
        temp_string = row.get('[enhanced_match]')
        if temp_string == '':
            temp_string = 'none'
        if ',ignored-input' in temp_string:
            temp_string = temp_string.replace(',ignored-input', '')
        if temp_string in self.count:
            self.count[temp_string] += 1
        else:
            self.count[temp_string] = 1

    def create_final_dict(self, total):
        for item in self.count:
            if self.count[item] != 0:
                percentage = round(self.count[item] * 100 / total, 2)
                self.final[item] = str(self.count[item]) + " (" + str(percentage) + "%)"

    def create_csv_dict(self, total):
        for item in self.count:
            if self.count[item] != 0:
                percentage = round(self.count[item] * 100 / total, 2)
                self.csv_dict[item] = [str(self.count[item]), str(percentage) + "%"]