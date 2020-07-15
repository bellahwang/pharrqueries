
from iliad import returnIliad
from odyssey import returnOdyssey
import cunliffeQueryFunctions
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "cunliffe.lexentries.unicode-copy.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

inputWord = input("Enter a lemma to search the Cunliffe Lexicon. ")

for entry in root.findall(".//TEI:div[@type='textpart']", ns):
	wordEntry = entry.get('n')
	wordCode = entry.get('{http://www.w3.org/XML/1998/namespace}id')
	if (wordEntry != None):
		if (wordEntry == inputWord):
			print("Found " + inputWord + "!")
			while(True):
				print("Choose one of the following options. Type 'Quit' or 'q' to exit.")
				print("|")
				print(" ->", "Full Entry (f)")
				print("|")
				print(" ->", "Gloss (g)")
				print("|")
				print(" ->", "Citations (c)")
				print("     |")
				print("      ->", "Citations with notes (cn)")
				print(" ->", "References (r)")
				print("|")
				print(" ->", "Terms (t)")
				print("     |")
				print("      ->", "Terms with notes (tn)")
				print(" ->", "Quit (q)")

				userInput = input("Enter: ")

				if (userInput == "Full Entry" or userInput == "f"):
					cunliffeQueryFunctions.FullEntry(inputWord)
					print("")

				elif (userInput == "Gloss" or userInput == "g"):
					cunliffeQueryFunctions.Gloss(inputWord)
					print("")

				elif (userInput == "Citations" or userInput == "c"):
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

				elif (userInput == "Citations with notes" or userInput == "cn"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for cit in entry.findall("./TEI:cit", ns):
							for quote in cit.findall("./TEI:quote", ns):
										     # bold	      green									end
								print(head, "\033[1m" + "\33[32m" + "'" + quote.text + "'" + "\x1b[0m")
								for note in cit.findall("./TEI:note", ns):
									print("(" + note.text + ")")
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
										print(head, "\033[1m" + "\33[32m" + "'" + quote.text + "'" + "\x1b[0m")
										for note in cit.findall("./TEI:note", ns):
											print("(" + note.text + ")")
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

				elif (userInput == "References" or userInput == "r"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for ref in entry.findall("./TEI:cit/TEI:ref", ns):
							target = ref.get("target")
							if (target != None):
								print(head, ref.text, target)
						for ref in entry.findall("./TEI:ref", ns):
							target = ref.get("target")
							if (target != None):
								print(head, ref.text, target)
						for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
							for head in subCat.findall("./TEI:head", ns):
								head = head.get("id")
								for ref in subCat.findall("./TEI:cit/TEI:ref", ns):
									target = ref.get("target")
									if (target != None):
										print(head, ref.text, target)
								for ref in subCat.findall("./TEI:ref", ns):
									print(head, ref.text, target)
									target = ref.get("target")
									if (target != None):
										print(head, ref.text, target)
					print("")

				elif (userInput == "Terms" or userInput == "t"):
					for head in entry.findall("./TEI:head", ns):
						head = head.get("id")
						for term in entry.findall("./TEI:cit/TEI:term", ns):
							print("Head:", head, "Term:", term.text, "Attributes:", term.attrib)
						for term in entry.findall("./TEI:term", ns):
							print("Head:", head, "Term:", term.text, "Attributes:", term.attrib)
						for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
							for head in subCat.findall("./TEI:head", ns):
								head = head.get("id")
								for term in subCat.findall("./TEI:cit/TEI:term", ns):
									print("Head:", head, "Term:", term.text, "Attributes:", term.attrib)
								for term in subCat.findall("./TEI:term", ns):
									print("Head:", head, "Term:", term.text, "Attributes:", term.attrib)
					# for head in entry.findall("./TEI:head", ns):
					# 	head = head.get("id")
					# 	for term in entry.findall("./TEI:term", ns):
					# 		print(head, term.text, term.attrib)
					# 	for subCat in entry.findall("./TEI:div[@type='textpart']", ns):
					# 		for head2 in subCat.findall("./TEI:head", ns):
					# 			head2 = head2.get("id")
					# 			for term in subCat.findall("./TEI:term", ns):
					# 				print(head2, term.text, term.attrib)
					print("")

				elif (userInput == "Quit" or userInput == "q"):
					break
				else:
					print("Invalid command. Please try again.")
					print("")
