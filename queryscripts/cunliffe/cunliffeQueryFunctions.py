import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "cunliffe.lexentries.unicode-copy.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()


def FullEntry(inputWord):
	for entry in root.findall(".//TEI:div[@type='textpart']", ns):
		wordEntry = entry.get('n')
		if (wordEntry != None):
			if (wordEntry == inputWord):
				for head in entry.findall("./TEI:head", ns):
					head = head.get("id")
					for p in entry.findall("./TEI:p", ns):
						print("Head:", head, "Entry:", p.text)
					for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
						for head in subCat.findall("./TEI:head", ns):
							head = head.get("id")
							for p in subCat.findall("./TEI:p", ns):
								print("Head:", head, "Entry:", p.text)

def Gloss(inputWord):
	for entry in root.findall(".//TEI:div[@type='textpart']", ns):
		wordEntry = entry.get('n')
		if (wordEntry != None):
			for head in entry.findall("./TEI:head", ns):
				head = head.get("id")
				for gloss in entry.findall("./TEI:gloss", ns):
					print("Head:", head, "Gloss:", gloss.text)
					for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
						for head in subCat.findall("./TEI:head", ns):
							head = head.get("id")
							for gloss in subCat.findall("./TEI:gloss", ns):
								print("Head:", head, "Gloss:", gloss.text)

def Citations(inputWord, inputCommand):
	for entry in root.findall(".//TEI:div[@type='textpart']", ns):
		wordEntry = entry.get('n')
		if (wordEntry != None):
			for head in entry.findall("./TEI:head", ns):
				head = head.get("id")
				for cit in entry.findall("./TEI:cit", ns):
					for quote in cit.findall("./TEI:quote", ns):
								     # bold	      green									end
						print(head, "\033[1m" + "\33[32m" + "'" + quote.text + "'" + "\x1b[0m")
						for bibl in cit.findall("./TEI:bibl", ns):
							biblEntry = bibl.get('n')
							print(head, biblEntry)
							if (biblEntry.startswith('Hom. Il.')):
								returnIliad(wordEntry, biblEntry)
								print("")
								print("")
							else:
								returnOdyssey(wordEntry, biblEntry)
								print("")
								print("")
				for bibl in entry.findall("./TEI:bibl", ns):
					biblEntry = bibl.get('n')
					print(head, biblEntry)
					if (biblEntry.startswith('Hom. Il.')):
						returnIliad(wordEntry, biblEntry)
						print("")
						print("")
					else:
						returnOdyssey(wordEntry, biblEntry)
						print("")
						print("")
				
				for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
					for head in subCat.findall("./TEI:head", ns):
						head = head.get("id")
						for cit in entry.findall("./TEI:cit", ns):
							for quote in cit.findall("./TEI:quote", ns):
										     # bold	      green									end
								# print(head, "\033[1m" + "\33[32m" + "'" + quote.text + "'" + "\x1b[0m")
								print(head, quote.text)
								for bibl in cit.findall("./TEI:bibl", ns):
									biblEntry = bibl.get('n')
									print(biblEntry)
									if (biblEntry.startswith('Hom. Il.')):
										returnIliad(wordEntry, biblEntry)
										print("")
										print("")
									else:
										returnOdyssey(wordEntry, biblEntry)
										print("")
										print("")
						for bibl in subCat.findall(".//TEI:bibl", ns):
							biblEntry = bibl.get('n')
							print(head, biblEntry)
							if (biblEntry.startswith('Hom. Il.')):
								returnIliad(wordEntry, biblEntry)
								print("")
								print("")
							else:
								returnOdyssey(wordEntry, biblEntry)
								print("")
								print("")