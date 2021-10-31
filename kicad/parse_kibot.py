import re
import xml.etree.ElementTree as ET

def bom_parser(source) :
    
    target = []
    root = ET.parse(source).getroot()

    for compomnents in root.findall('components'):
        for c in compomnents.findall('comp'):
            if c.find('libsource').get('lib') != 'Mechanical' :
                description = ''
                for f in c.findall('fields/field'):
                    if f.get('name') == 'Description' :
                        description = f.text
                if description == '':
                    description = c.find('footprint').text

                target.append({
                    'ref': c.get('ref'), 
                    'value': c.find('value').text, 
                    'datasheet': c.find('datasheet').text, 
                    'description': description
                })

    return target

def kibot_parser(source) :

    target = {}
    p_erc_err_drc = re.compile('^\*\* Found (.*) DRC errors \*\*$')
    p_nc_err = re.compile('^\*\* Found (.*) unconnected pads \*\*$')
    p_erc_err = re.compile('^ERC report \((.*)\)$')
    p_erc_sheet = re.compile('^\*\*\*\*\* Sheet (.*)$')
    p_err_type = re.compile('^ErrType\((.*)\): (.*)$')
    p_err_entry = re.compile('^.*@\((.*) mm, (.*) mm\): (.*)$')

    act_list = []
    act_message = {}
    sheet_name = '/'

    with open(source) as f:
        lines = f.readlines()
        for line in lines:

            if( p_erc_err_drc.match(line) ):
                act_list = []
                target['drc'] = act_list

            elif( p_nc_err.match(line) ):
                act_list = []
                target['unconnected'] = act_list

            elif( p_erc_err.match(line) ):
                act_list = []
                target['erc'] = act_list

            elif( p_erc_sheet.match(line) ):
                err = p_erc_sheet.match(line)
                sheet_name = err.group(1)

            elif( p_err_type.match(line) ):
                err = p_err_type.match(line)
                act_message = {'code':err.group(1), 'sheet': sheet_name, 'message':err.group(2), 'con':[]}
                act_list.append(act_message)

            elif( p_err_entry.match(line) ):
                err = p_err_entry.match(line)
                act_message['con'].append( {'x':err.group(1), 'y':err.group(2), 'message':err.group(3)})

    return target


