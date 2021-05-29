import re


with open('harvard.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('harvard2.txt', 'w', encoding='utf-8') as file:
    for count, line in enumerate(lines):
        print(count)
        if 'alt="Wróć do treści"></a>' in line:
            m = re.search('href="#refh\d+"', line)
            line = line.replace(m.group(0), 'href="javascript:void(0);" onclick="footRev(this)"')
            file.write(line)
        else:
            file.write(line)