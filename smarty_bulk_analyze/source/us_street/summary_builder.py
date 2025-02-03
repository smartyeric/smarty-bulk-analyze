import csv
import json

from smarty_bulk_analyze.source.us_street.summaries.matched_summary import MatchedSummary
from smarty_bulk_analyze.source.us_street.summaries.unmatched_summary import UnmatchedSummary
from smarty_bulk_analyze.source.us_street.summaries.input_summary import InputSummary

from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.footnote_summary import FootnoteSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.enhanced_match_summary import EnhancedMatchSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.enhanced_match_groups_summary import EnhancedMatchGroupsSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.enhanced_match_no_ignore_summary import EnhancedMatchNoIgnoreSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.dpv_match_code_summary import DPVMatchCodeSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.dpv_footnote_summary import DPVFootnoteSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.dpv_footnote_groups_summary import DPVFootnoteGroupsSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.analysis_misc_summary import AnalysisMiscSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.precision_not_none_summary import PrecisionNotNoneSummary

class SummaryBuilder:
    def __init__(self, parameters):
        self.input_summary = InputSummary()
        self.matched_summary = MatchedSummary()
        self.unmatched_summary = UnmatchedSummary()

        self.footnote_summary = FootnoteSummary()
        self.enhanced_match_summary = EnhancedMatchSummary()
        self.enhanced_match_groups_summary = EnhancedMatchGroupsSummary()
        self.enhanced_match_no_ignore_summary = EnhancedMatchNoIgnoreSummary()
        self.dpv_match_code_summary = DPVMatchCodeSummary()
        self.dpv_footnote_summary = DPVFootnoteSummary()
        self.dpv_footnote_groups_summary = DPVFootnoteGroupsSummary()
        self.analysis_misc_summary = AnalysisMiscSummary()
        self.precision_not_none_summary = PrecisionNotNoneSummary()

        self.summary_array = [
            self.footnote_summary,
            self.enhanced_match_summary,
            self.enhanced_match_groups_summary,
            self.precision_not_none_summary,
            self.enhanced_match_no_ignore_summary,
            self.dpv_footnote_summary,
            self.dpv_footnote_groups_summary,
            self.analysis_misc_summary
        ]

        if (parameters.config != None):
            temp_array = []
            for name in parameters.summaries['Summaries']:
                for summary in self.summary_array:
                    if summary.name == name:
                        temp_array.append(summary)
            self.summary_array = temp_array
        
    
    def process_row(self, row):
        for summary in self.summary_array:
            summary.process_row(row)

    def finalize_results(self, total):
        for summary in self.summary_array:
            summary.count = self.sort_dict(summary.count)
            summary.create_final_dict(total)
    
    def generate_csv(self, parameters, total):
        for summary in self.summary_array:
            summary.create_csv_dict(total)
        with open(parameters.output, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=parameters.output_delimiter)
            csvwriter.writerow("")
            for summary in self.summary_array:
                csvwriter.writerow([summary.display_name, "Count", "Percentage"])
                for row_name in self.sort_dict(summary.count):
                    csvwriter.writerow([row_name, summary.csv_dict[row_name][0], summary.csv_dict[row_name][1]])
                csvwriter.writerow("")

    def sort_dict(self, dictionary):
        return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))