# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"H13..00","system":"readv2"},{"code":"H01..11","system":"readv2"},{"code":"63733.0","system":"readv2"},{"code":"17173.0","system":"readv2"},{"code":"54375.0","system":"readv2"},{"code":"1674.0","system":"readv2"},{"code":"5437.0","system":"readv2"},{"code":"39501.0","system":"readv2"},{"code":"18572.0","system":"readv2"},{"code":"49548.0","system":"readv2"},{"code":"15163.0","system":"readv2"},{"code":"4433.0","system":"readv2"},{"code":"48703.0","system":"readv2"},{"code":"2257.0","system":"readv2"},{"code":"10546.0","system":"readv2"},{"code":"33437.0","system":"readv2"},{"code":"J32","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-sinusitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sinusitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sinusitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sinusitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
