# This is the main file for running the bulk output analysis tool

import csv
import sys
import json
import getopt
from smarty_bulk_analyze.source.us_street.parameters import Parameters
from smarty_bulk_analyze.source.us_street.csv_reader import CsvReader
from smarty_bulk_analyze.source.us_street.summary_builder import SummaryBuilder
from smarty_bulk_analyze.source.us_street.json_builder import JsonBuilder

def main():

    parameters = Parameters(sys.argv[1])
    parameters.set_parameters(sys.argv[1:])

    reader = CsvReader(parameters)
    records = reader.create_records()

    summary = SummaryBuilder(parameters)

    for row in records:
        summary.process_row(row)

    summary.finalize_results(reader.row_count)

    json_builder = JsonBuilder()
    json_builder.process_summary(summary)
    json_builder.print_json()

if __name__ == "__main__":
    main()
