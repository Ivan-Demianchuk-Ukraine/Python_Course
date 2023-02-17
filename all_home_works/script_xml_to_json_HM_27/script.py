

def converter_xml_to_json(xml_file):
    import xml.etree.ElementTree as ET
    import json
    three = ET.parse(f'{xml_file}')
    root = three.getroot()
    json_info = {}
    count = 0
    for page in root:
        page = page.attrib['name']
        json_info[f'{page}'] = {}
        for element in root[count].iter('element'):
            json_info[f'{page}'][element.attrib['name']] = {}
            for locator in root[count].iter('locator'): #тут надо чтобы не in root[count] было, а глубже типо root[count][element]
                json_info[f'{page}'][element.attrib['name']][locator.attrib['platform']] = [locator.attrib['locator_type']] + [locator.text]

        count += 1
    json_info = json.dumps(json_info, indent=4)
    with open('json_new_file.json', 'w') as f:
        f.writelines(json_info)
    return json_info


print(converter_xml_to_json('xml_file.xml'))
