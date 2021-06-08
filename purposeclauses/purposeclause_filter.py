import lxml.etree as ET

# change FILENAME to local path
FILENAME = "iliad_purposeclauses_2ndrun.xml"

root = ET.parse(FILENAME)

for sentence in root.xpath(".//sentence[@hasconj='F']"):
    sentence.getparent().remove(sentence)

root.write('iliad_purposeclauses_3rdrun.xml', pretty_print=True, encoding="UTF-8", xml_declaration=True)