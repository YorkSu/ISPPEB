import csv
with open('MUTI_DA056_DA057.csv', 'r') as f: sp_data = [int(i[0]) for i in csv.reader(f) if i[0].isdigit()][:20000]
with open('OUTPUT_EC001.csv', 'r') as f: peb_data = [int(i[0]) for i in csv.reader(f) if i[0].isdigit()][:20000]
comp_data = list(zip(sp_data, peb_data))
mode_type, mode_data = [], []
for i in comp_data:
  if i not in mode_type:
    mode_type.append(i)
    mode_data.append(1)
    continue
  mode_data[mode_type.index(i)] += 1
frequency_data = [[mode_type[inx][0], mode_type[inx][1], mode_data[inx]] for inx in range(len(mode_type))]
frequency_data.insert(0, ['social_participation', 'physical_examination_behave', 'frequency'])
with open('OUTPUT_SP_PEB_FRQ.csv', 'w', newline='') as f: csv.writer(f).writerows(frequency_data)
