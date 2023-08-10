# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"F51..00","system":"readv2"},{"code":"F510.00","system":"readv2"},{"code":"F510z00","system":"readv2"},{"code":"F513z00","system":"readv2"},{"code":"F514z00","system":"readv2"},{"code":"F520.00","system":"readv2"},{"code":"F520300","system":"readv2"},{"code":"F520z00","system":"readv2"},{"code":"F522.00","system":"readv2"},{"code":"F523.00","system":"readv2"},{"code":"FyuP000","system":"readv2"},{"code":"FyuP100","system":"readv2"},{"code":"FyuP200","system":"readv2"},{"code":"H040600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nonsuppurative-cold---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nonsuppurative-cold---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nonsuppurative-cold---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
