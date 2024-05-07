import csv
import sys
import json
import getopt

stateArg = 'All'
inputFile = sys.argv[1]
outputFile = 'none'
options, remainder = getopt.getopt(sys.argv[1:], 'i:s:o:', ['input=', 'state=', 'output='])
for opt, arg in options:
    if (opt in ('-i', '--input')):
        inputFile = arg
    if (opt in ('-s', '--state')):
        stateArg = arg
    if (opt in ('-o', '--output')):
        outputFile = arg

states = [
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY", "DC", "AS", "GU", "MP", "PR", "VI"
]
abbreviation_to_name = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
    "DC": "District of Columbia",
    "AS": "American Samoa",
    "GU": "Guam GU",
    "MP": "Northern Mariana Islands",
    "PR": "Puerto Rico PR",
    "VI": "U.S. Virgin Islands"
}

def detect_delimiter(file_path):
    delimiters = [',', '|', '\t']
    delimiter_counts = {delimiter: 0 for delimiter in delimiters}

    with open(file_path, newline='') as csvfile:
        for i, line in enumerate(csvfile):
            if i >= 10:  # Read only the first ten lines
                break
            for delimiter in delimiters:
                delimiter_counts[delimiter] += line.count(delimiter)

    # Choose the delimiter with the highest count
    detected_delimiter = max(delimiter_counts, key=delimiter_counts.get)
    return detected_delimiter

def read_csv_file(file_path, delimiter=','):
    records = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        reader.fieldnames = [field.strip().lower() for field in reader.fieldnames]
        #if (len(sys.argv) - 1 == 2):
        #    stateArg = sys.argv[2]
        #else:
        #    stateArg = 'All'
        if (stateArg in states):
            for row in reader:
                if (stateArg == row.get('state') or abbreviation_to_name[stateArg] == row.get('state') or stateArg == row.get('[state_abbreviation]')):
                    records.append(row)
        if (stateArg == 'All' or (stateArg not in states)):
            for row in reader:
                records.append(row)
    return records

def count_records(records):
    summary_counts = {}
    summary_examples = {}
    for row in records:
        summary_value = row.get('[summary]')
        if summary_value in summary_counts:
            if (summary_counts[summary_value] == 1):
                summary_examples[summary_value + '2'] = generate_example(row)
            summary_counts[summary_value] += 1
        else:
            summary_counts[summary_value] = 1
            summary_examples[summary_value] = generate_example(row)
    return summary_counts, summary_examples

def generate_input_summary(records):
    inputSum = {}
    recordCount = len(records)
    freeformCount = 0
    componentsCount = 0
    for row in records:
        if (str(row.get('city')) == '' and str(row.get('state')) == '' and (str(row.get('zip')) == '' or str(row.get('zipcode')) == '')):
            freeformCount += 1
        else:
            componentsCount += 1
    inputSum['Total Records Input'] = recordCount
    inputSum['Freeform Records'] = freeformCount
    inputSum['Components Records'] = componentsCount
    return inputSum

def add_examples(inputArray, recordCount):
    finalDict = {}
    tempDict = {}
    exampleDict = {}
    inputCounts = inputArray[0]
    inputExamples = inputArray[1]
    for summary_value, count in inputCounts.items():
        if (isinstance(count, dict)):
            for key in count:
                percentage = round((count[key] / recordCount) * 100)
                tempDict[key] = f"{count[key]}/{recordCount} ({percentage}%)"
                if (key in inputExamples):
                    exampleDict['Example 1'] = f"{inputExamples[key]}"
                if (key + '2' in inputExamples):
                    exampleDict['Example 2'] = f"{inputExamples[key + '2']}"
                tempDict [key + ' Examples'] = exampleDict.copy()
            finalDict[summary_value] = tempDict
            tempDict = {}
        else:
            percentage = round((count / recordCount) * 100)
            finalDict[summary_value] = f"{count}/{recordCount} ({percentage}%)"
            if (summary_value in inputExamples):
                exampleDict['Example 1'] = f"{inputExamples[summary_value]}"
            if (summary_value + '2' in inputExamples):
                exampleDict['Example 2'] = f"{inputExamples[summary_value + '2']}"
            finalDict [summary_value + ' Examples'] = exampleDict.copy()
    return finalDict

