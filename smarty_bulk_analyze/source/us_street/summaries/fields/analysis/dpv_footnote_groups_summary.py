class DPVFootnoteGroupsSummary:
    def __init__(self):
        self.name = 'DPV Footnote Groups Summary'
        self.display_name = 'DPV Footnote Summary'
        self.count = {}

        self.list = [
            "AA",
            "A1",
            "BB",
            "CC",
            "C1",
            "F1",
            "G1",
            "M1",
            "M3",
            "N1",
            "PB",
            "P1",
            "P3",
            "RR",
            "R1",
            "R7",
            "TA",
            "U1"
        ]

        self.dict = {
            "AA":"Street name, city, state, and ZIP are all valid.",
            "A1":"Address not present in USPS data.",
            "BB":"Entire address is valid.",
            "CC":"The submitted secondary information (apartment, suite, etc.) was not recognized. Secondary number is NOT REQUIRED for delivery.",
            "C1":"The submitted secondary information (apartment, suite, etc.) was not recognized. Secondary number IS REQUIRED for delivery.",
            "F1":"Military or diplomatic address",
            "G1":"General delivery address",
            "M1":"Primary number (e.g., house number) is missing.",
            "M3":"Primary number (e.g., house number) is invalid.",
            "N1":"Address is missing secondary information (apartment, suite, etc.) which IS REQUIRED for delivery.",
            "PB":"PO Box street style address.",
            "P1":"PO, RR, or HC box number is missing.",
            "P3":"PO, RR, or HC box number is invalid.",
            "RR":"Confirmed address with private mailbox (PMB) info.",
            "R1":"Confirmed address without private mailbox (PMB) info.",
            "R7":"Confirmed as a valid address that doesn't currently receive US Postal Service street delivery.",
            "TA":"Primary number was matched by dropping trailing alpha.",
            "U1":"Address has a unique ZIP Code."
        }

        self.examples = {}

        self.final = {}
        self.csv_dict = {}

    def process_row(self, row):
        temp_string = row.get('[dpv_footnotes]')
        if temp_string == "":
            temp_string = "blank"
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
                self.csv_dict[item] [str(self.count[item]), str(percentage) + "%"]

    # for item in self.list:
    #     self.examples.update({item: []})
