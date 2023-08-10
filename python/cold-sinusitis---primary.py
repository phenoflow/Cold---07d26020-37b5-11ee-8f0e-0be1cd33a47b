# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"H01..00","system":"readv2"},{"code":"H01..11","system":"readv2"},{"code":"H010.00","system":"readv2"},{"code":"H011.00","system":"readv2"},{"code":"H012.00","system":"readv2"},{"code":"H013.00","system":"readv2"},{"code":"H01y.00","system":"readv2"},{"code":"H01y000","system":"readv2"},{"code":"H01yz00","system":"readv2"},{"code":"H01z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cold-sinusitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cold-sinusitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cold-sinusitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
