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

import unittest

from sys import path as syspath
from os import path as ospath
from pathlib import Path
import json

syspath.append("..")

comnbined_result = {"kontur": {'summary': {'drc': 0, 'unconnected': 0, 'erc': 0}, "main": {"bom": [{"ref": ["C1", "C2"], "value": "22u", "datasheet": "~", "description": "Aluminium Electrolytic Capacitors (50V, D=6.3 mm, LS=2.5 mm)", "footprint": "Capacitor_THT:CP_Radial_D6.3mm_P2.50mm"}, {"ref": ["C3", "C4", "C5", "C6", "C8", "C10", "C11"], "value": "0.1u", "datasheet": "~", "description": "Multilayer Ceramic Capacitors MLCC (50V, L=4 mm, W=2.5 mm, LS=2.5 mm)", "footprint": "Capacitor_THT:C_Rect_L4.0mm_W2.5mm_P2.50mm"}, {"ref": ["C7", "C9"], "value": "2.2u", "datasheet": "~", "description": "Multilayer Ceramic Capacitors MLCC (25V, L=6 mm, W=5.5 mm, LS=5 mm)", "footprint": "Capacitor_THT:C_Disc_D6.0mm_W4.4mm_P5.00mm"}, {"ref": ["D1", "D4", "D7", "D8", "D9", "D10", "D11", "D12", "D15", "D18", "D19", "D20", "D21", "D22"], "value": "1N4148", "datasheet": "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf", "description": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal", "footprint": "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal"}, {"ref": ["D2", "D3", "D5", "D6", "D13", "D14", "D16", "D17"], "value": "1N4148", "datasheet": "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf", "description": "Diode_THT:D_DO-35_SOD27_P2.54mm_Vertical_KathodeUp", "footprint": "Diode_THT:D_DO-35_SOD27_P2.54mm_Vertical_KathodeUp"}, {"ref": ["J1"], "value": "01x09 Female", "datasheet": "~", "description": "Board to Board Connectors (2.54 mm)", "footprint": "Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical"}, {"ref": ["J2"], "value": "10 Pos", "datasheet": "~", "description": "Pin Header IDC (2.54mm)", "footprint": "Connector_IDC:IDC-Header_2x05_P2.54mm_Vertical"}, {"ref": ["J3"], "value": "01x07 Female", "datasheet": "~", "description": "Board to Board Connectors (2.54 mm)", "footprint": "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical"}, {"ref": ["R1", "R16", "R19", "R32"], "value": "100k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R2", "R20"], "value": "27k", "datasheet": "~", "description": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R3", "R21"], "value": "390k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R4", "R9", "R22", "R25"], "value": "47k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R5", "R6"], "value": "10", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R7", "R23"], "value": "470k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R8", "R24"], "value": "2.2k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R10", "R26"], "value": "10k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R11", "R27"], "value": "36k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R12", "R14", "R15", "R17", "R18", "R28"], "value": "1k", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["R13", "R29"], "value": "220", "datasheet": "~", "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)", "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"}, {"ref": ["U1", "U2", "U4"], "value": "LM324", "datasheet": "http://www.ti.com/lit/ds/symlink/lm2902-n.pdf", "description": "Package_DIP:DIP-14_W7.62mm_Socket", "footprint": "Package_DIP:DIP-14_W7.62mm_Socket"}, {"ref": ["U3"], "value": "4001", "datasheet": "http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4000bms-01bms-02bms-25bms.pdf", "description": "Package_DIP:DIP-14_W7.62mm_Socket", "footprint": "Package_DIP:DIP-14_W7.62mm_Socket"}], "drc": [], "unconnected": [], "erc": []}}}

import kicad
from kicad import parse_kibot
class TestParseFiles(unittest.TestCase):

    def test_schema(self):
        self.assertEqual( kicad.get_kicad_files('/foo/bar.pro')[0], '/foo/bar.sch')

    def test_pcb(self):
        self.assertEqual( kicad.get_kicad_files('/foo/bar.pro')[1], '/foo/bar.kicad_pcb')

    def test_name(self):
        self.assertEqual( kicad.get_kicad_name('/foo/bar.pro'), 'bar')

class TestParseKibot(unittest.TestCase):

    def test_erc_ok(self):
        result = {'erc': []}
        response = {}
        parse_kibot.kibot_parser('test/files/main-erc-ok.txt', response)
        self.assertEqual( response, result)
        
    def test_erc_error(self):
        result = {'erc': [{'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '227.33', 'y': '78.74', 'message': 'Pin 5 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '214.63', 'y': '123.19', 'message': 'Pin 3 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '214.63', 'y': '118.11', 'message': 'Pin 2 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '229.87', 'y': '120.65', 'message': 'Pin 1 (Output) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '233.68', 'y': '100.33', 'message': 'Pin 7 (Output) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '248.92', 'y': '102.87', 'message': 'Pin 6 (Input) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '248.92', 'y': '97.79', 'message': 'Pin 5 (Input) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '242.57', 'y': '76.20', 'message': 'Pin 7 (Output) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '227.33', 'y': '73.66', 'message': 'Pin 6 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '205.74', 'y': '76.20', 'message': 'Pin 7 (Output) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '190.50', 'y': '73.66', 'message': 'Pin 6 (Input) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '190.50', 'y': '78.74', 'message': 'Pin 5 (Input) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '33.02', 'y': '29.21', 'message': 'Pin TN (Passive) of component J2 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '33.02', 'y': '24.13', 'message': 'Pin S (Passive) of component J2 is unconnected.'}]}]}
        response = {}
        parse_kibot.kibot_parser('test/files/main-erc-error.txt', response)
        self.assertEqual( response, result)

    def test_drc_ok(self):
        result = {'drc': [], 'unconnected': []}
        response = {}
        parse_kibot.kibot_parser('test/files/main-drc-ok.txt', response)
        self.assertEqual( response, result)

    def test_drc_unconnected(self):
        result = {'drc': [], 'unconnected': [{'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '94.148', 'message': 'Pad 6 of J1 on All copper layers'}, {'x': '59.182', 'y': '94.148', 'message': 'Pad 5 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '59.182', 'y': '96.688', 'message': 'Pad 7 of J1 on All copper layers'}, {'x': '59.182', 'y': '94.148', 'message': 'Pad 5 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '96.688', 'message': 'Pad 8 of J1 on All copper layers'}, {'x': '59.182', 'y': '96.688', 'message': 'Pad 7 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '96.688', 'message': 'Pad 8 of J1 on All copper layers'}, {'x': '68.732', 'y': '98.518', 'message': 'Pad 1 of C2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '84.542', 'y': '86.868', 'message': 'Pad 2 of C1 on All copper layers'}, {'x': '68.732', 'y': '98.518', 'message': 'Pad 1 of C2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '82.042', 'y': '86.868', 'message': 'Pad 1 of C1 on All copper layers'}, {'x': '67.497', 'y': '84.968', 'message': 'Pad 1 of R1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '71.232', 'y': '98.518', 'message': 'Pad 2 of C2 on All copper layers'}, {'x': '67.497', 'y': '89.018', 'message': 'Pad 1 of R2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '59.182', 'y': '99.228', 'message': 'Pad 9 of J1 on All copper layers'}, {'x': '61.722', 'y': '99.228', 'message': 'Pad 10 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '91.608', 'message': 'Pad 4 of J1 on All copper layers'}, {'x': '59.182', 'y': '91.608', 'message': 'Pad 3 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '77.657', 'y': '84.968', 'message': 'Pad 2 of R1 on All copper layers'}, {'x': '61.722', 'y': '91.608', 'message': 'Pad 4 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '89.068', 'message': 'Pad 2 of J1 on All copper layers'}, {'x': '59.182', 'y': '89.068', 'message': 'Pad 1 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '77.657', 'y': '89.018', 'message': 'Pad 2 of R2 on All copper layers'}, {'x': '61.722', 'y': '89.068', 'message': 'Pad 2 of J1 on All copper layers'}]}]}
        response = {}
        parse_kibot.kibot_parser('test/files/main-drc-unconnected.txt', response)
        self.assertEqual( response, result)

class TestCombineResults(unittest.TestCase):

    def test_combined_reports(self):
        self.assertEqual( parse_kibot.combine_reports(['test/files/kontur_main_bom.json', 'test/files/kontur_main_report.json']), comnbined_result)
