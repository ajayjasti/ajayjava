import xml.dom.pulldom as pulldom

# Initialize the parser
events = pulldom.parse("student.xml")

# Load the DTD
with open('student.dtd', 'r') as f:
    dtd = f.read()

# Iterate over the XML document
for event in events:
    # Check for the start of an element
    if type(event) == pulldom.START_ELEMENT:
        # Validate against the DTD
        if event.tagName == "student":
            # Check for the required "id" attribute
            if "id" not in event.attributes:
                print("ERROR: Missing 'id' attribute in <student> element.")
                break
                
        # Check for the required "name" and "dob" elements
        if event.tagName in ["name", "dob"]:
            if not events.expandNode(event).data.strip():
                print(f"ERROR: Missing value in <{event.tagName}> element.")
                break
                
print("The document is valid")
