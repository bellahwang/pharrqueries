from englishalignment import printEngSent
from grkalignment import printGrkSent

import sys
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "tlg0012.tlg002.perseus-grc1.tb.xml"
tree = ET.parse(FILENAME)
root = tree.getroot()

count = 1		    #sets counter keeping track of query results

# for html file conversion
sys.stdout.write("<table>" + "\n")

for sentence in root.findall('.//sentence'):
	sentid = sentence.get('id')
	for word in sentence.findall('./word'):
		if 'postag' in word.attrib:
			postag = word.get('postag')
			tense = postag[3]
			form = word.get('form')
			cite = word.get('cite')
			lemma = word.get('lemma')
			id = word.get('id')
			
			if (tense == 'f'):
				sys.stdout.write("\t" + "<tr>" + "\n")
				sys.stdout.write("\t" + "\t" + "<td>" + form + "</td>" + "\n")
				sys.stdout.write("\t" + "\t" + "<td>" + lemma + "</td>" + "\n")
				sys.stdout.write("\t" + "\t" + "<td>" + cite + "</td>" + "\n")
				sys.stdout.write("\t" + "\t" + "<td>")
				printGrkSent(sentid, id)
				sys.stdout.write("</td>" + "\n")
				sys.stdout.write("\t" + "\t" + "<td>")
				printEngSent(sentid)
				sys.stdout.write("\t" + "\t" + "</td>" + "\n")
				sys.stdout.write("\t" + "</tr>" + "\n")

# for html file conversion
sys.stdout.write("</table>")
