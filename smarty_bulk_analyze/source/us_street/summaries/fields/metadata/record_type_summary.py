class RecordTypeSummary:
    def __init__(self):
        self.AA = 0
        self.A1 = 0
        self.BB = 0
        self.CC = 0
        self.C1 = 0
        self.F1 = 0

        self.list = [
            "AA",
            "A1",
            "BB",
            "CC",
            "C1",
            "F1"
        ]

        self.dict = {
            "AA":"Street name, city, state, and ZIP are all valid.",
            "A1":"Address not present in USPS data.",
            "BB":"Entire address is valid.",
            "CC":"The submitted secondary information (apartment, suite, etc.) was not recognized. Secondary number is NOT REQUIRED for delivery.",
            "C1":"The submitted secondary information (apartment, suite, etc.) was not recognized. Secondary number IS REQUIRED for delivery.",
            "F1":"Military or diplomatic address"
        }

        self.examples = {}

        for item in self.list:
            self.examples.update({item: []})