class PrecisionNotNoneSummary:
    def __init__(self):
        self.name = "Precision Not None Summary"
        self.count = {}
        self.total = 0

        self.examples = {}

        self.final = {}

    def process_row(self, row):
        if row.get('[precision]') in self.count and 'none' not in row.get('[enhanced_match]') and row.get('[enhanced_match]') != "":
            self.count[row.get('[precision]')] += 1
        elif 'none' not in row.get('[enhanced_match]') and row.get('[enhanced_match]') != "":
            self.count[row.get('[precision]')] = 1
        if 'none' not in row.get('[enhanced_match]') and row.get('[enhanced_match]') != "":
            self.total += 1
        
        

    def create_final_dict(self, total):
        for item in self.count:
            if self.count[item] != 0:
                percentage = round(self.count[item] * 100 / self.total, 2)
                self.final[item] = str(self.count[item]) + " (" + str(percentage) + "%)"