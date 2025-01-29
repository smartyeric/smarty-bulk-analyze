import json

class JsonBuilder:
    def __init__(self):
        self.json_dict = {}
        self.indent = 4

    def process_summary(self, summary_builder):
        for summary in summary_builder.summary_array:
            self.json_dict.update({summary.name: summary.final})

    def print_json(self):
        print(json.dumps(self.json_dict, indent=self.indent))