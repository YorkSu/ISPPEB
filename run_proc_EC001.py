import csv
with open('EC001.csv', 'r') as f: ec001_raw_data = [[i[0]] for i in csv.reader(f)][1:]
output_data = [[{'': -1, '1': 3, '2': 1, '3': 2}[i[0] if i else i]] for item in ec001_raw_data for i in item]
mode_dict = dict((i, output_data.count([i])) for i in range(1, 4))
mode = max(mode_dict, key=mode_dict.get)
output_data = [i[0] == -1 and [mode] or i for i in output_data]
output_data.insert(0, ['physical_examination_behave'])
with open('OUTPUT_EC001.csv', 'w', newline='') as f: csv.writer(f).writerows(output_data)
