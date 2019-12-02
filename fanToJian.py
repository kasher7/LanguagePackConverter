from hanziconv import HanziConv as hanz
import xml.etree.ElementTree as ET
import os

rootdir = 'ZH_Hant_HK'

def toSimplified(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    # changing a field text
    for elem in root.iter('Text'):
        elem.text = hanz.toSimplified(elem.text)

    tree.write('NewPack\\' + file_name, encoding="utf-8")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        toSimplified(os.path.join(subdir, file))


