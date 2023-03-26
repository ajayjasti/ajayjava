import xml.dom.pulldom as pulldom
import xml.etree.ElementTree as ET

# Load the XML document
with open('student.xml', 'r') as f:
    xml_document = f.read()

# Load the Schema
with open('student.xsd', 'r') as f:
    xml_schema = f.read()

# Parse the XML document
document_tree = ET.fromstring(xml_document)

# Validate the XML document against its schema
if document_tree.tag != 'class':
    print("XML document is invalid: root element is not 'class'.")
    exit()

for student in document_tree.findall('student'):
    # Validate student tag
    if 'id' not in student.attrib:
        print("XML document is invalid: student tag is missing 'id' attribute.")
        exit()

    # Validate name tag
    name = student.find('name')
    if name is None:
        print("XML document is invalid: student tag is missing 'name' tag.")
        exit()
    if not name.text:
        print("XML document is invalid: 'name' tag is empty.")
        exit()

    # Validate dob tag
    dob = student.find('dob')
    if dob is None:
        print("XML document is invalid: student tag is missing 'dob' tag.")
        exit()
    if not dob.text:
        print("XML document is invalid: 'dob' tag is empty.")
        exit()

print("XML document is valid.")
