import pprint
import os


def lower_func(elem):
    return elem.lower()


def ext_check(file_name):
    return os.path.splitext(file_name)[1]


def json_read(file_name):
    import json
    json_list = []
    with open(file_name, encoding='utf8') as jnews:
        data = json.load(jnews)
    for desr in data['rss']['channel']['items']:
        json_list.extend(map(lower_func, desr['description'].split()))
    return json_list


def xml_read(file_name):
    import xml.etree.ElementTree as ET
    xml_list = []
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    xml_item = root.findall('channel/item/description')
    for item in xml_item:
        xml_list.extend(map(lower_func, item.text.split()))
    return xml_list


def top_words(file_name, top):
    if ext_check(file_name) == '.json':
        word_list = json_read(file_name)
    elif ext_check(file_name) == '.xml':
        word_list = xml_read(file_name)

    fin_list = []
    for elem in word_list:
        if len(elem) > 6:
            if elem not in fin_list:
                fin_list.append([word_list.count(elem), elem])

    return sorted(fin_list[:top], reverse=True)


pprint.pprint(top_words('newsafr.json', 10))
print()
pprint.pprint(top_words('newsafr.xml', 10))
