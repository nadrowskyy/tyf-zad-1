import re


id_dict = dict()

for i in range(1, 281):
    id_dict[i] = 1

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('index2.html', 'w', encoding='utf-8') as file:
    for count, line in enumerate(lines):
        print(count)
        if 'class="footnote-harvard" aria-describedby="goTo">' in line:
            mtch_footnote = re.search(
                '<a href="#h?\d+" id="refh\d+" class="footnote-harvard" aria-describedby="goTo">\[?\d+\]?<\/a>', line)
            mtch_ref = re.search('id="refh\d+"', mtch_footnote.group(0))
            mtch_id = re.search('\d+', mtch_ref.group(0))
            tmp_id = int(mtch_id.group(0))
            tmp_value = id_dict[tmp_id]
            tmp_ref = f'id="refh{tmp_id}-{tmp_value}"'
            mtch_footnote_2 = mtch_footnote.group(0).replace(mtch_ref.group(0), tmp_ref)
            id_dict[tmp_id] = tmp_value + 1
            line_2 = line.replace(mtch_footnote.group(0), mtch_footnote_2)
            id_improve = re.search('href="#\d+"', line_2)
            if id_improve is not None:
                line_2 = line_2.replace(id_improve.group(0), f'href="#h{tmp_id}"')
            file.write(line_2)
        else:
            file.write(line)