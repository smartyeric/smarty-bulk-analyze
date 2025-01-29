import sys
import json
import getopt

class Parameters:
    def __init__(self, input):
        self.state = 'All'
        self.input = input
        self.output = 'none'
        self.examples = 2
        self.descriptions = False
        self.config = None
        self.summaries = None

    def set_parameters(self, system):
        options, remainder = getopt.getopt(system, 'i:s:o:e:d:c:', ['input=', 'state=', 'output=', 'examples=', 'descriptions', 'config='])
        for opt, arg in options:
            if (opt in ('-i', '--input')):
                self.input = arg
            if (opt in ('-s', '--state')):
                self.state = arg
            if (opt in ('-o', '--output')):
                self.output = arg
            if (opt in ('-e', '--examples')):
                self.examples = arg
            if (opt in ('-d', '--descriptions')):
                self.descriptions = True
            if (opt in ('-c', '--config')):
                self.config = arg

        if self.config != None:
            with open(self.config) as json_data:
                self.summaries = json.load(json_data)
                json_data.close()
                
