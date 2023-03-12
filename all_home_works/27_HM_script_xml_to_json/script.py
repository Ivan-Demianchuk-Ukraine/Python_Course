def converter_xml_to_json(xml_file):
    import xml.etree.ElementTree as ET
    import json
    three = ET.parse(f'{xml_file}')
    root = three.getroot()
    json_info = {}
    page_count = 0
    for page in root:
        page = page.attrib['name']
        json_info[f'{page}'] = {}
        i = 0
        for element in root[page_count].iter('element'):
            json_info[f'{page}'][element.attrib['name']] = {}

            for locator in root[page_count][i].iter('locator'):
                json_info[f'{page}'][element.attrib['name']][locator.attrib['platform']]\
                    = [locator.attrib['locator_type']] + [locator.text]
            i = i + 1
        page_count += 1

    json_info = json.dumps(json_info, indent=4)
    with open('json_new_file.json', 'w') as f:
        f.writelines(json_info)
    return json_info


converter_xml_to_json('xml_file.xml')
