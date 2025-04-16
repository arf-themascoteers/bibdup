import bibtexparser

loc = r'D:\src\thesis1\3-BackMattar\thesis.bib'

with open(loc, 'r', encoding='utf-8') as bibfile:
    db = bibtexparser.load(bibfile)

title_map = {}

for entry in db.entries:
    title = entry.get('title', '').strip()
    key = entry.get('ID', '').strip()
    title_map.setdefault(title, []).append(key)

for keys in title_map.values():
    if len(keys) > 1:
        for k in keys:
            print(k)
