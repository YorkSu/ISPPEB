import csv
with open('DA056.csv', 'r') as f: da056_raw_data = list(csv.reader(f))[1:]
da056_mid_data = [[0 if i == '' else 1 for i in item] for item in da056_raw_data]
with open('DA057.csv', 'r') as f: da057_raw_data = list(csv.reader(f))[1:]
da057_mid_data = [[{'': 0, '1': 3, '2': 2, '3': 1}[i[0] if i else i] for i in item] for item in da057_raw_data]
muti_data = [da056_mid_data[i][-1] and [0] or (not any(da056_mid_data[i])) and [-1] or [sum([da056_mid_data[i][inx] * da057_mid_data[i][inx] for inx in range(len(da057_mid_data[i]))])] for i in range(len(da056_mid_data))]
mode_dict = dict((i, muti_data.count([i])) for i in range(0, 34))
mode = max(mode_dict, key=mode_dict.get)
muti_data = [i[0] == -1 and [mode] or i for i in muti_data]
muti_data.insert(0, ['social_participation'])
with open('MUTI_DA056_DA057.csv', 'w', newline='') as f: csv.writer(f).writerows(muti_data)
