import bibtexparser
from rapidfuzz import fuzz

loc = r'D:\src\thesis1\3-BackMattar\thesis.bib'

with open(loc, 'r', encoding='utf-8') as bibfile:
    db = bibtexparser.load(bibfile)

entries = [(entry.get('ID', '').strip(), entry.get('title', '').strip()) for entry in db.entries]
visited = set()

for i in range(len(entries)):
    key_i, title_i = entries[i]
    if key_i in visited:
        continue
    group = [key_i]
    for j in range(i + 1, len(entries)):
        key_j, title_j = entries[j]
        if key_j in visited:
            continue
        if fuzz.ratio(title_i, title_j) >= 80:
            group.append(key_j)
            visited.add(key_j)
    if len(group) > 1:
        for k in group:
            print(k)
        print("---")
