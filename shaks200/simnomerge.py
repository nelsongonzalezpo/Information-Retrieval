import xml.etree.ElementTree as ET

e = ET.parse('/Users/leonardomoya/Dropbox/recuperacion/shaks200/as_you.xml').getroot()
words = set()


def traverse(root, counter):
    for child in root:
        print("   "*counter, child.tag, child.text)
        traverse(child, counter+1)

traverse(e, 0)
personas = e.findall(".//*")
for p in personas:
    print("  ", p.text)

    quit
