class FootnoteSummary:
    def __init__(self):
        # self.A = 0
        # self.B = 0
        # self.C = 0
        # self.D = 0
        # self.E = 0
        # self.F = 0
        # self.G = 0
        # self.H = 0
        # self.I = 0
        # self.J = 0
        # self.K = 0
        # self.L = 0
        # self.LL = 0
        # self.LI = 0
        # self.M = 0
        # self.N = 0
        # self.O = 0
        # self.P = 0
        # self.Q = 0
        # self.R = 0
        # self.S = 0
        # self.T = 0
        # self.U = 0
        # self.V = 0
        # self.W = 0
        # self.X = 0
        # self.Y = 0
        # self.Z = 0

        self.name = "Footnote Summary"
        self.display_name = "Footnote Summary"

        self.list = [
            "A#",
            "B#",
            "C#",
            "D#",
            "E#",
            "F#",
            "G#",
            "H#",
            "I#",
            "J#",
            "K#",
            "L#",
            "LL#",
            "LI#",
            "M#",
            "N#",
            "O#",
            "P#",
            "Q#",
            "R#",
            "S#",
            "T#",
            "U#",
            "V#",
            "W#",
            "X#",
            "Y#",
            "Z#",
        ]

        self.count = {
            "A#":0,
            "B#":0,
            "C#":0,
            "D#":0,
            "E#":0,
            "F#":0,
            "G#":0,
            "H#":0,
            "I#":0,
            "J#":0,
            "K#":0,
            "L#":0,
            "LL#":0,
            "LI#":0,
            "M#":0,
            "N#":0,
            "O#":0,
            "P#":0,
            "Q#":0,
            "R#":0,
            "S#":0,
            "T#":0,
            "U#":0,
            "V#":0,
            "W#":0,
            "X#":0,
            "Y#":0,
            "Z#":0
        }

        self.dict = {
            "A#":"Corrected ZIP Code",
            "B#":"Corrected city/state spelling",
            "C#":"Invalid city/state/ZIP",
            "D#":"No ZIP+4 assigned",
            "E#":"Same ZIP for multiple",
            "F#":"Address not found",
            "G#":"Used addressee data",
            "H#":"Missing secondary number",
            "I#":"Insufficient/ incorrect address data",
            "J#":"Dual address",
            "K#":"Cardinal rule match",
            "L#":"Changed address component",
            "LL#":"Flagged address for LACSLink",
            "LI#":"Flagged address for LACSLink",
            "M#":"Corrected street spelling",
            "N#":"Fixed abbreviations",
            "O#":"Multiple ZIP+4; lowest used",
            "P#":"Better address exists",
            "Q#":"Unique ZIP match",
            "R#":"No match; EWS: Match soon",
            "S#":"Unrecognized secondary address",
            "T#":"Multiple response due to magnet street syndrome",
            "U#":"Unofficial city name",
            "V#":"Unverifiable city/state",
            "W#":"Invalid delivery address",
            "X#":"Default Unique ZIP Code",
            "Y#":"Military match",
            "Z#":"Matched with ZIPMOVE"
        }

        self.examples = {}

        self.final = {}
        self.csv_dict = {}

        for item in self.list:
            self.examples.update({item: []})

    def process_row(self, row):
        for item in self.count:
            if item in row.get('[footnotes]'):
                if item == 'L#':
                    if 'LL#' not in row.get('[footnotes]'):
                        self.count[item] += 1
                elif item == 'I#':
                    if 'LI#' not in row.get('[footnotes]'):
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