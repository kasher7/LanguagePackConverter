from hanziconv import HanziConv as hanz
import xml.etree.ElementTree as ET
import os

rootdir = '.'

def toSimplified(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    # changing a field text
    for elem in root.iter():
        if elem.text is not None:
            elem.text = hanz.toSimplified(elem.text)

    tree.write(file_name, encoding="utf-8")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".xml"):
            print(os.path.join(subdir, file))
            toSimplified(os.path.join(subdir, file))



