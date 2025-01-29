class DPVMatchCodeSummary:
    def __init__(self):
        self.Y = 0
        self.N = 0
        self.S = 0
        self.D = 0

        self.list = [
            "Y",
            "N",
            "S",
            "D"
        ]

        self.dict = {
            "Y":"Confirmed; entire address is present in the USPS data.",
            "N":"Not confirmed; address is not present in the USPS data.",
            "S":"Confirmed, the main address is present in the USPS data, but the submitted secondary information (apartment, suite, etc.) was not recognized.",
            "D":"Confirmed, but missing secondary info"
        }

        self.examples = {}

        for item in self.list:
            self.examples.update({item: []})