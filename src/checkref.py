import bibtexparser
from collections import defaultdict

# ================
# CONFIG.  pip install bibtexparser
# ================
input_file = "references.bib"      # tu .bib original
output_file = "references_clean.bib"  # salida limpia

# Campos básicos que casi siempre deberían estar
required_fields = {"author", "title", "year"}

# ================
# SCRIPT
# ================
with open(input_file, encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

entries = bib_database.entries

seen_ids = set()
seen_dois = set()
clean_entries = []
problems = defaultdict(list)

for entry in entries:
    entry_id = entry.get("ID")
    doi = entry.get("doi", "").lower().strip()

    # Check ID duplicados
    if entry_id in seen_ids:
        problems["Duplicate ID"].append(entry_id)
        continue
    seen_ids.add(entry_id)

    # Check DOI duplicados
    if doi and doi in seen_dois:
        problems["Duplicate DOI"].append((entry_id, doi))
        continue
    if doi:
        seen_dois.add(doi)

    # Check campos requeridos
    missing = [f for f in required_fields if f not in entry]
    if missing:
        problems["Missing fields"].append((entry_id, missing))

    clean_entries.append(entry)

# Guardar limpio
bib_database.entries = clean_entries
with open(output_file, "w", encoding="utf-8") as bibfile:
    bibtexparser.dump(bib_database, bibfile)

# Reporte
print("=== REVISIÓN .BIB ===")
if problems:
    for k, v in problems.items():
        print(f"\n{k}:")
        for item in v:
            print("  ", item)
else:
    print("✅ Sin problemas encontrados.")

print(f"\nArchivo limpio exportado en: {output_file}")