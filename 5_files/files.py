import csv


# with open('test.csv', newline='') as in_csv,\
#      open('resuts.csv', 'w', newline='') as out_csv:
#     csv_reader = csv.reader(in_csv, delimiter=',', quotechar='"')
#     csv_writer = csv.writer(out_csv, delimiter=',',
#                             quotechar='"', quoting=csv.QUOTE_ALL)
#     headers = next(csv_reader)
#     csv_writer.writerow([headers[1], headers[0], headers[2]])
#     print("headers - ", headers)
#     for row in csv_reader:
#         # print(row)
#         print(f"Age - {row[2]}, Surname - {row[1]}, Name - {row[0]}")
#         csv_writer.writerow([row[1], row[0], row[2]])

with open('test.csv', newline='') as in_csv,\
     open('resuts.csv', 'w', newline='') as out_csv:
    reader = csv.DictReader(in_csv)

    new_fieldnames = reader.fieldnames
    new_fieldnames.append('test')
    print(new_fieldnames)
    writer = csv.DictWriter(out_csv, fieldnames=new_fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for row in reader:
        try:
            print(row['name1'])
        except:
            print("My own Error handler")
        finally:
            print("Hello")
        row['test'] = 'test_value'
        writer.writerow(row)

