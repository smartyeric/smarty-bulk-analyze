class DPVFootnoteSummary:
    def __init__(self):
        self.AA = 0
        self.A1 = 0
        self.BB = 0
        self.CC = 0
        self.C1 = 0
        self.F1 = 0
        self.G1 = 0
        self.M1 = 0
        self.M3 = 0
        self.N1 = 0
        self.PB = 0
        self.P1 = 0
        self.P3 = 0
        self.RR = 0
        self.R1 = 0
        self.R7 = 0
        self.TA = 0
        self.U1 = 0

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

        for item in self.list:
            self.examples.update({item: []})