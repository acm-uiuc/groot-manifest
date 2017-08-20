import xml.etree.ElementTree as ET

SCHEMA = {
    'remote': ['name', 'fetch'],
    'default': ['remote', 'revision'],
    'project': ['path', 'name']
}

tree = ET.parse('default.xml')
root = tree.getroot()
for child in root:
    # Check that child tag is valid
    assert child.tag in SCHEMA.keys(), '"{}" not in {}'.format(child.tag, SCHEMA.keys())

    # Check that child has necessary keys
    for attrib in SCHEMA[child.tag]:
        assert attrib in child.attrib, '"{}" not in {}'.format(attrib, child.attrib)
