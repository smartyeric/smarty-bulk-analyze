class EnhancedMatchGroupsSummary:
    def __init__(self):
        self.name = "Enhanced Match Groups Summary"
        self.count = {}
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

    def process_row(self, row):
        if row.get('[enhanced_match]') in self.count:
            self.count[row.get('[enhanced_match]')] += 1
        else:
            self.count[row.get('[enhanced_match]')] = 1

    def create_final_dict(self, total):
        for item in self.count:
            if self.count[item] != 0:
                percentage = round(self.count[item] * 100 / total, 2)
                self.final[item] = str(self.count[item]) + " (" + str(percentage) + "%)"
    
