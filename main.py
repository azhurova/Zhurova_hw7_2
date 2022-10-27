import os

fin = {}
for file in os.listdir('files'):
  with open(os.path.join('files', file), encoding='utf-8') as f:
    text = f.readlines()
    len_text = len(text)
    text1 = "".join(text)
    fin[file] = (len_text, text1)
#print(fin)

fin1 = {}
for x in sorted(fin, key=fin.get):
  fin1[x] = fin[x]
#print(fin1) сортированный по количеству строк

with open('all_file.txt', 'w', encoding='utf-8') as f:
  for key, value in fin1.items():

    f.writelines(key+'\n')
    f.writelines(f'{value[0]}\n')
    f.writelines(f'{value[1]}\n')