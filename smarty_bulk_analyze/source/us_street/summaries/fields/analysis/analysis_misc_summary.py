class AnalysisMiscSummary:
    def __init__(self):
        self.name = "Analysis Miscellaneous Summary"
        self.display_name = "Analysis Miscellaneous Summary"
        
        self.count = {}

        self.list = [
            "dpv_cmra",
            "dpv_vacant",
            "suitelink_match"
        ]

        self.dict = {
            "dpv_cmra":"Indicates whether the address is associated with a Commercial Mail Receiving Agency",
            "dpv_vacant":"Indicates that a delivery point was active in the past but is currently vacant",
            "suitelink_match":"Indicates a match (or not) to the USPS SuiteLink data"
        }

        self.examples = {}

        self.final = {}
        self.csv_dict = {}
    
    def process_row(self, row):
        for column_name in self.list:
            temp_string = row.get("[" + column_name + "]")
            if temp_string == "":
                temp_string == "N"
            if temp_string in self.count:
                self.count[column_name] += 1
            else:
                self.count[column_name] =1

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

        # for item in self.list:
        #     self.examples.update({item: []})