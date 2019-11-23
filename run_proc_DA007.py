import csv
with open('DA007.csv', 'r') as f: da007_raw_data = [i for i in csv.reader(f)][1:]
output_data = [[1 if any(item) else 0] for item in da007_raw_data]
output_data.insert(0, ['chronic_disease'])
with open('OUTPUT_DA007.csv', 'w', newline='') as f: csv.writer(f).writerows(output_data)
# print(output_data)
