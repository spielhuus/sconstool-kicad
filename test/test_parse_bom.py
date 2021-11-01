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

import kicad
from kicad import parse_kibot

bom_result = {
    "bom": [
        {
            "ref": [
                "C1",
                "C2"
            ],
            "value": "22u",
            "datasheet": "~",
            "description": "Aluminium Electrolytic Capacitors (50V, D=6.3 mm, LS=2.5 mm)",
            "footprint": "Capacitor_THT:CP_Radial_D6.3mm_P2.50mm"
        },
        {
            "ref": [
                "C3",
                "C4",
                "C5",
                "C6",
                "C7",
                "C8",
                "C9",
                "C10",
                "C11",
                "C12"
            ],
            "value": "0.1u",
            "datasheet": "~",
            "description": "Multilayer Ceramic Capacitors MLCC (50V, L=4 mm, W=2.5 mm, LS=2.5 mm)",
            "footprint": "Capacitor_THT:C_Disc_D3.4mm_W2.1mm_P2.50mm"
        },
        {
            "ref": [
                "J1"
            ],
            "value": "10 Pos",
            "datasheet": "~",
            "description": "Pin Header IDC (2.54mm)",
            "footprint": "Connector_IDC:IDC-Header_2x05_P2.54mm_Vertical"
        },
        {
            "ref": [
                "J2"
            ],
            "value": "01x05 Female",
            "datasheet": "~",
            "description": "Board to Board Connectors (2.54 mm)",
            "footprint": "Connector_PinSocket_2.54mm:PinSocket_1x05_P2.54mm_Vertical"
        },
        {
            "ref": [
                "J3"
            ],
            "value": "01x03 Female",
            "datasheet": "~",
            "description": "Board to Board Connectors (2.54 mm)",
            "footprint": "Connector_PinSocket_2.54mm:PinSocket_1x03_P2.54mm_Vertical"
        },
        {
            "ref": [
                "R1",
                "R2"
            ],
            "value": "10",
            "datasheet": "~",
            "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)",
            "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"
        },
        {
            "ref": [
                "R3",
                "R4",
                "R5",
                "R6"
            ],
            "value": "10k",
            "datasheet": "~",
            "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)",
            "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"
        },
        {
            "ref": [
                "R7",
                "R8"
            ],
            "value": "330k",
            "datasheet": "~",
            "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)",
            "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"
        },
        {
            "ref": [
                "R9",
                "R10"
            ],
            "value": "100",
            "datasheet": "~",
            "description": "Metal Film Resistors - Through Hole (L=3.6 mm, D=1.6 mm, 1%)",
            "footprint": "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal"
        },
        {
            "ref": [
                "RV1",
                "RV2"
            ],
            "value": "100k",
            "datasheet": "~",
            "description": "Trimmer Resistor, Bourns 3386P",
            "footprint": "Potentiometer_THT:Potentiometer_Bourns_3386P_Vertical"
        },
        {
            "ref": [
                "U1",
                "U2",
                "U5"
            ],
            "value": "TL072",
            "datasheet": "http://www.ti.com/lit/ds/symlink/tl071.pdf",
            "description": "Package_DIP:DIP-8_W7.62mm_Socket",
            "footprint": "Package_DIP:DIP-8_W7.62mm_Socket"
        }
    ]
}

class TestParseBom(unittest.TestCase):

    def test_letters(self):
        self.assertEqual( parse_kibot.letter('R01'), 'R')
        self.assertEqual( parse_kibot.letter('RV01'), 'RV')

    def test_numbers(self):
        self.assertEqual( parse_kibot.number('R01'), 1)
        self.assertEqual( parse_kibot.number('RV12'), 12)

    def test_parse(self):
        response = {}
        parse_kibot.bom_parser('test/files/produkt.xml', response)
        self.assertEqual( response, bom_result)
