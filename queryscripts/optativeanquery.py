from englishalignment import printEngSent
from grkalignment_2var import printGrkSent2
from grkalignment import printGrkSent

import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg002.perseus-grc1.tb.xml"
tree = ET.parse(FILENAME)
root = tree.getroot()

count = 1		    #sets counter keeping track of query results
subjid = None 		#in case the code encounters a subjunctive first
anhead = None		#in case the code encounters an ἄν first
anid = None

# for html file conversion
# sys.stdout.write("<table>" + "\n")

for sentence in root.findall('.//sentence'):
	sentid = sentence.get('id')
	for word in sentence.findall('./word'):
		if 'postag' in word.attrib:
			postag = word.get('postag')
			mood = postag[4]
			form = word.get('form')
			cite = word.get('cite')
			lemma = word.get('lemma')
			if lemma == 'ἄν':
			 	anhead = word.get('head')
			 	anid = word.get('id')
			else: #only other possibility is if the word is a subjunctive
				subjid = word.get('id')
				if (mood == 'o'):
					if anhead == subjid: #checks if ἄν modifies subjunctive
						
						# comment out if converting to html
						print(count, "form: ", form, "lemma: ", lemma, "cite: ", cite)
						printGrkSent2(sentid, subjid, anid)
						print('')
						printEngSent(sentid)
						print('')
						print('')
						count += 1
						
						# for html file conversion
						# sys.stdout.write("\t" + "<tr>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + form + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + lemma + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + cite + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>")
						# printGrkSent2(sentid, subjid, anid)
						# sys.stdout.write("</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>")
						# printEngSent(sentid)
						# sys.stdout.write("\t" + "\t" + "</td>" + "\n")
						# sys.stdout.write("\t" + "</tr>" + "\n")

					else:
						
						# comment out if converting to html
						print(count, "form: ", form, "lemma: ", lemma, "cite: ", cite)
						printGrkSent(sentid, subjid)
						print('')
						printEngSent(sentid)
						print('')
						print('')
						count += 1

						# for html file conversion
						# sys.stdout.write("\t" + "<tr>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + form + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + lemma + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>" + cite + "</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>")
						# printGrkSent(sentid, subjid)
						# sys.stdout.write("</td>" + "\n")
						# sys.stdout.write("\t" + "\t" + "<td>")
						# printEngSent(sentid)
						# sys.stdout.write("\t" + "\t" + "</td>" + "\n")
						# sys.stdout.write("\t" + "</tr>" + "\n")

# for html file conversion
# sys.stdout.write("</table>")
