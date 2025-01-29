class AnalysisMiscSummary:
    def __init__(self):
        self.DPVCMRA = 0
        self.DPVVACANT = 0
        self.SUITELINK = 0

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

        for item in self.list:
            self.examples.update({item: []})