def generate_unmatched_summary(records):
    unmatchedSum = {}
    exampleDict = {}
    dpvFootnotesValue = ''
    summaryValue = ''
    unmatchedDict = {
        'M1': 0,
        'M3': 0,
        'P1': 0,
        'P3': 0,
        'A1': 0
    }
    descriptionDict = {
        'M1': 'House Number Missing',
        'M3': 'House Number Not Matched',
        'P1': 'PO Box Number Missing',
        'P3': 'PO Box Number Not Matched',
        'A1': 'No Match Found'
    }
    POBoxOnlyCount = 0
    for row in records:
        dpvFootnotesValue = row.get('[dpv_footnotes]')
        for item in unmatchedDict:
            if (item in dpvFootnotesValue):
                if descriptionDict[item] in unmatchedSum:
                    if (unmatchedSum[descriptionDict[item]] == 1):
                        exampleDict[descriptionDict[item] + '2'] = generate_example(row)
                    unmatchedSum[descriptionDict[item]] += 1
                else:
                    unmatchedSum[descriptionDict[item]] = 1
                    exampleDict[descriptionDict[item]] = generate_example(row)
        summaryValue = row.get('[summary]')
        if (summaryValue == 'No Match - PO Box Only'):
            if ('No Match - PO Box Only' in unmatchedSum):
                if (unmatchedSum['No Match - PO Box Only'] == 1):
                    exampleDict['No Match - PO Box Only' + '2'] = generate_example(row)
                    unmatchedSum['No Match - PO Box Only'] += 1
            else:
                unmatchedSum['No Match - PO Box Only'] = 1
                exampleDict['No Match - PO Box Only'] = generate_example(row)
    return unmatchedSum, exampleDict
    
def generate_matched_summary(records):
    matchedSum = {}
    exampleDict = {}
    delList = []
    dpvFootnotesValue = ''
    enhancedMatchValue = ''
    zipTypeValue = ''
    rdiValue = ''
    lacsLinkValue = ''
    dpvVacantValue = ''
    recordTypeValue = ''
    dpvFootnotesDict = {
        'F1': 0,
        'G1': 0,
        'PB': 0,
        'RR': 0,
        'R1': 0,
        'R7': 0,
        'U1': 0
    }
    dpvFootnotesDescriptionDict = {
        'F1': 'Military or Diplomatic Address',
        'G1': 'General Delivery Address',
        'PB': 'PO Box Street Style Address',
        'RR': 'CMRA With Private Mailbox (PMB) Info',
        'R1': 'CMRA Without Private Mailbox (PMB) Info',
        'R7': 'Valid Address That Doesn\'t Currently Receive US Postal Service Street Delivery',
        'U1': 'Unique ZIP Code'
    }
    enhancedMatchDict = {
        'missing-secondary': 0,
        'unknown-secondary': 0,
        'ignored-input': 0
    }
    enhancedMatchDescriptionDict = {
        'none': 'No Match Found',
        'non-postal-match': 'Non-USPS Addresses',
        'missing-secondary': 'Missing Secondary',
        'unknown-secondary': 'Unknown Secondary',
        'ignored-input': 'Ignored Input'
    }
    enhancedMatchPostalDict = {
        'postal-match': 0
    }
    enhancedMatchPostalDescriptionDict = {
        'postal-match': 'USPS Addresses'
    }
    fullEnhancedMatchDict = {
        'none': 0,
        'postal-match': 0,
        'non-postal-match': 0,
        'missing-secondary': 0,
        'unknown-secondary': 0,
        'ignored-input': 0
    }
    fullEnhancedMatchDescriptionDict = {
        'none': 'No Match Found',
        'postal-match': 'USPS Addresses',
        'non-postal-match': 'Non-USPS Addresses',
        'missing-secondary': 'Missing Secondary',
        'unknown-secondary': 'Unknown Secondary',
        'ignored-input': 'Ignored Input'
    }
    zipTypeDict = {
        'Unique': 0,
        'Military': 0,
        'POBox': 0,
        'Standard': 0
    }
    zipTypeDescriptionDict = {
        'Unique': 'Unique',
        'Military': 'Military',
        'POBox': 'PO Box',
        'Standard': 'Standard'
    }
    rdiDict = {
        'Residential': 0,
        'Commercial': 0,
        'Unknown': 0
    }
    rdiDescriptionDict = {
        'Residential': 'Residential',
        'Commercial': 'Commercial',
        'Unknown': 'Unknown'
    }
    lacsLinkDict = {
        'Y': 0
    }
    lacsLinkDescriptionDict = {
        'Y': 'LACS Link Addresses'
    }
    dpvVacantDict = {
        'Y': 0
    }
    dpvVacantDescriptionDict = {
        'Y': 'Vacant'
    }
    recordTypeDict = {
        'F': 0,
        'G': 0,
        'H': 0,
        'P': 0,
        'S': 0
    }
    recordTypeDescriptionDict = {
        'F': 'Firm (Best)',
        'G': 'General Delivery (Held at local Post Office)',
        'H': 'Contains Subunits',
        'P': 'PO Box',
        'R': 'Rural Route or Highway Contract',
        'S': 'Street'
    }
    fullDictIDs = {
        1: dpvFootnotesDict,
        2: enhancedMatchDict,
        3: zipTypeDict,
        4: rdiDict,
        5: lacsLinkDict,
        6: dpvVacantDict,
        7: recordTypeDict
    }
    fullDictDescription = {
        1: dpvFootnotesDescriptionDict,
        2: enhancedMatchDescriptionDict,
        3: zipTypeDescriptionDict,
        4: rdiDescriptionDict,
        5: lacsLinkDescriptionDict,
        6: dpvVacantDescriptionDict,
        7: recordTypeDescriptionDict
    }
    colValueDict = {
        1: '[dpv_footnotes]',
        2: '[enhanced_match]',
        3: '[zip_type]',
        4: '[rdi]',
        5: '[lacslink_indicator]',
        6: '[dpv_vacant]',
        7: '[record_type]'
    }
    standardDict = {
        1: dpvFootnotesDescriptionDict,
        5: lacsLinkDescriptionDict,
        6: dpvVacantDescriptionDict,
    }
    for row in records:
        for index in fullDictIDs:
            fullDictIDs[index] = generate_stats(row, colValueDict[index], fullDictIDs[index], fullDictDescription[index])
            exampleDict = generate_stats_examples(row, fullDictIDs[index], fullDictDescription[index], exampleDict)
        if ('postal-match' in row.get('[summary]') and 'non-postal-match' not in row.get('[summary]')):
            if enhancedMatchPostalDict['postal-match'] > 0:
                    enhancedMatchPostalDict['postal-match'] += 1
                    if (enhancedMatchPostalDict['postal-match'] == 1):
                        exampleDict[enhancedMatchPostalDescriptionDict['postal-match'] + '2'] = generate_example(row)
            else:
                enhancedMatchPostalDict['postal-match'] = 1
                exampleDict[enhancedMatchPostalDescriptionDict['postal-match']] = generate_example(row)
    for index in standardDict:
        for item in standardDict[index]:
            matchedSum[fullDictDescription[index][item]] = fullDictIDs[index][item]
    matchedSum['Zip Code Type'] = create_description_dict(zipTypeDict, zipTypeDescriptionDict)
    matchedSum['RDI'] = create_description_dict(rdiDict, rdiDescriptionDict)
    matchedSum['Record Type'] = create_description_dict(recordTypeDict, recordTypeDescriptionDict)
    matchedSum['Flags'] = create_description_dict (enhancedMatchDict, enhancedMatchDescriptionDict)
    for item in matchedSum:
        if (matchedSum[item] == 0):
            delList.append(item)
    for item in delList:
        del matchedSum[item]
    return matchedSum, exampleDict
    
