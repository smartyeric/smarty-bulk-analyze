class EnhancedMatchSummary:
    def __init__(self):
        # self.none = 0
        # self.nonPostalMatch = 0
        # self.postalMatch = 0
        # self.missingSecondary = 0
        # self.unknownSecondary = 0
        # self.ignoredInput = 0

        self.list = [
            "none",
            "non-postal-match",
            "postal-match",
            "missing-secondary",
            "unknown-secondary",
            "ignored-input"
        ]

        self.name = "Enhanced Match Summary"
        self.display_name = "Enhanced Match Summary"

        self.count = {
            "none":0,
            "non-postal-match":0,
            "postal-match":0,
            "missing-secondary":0,
            "unknown-secondary":0,
            "ignored-input":0
        }

        self.dict = {
            "none":"No address match was found.",
            "non-postal-match":"A match was found within additional, non-postal address data.",
            "postal-match":"A match was found within postal address data.",
            "missing-secondary":"The address should have a secondary (e.g., apartment), but none was found in the input.",
            "unknown-secondary":"The provided secondary information did not match a known secondary within the address data.",
            "ignored-input":"The provided input contained information that was not used for a match."
        }

        self.examples = {}

        self.final = {}
        self.csv_dict = {}

        for item in self.list:
            self.examples.update({item: []})

    def process_row(self, row):
        for item in self.count:
            if item in row.get('[enhanced_match]'):
                if item == 'postal-match':
                    if "non-postal-match" not in row.get('[enhanced_match]'):
                        self.count[item] += 1
                else:
                    self.count[item] += 1

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