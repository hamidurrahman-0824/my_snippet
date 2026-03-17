import csv
with open('customers-1000.csv', 'r') as src:
    src = csv.reader(src)
    with open('csv_names.csv','w') as dest:
        csv_writer = csv.writer(dest, delimiter= '\t')
        for line in src:
            csv_writer.writerow(line)
#DictReader
#DictReader
