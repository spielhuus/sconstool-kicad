#!/usr/bin/env python
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import re
import json
import xml.etree.ElementTree as ET

def number(input) :
    numbers = ''
    for char in input :
        if char.isdigit() :
            numbers += char

    return int(numbers)

def letter(input) :
    letters = ''
    for char in input :
        if char.isalpha() :
            letters += char

    return letters

def bom_parser(source, target) :
    
    root = ET.parse(source).getroot()
    target_sorted = {}
    # parse the xml file
    for compomnents in root.findall('components'):
        for c in compomnents.findall('comp'):
            if c.find('libsource').get('lib') != 'Mechanical' :
                description = ''
                for f in c.findall('fields/field'):
                    if f.get('name') == 'Description' :
                        description = f.text
                if description == '':
                    description = c.find('footprint').text

                el_datasheet = c.find('datasheet').text
                datasheet = '~'
                if( datasheet != None ) :
                    datasheet = el_datasheet.text

                target_sorted[('%s%03d' % (letter(c.get('ref')), number(c.get('ref'))))] = {
                    'ref': c.get('ref'), 
                    'value': c.find('value').text, 
                    'datasheet': datasheet, 
                    'description': description,
                    'footprint': c.find('footprint').text
                }

    target_grouped = {}
    for key in sorted(target_sorted) :
        element = target_sorted[key]
        if ('%s-%s' % (element['value'], element['footprint'])) in target_grouped :
            target_grouped[('%s-%s' % (element['value'], element['footprint']))]['ref'].append(element['ref'])
        else :
            target_grouped[('%s-%s' % (element['value'], element['footprint']))] = {
                'ref': [element['ref']], 
                'value': element['value'], 
                'datasheet': element['datasheet'], 
                'description': element['description'],
                'footprint': element['footprint']
            }
                
    res_target = []
    for key in target_grouped :
        element = target_grouped[key]
        res_target.append({
            'ref': element['ref'], 
            'value': element['value'], 
            'datasheet': element['datasheet'], 
            'description': element['description'],
            'footprint': element['footprint']
        })
    target['bom'] = res_target

    return None

def kibot_parser(source, target) :

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

    return None

def combine_reports(source) :
    result = {}
    for s in source :
        with open(s) as f:
            reports = json.load(f)
            for name in reports :
                if name not in result :
                    result[name] = {'summary': {}}
                count_results(s, result[name]['summary'])
                for board in reports[name] :
                    if board not in result[name] :
                        result[name][board] = {}
                    for report in reports[name][board] :
                        result[name][board][report] = reports[name][board][report]
    return result

def count_results(source, results) :
    with open(source) as f:
        reports = json.load(f)
        for name in reports :
            for board in reports[name] :
                if board == 'unit_test' :
                    test = reports[name][board]['report']['summary']
                    results[board] = {'passed': test['passed'], 'num_tests': test['num_tests']}
                else :
                    for report in reports[name][board] :
                        if report != 'bom' :
                            if report not in results :
                                results[report] = len(reports[name][board][report])
                            else :
                                results[report] += len(reports[name][board][report])
    return results