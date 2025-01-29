from smarty_bulk_analyze.source.us_street.summaries.matched_summary import MatchedSummary
from smarty_bulk_analyze.source.us_street.summaries.unmatched_summary import UnmatchedSummary
from smarty_bulk_analyze.source.us_street.summaries.input_summary import InputSummary

from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.footnote_summary import FootnoteSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.enhanced_match_summary import EnhancedMatchSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.enhanced_match_groups_summary import EnhancedMatchGroupsSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.dpv_match_code_summary import DPVMatchCodeSummary
from smarty_bulk_analyze.source.us_street.summaries.fields.analysis.dpv_footnote_summary import DPVFootnoteSummary
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
        self.dpv_match_code_summary = DPVMatchCodeSummary()
        self.dpv_footnote_summary = DPVFootnoteSummary()
        self.analysis_mist_summary = AnalysisMiscSummary()
        self.precision_not_none_summary = PrecisionNotNoneSummary()

        self.summary_array = [
            self.footnote_summary,
            self.enhanced_match_summary,
            self.enhanced_match_groups_summary,
            self.precision_not_none_summary
        ]

        if (parameters.config != None):
            temp_array = []
            for summary in self.summary_array:
                if summary.name in parameters.summaries['Summaries']:
                    temp_array.append(summary)
            self.summary_array = temp_array
        
    
    def process_row(self, row):
        for summary in self.summary_array:
            summary.process_row(row)

    def finalize_results(self, total):
        for summary in self.summary_array:
            summary.create_final_dict(total)
    
