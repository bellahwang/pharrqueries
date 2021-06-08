import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "iliad_purposeclauses_1strun.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()
isthereconj = False

for sentence in root.findall(".//sentence"):
    isthereconj = False
    for word in sentence.findall("./word"):
        hasconj = word.get('hasconj')
        if (hasconj == 'T'):
            isthereconj = True
            sentence.set('hasconj', 'T')
    if (isthereconj == False):
        sentence.set('hasconj', 'F')

tree.write('iliad_purposeclauses_2ndrun.xml', encoding="UTF-8")