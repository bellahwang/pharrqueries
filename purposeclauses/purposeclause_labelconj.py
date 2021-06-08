import xml.etree.ElementTree as ET
# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

for sentence in root.findall(".//sentence"):
    for word in sentence.findall("./word"):
        lemma = word.get('lemma')
        if (lemma == "ἵνα" or lemma == "ὅπως" or lemma == "ὡς" or lemma == "μή" or lemma == "ὄφρα" or lemma == "ἕως"):
            word.set('hasconj', 'T')
        else:
            word.set('hasconj', 'F')

tree.write('iliad_purposeclauses_1strun.xml', encoding="UTF-8")