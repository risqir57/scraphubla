from mathematicians import simple_get

raw_html = simple_get('http://hubla.dephub.go.id/berita/Pages/AUDITOR-MANAJEMEN-KESELAMATAN-KAPAL-HARUS-MILIKI-KOMPETENSI-MEMADAI.aspx')
p = raw_html.find("div", {"class": "article"}).next_sibling
print(p)