def create_description_dict(dict, descDict):
    finalDict = {}
    delList = []
    for item in dict:
        finalDict[descDict[item]] = dict[item]
    for item in finalDict:
        if (finalDict[item] == 0):
            delList.append(item)
    for item in delList:
        del finalDict[item]
    return finalDict

def generate_stats(row, colValue, valueDict, descriptionDict):
    finalDict = valueDict
    for item in valueDict:
        value = row.get(colValue)
        if (item in value):
            if finalDict[item] > 0:
                finalDict[item] += 1
            else:
                finalDict[item] = 1
    return finalDict

def generate_stats_examples(row, valueDict, descriptionDict, exampleDict):
    for value in valueDict:
        if (valueDict[value] == 1 and descriptionDict[value] not in exampleDict):
            exampleDict[descriptionDict[value]] = generate_example(row)
        if (valueDict[value] == 2 and descriptionDict[value] + '2' not in exampleDict):
            exampleDict[descriptionDict[value] + '2'] = generate_example(row)
    return exampleDict
        
def generate_json(inputSum, initialSum, unmatchedSum, matchedSum):
    jDict = {}
    if (len(sys.argv) - 1 == 2):
        if (sys.argv[2] in states):
            jDict["State"] = abbreviation_to_name[sys.argv[2]]
        else:
            jDict["State"] = 'State Not Found'
    jDict["Input Summary"] = inputSum
    jDict["Initial Summary"] = initialSum
    jDict["Metadata"] = matchedSum
    jDict["Unmatched Summary"] = unmatchedSum
    return json.dumps(jDict, indent=4)

def generate_example(row):
    example = str(row.get('[delivery_line_1]'))
    if (str(row.get('[delivery_line_1]')) == ''):
        example = str(row.get('street'))
    if (row.get('[last_line]') != ''):
        example = example + ' ' + str(row.get('[last_line]'))
    return example

def main():
    file_path = inputFile
    detected_delimiter = detect_delimiter(file_path)
    records = read_csv_file(file_path, delimiter=detected_delimiter)
    summary_array = count_records(records)
    recordCount = len(records)
    inputSum = generate_input_summary(records)
    initialSum = add_examples(summary_array, recordCount)
    unmatchedArray = generate_unmatched_summary(records)
    unmatchedSum = add_examples(unmatchedArray, recordCount)
    matchedArray = generate_matched_summary(records)
    matchedSum = add_examples(matchedArray, recordCount)
    output_json = generate_json(inputSum, initialSum, unmatchedSum, matchedSum)
    print(output_json)

if __name__ == "__main__":
    main()