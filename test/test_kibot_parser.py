import unittest

from sys import path as syspath
from os import path as ospath
from pathlib import Path

syspath.append("..")

#syspath.append(Path(ospath.abspath('')).resolve())

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
        response = {'erc': []}
        self.assertEqual( parse_kibot.kibot_parser('test/files/main-erc-ok.txt'), response)
        
    def test_erc_error(self):
        response = {'erc': [{'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '227.33', 'y': '78.74', 'message': 'Pin 5 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '214.63', 'y': '123.19', 'message': 'Pin 3 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '214.63', 'y': '118.11', 'message': 'Pin 2 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '229.87', 'y': '120.65', 'message': 'Pin 1 (Output) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '233.68', 'y': '100.33', 'message': 'Pin 7 (Output) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '248.92', 'y': '102.87', 'message': 'Pin 6 (Input) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '248.92', 'y': '97.79', 'message': 'Pin 5 (Input) of component U6 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '242.57', 'y': '76.20', 'message': 'Pin 7 (Output) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '227.33', 'y': '73.66', 'message': 'Pin 6 (Input) of component U5 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '205.74', 'y': '76.20', 'message': 'Pin 7 (Output) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '190.50', 'y': '73.66', 'message': 'Pin 6 (Input) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '190.50', 'y': '78.74', 'message': 'Pin 5 (Input) of component U4 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '33.02', 'y': '29.21', 'message': 'Pin TN (Passive) of component J2 is unconnected.'}]}, {'code': '2', 'sheet': '/', 'message': 'Pin not connected (use a "no connection" flag to suppress this error)', 'con': [{'x': '33.02', 'y': '24.13', 'message': 'Pin S (Passive) of component J2 is unconnected.'}]}]}
        self.assertEqual( parse_kibot.kibot_parser('test/files/main-erc-error.txt'), response)

    def test_drc_ok(self):
        response = {'drc': [], 'unconnected': []}
        self.assertEqual( parse_kibot.kibot_parser('test/files/main-drc-ok.txt'), response)

    def test_drc_unconnected(self):
        response = {'drc': [], 'unconnected': [{'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '94.148', 'message': 'Pad 6 of J1 on All copper layers'}, {'x': '59.182', 'y': '94.148', 'message': 'Pad 5 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '59.182', 'y': '96.688', 'message': 'Pad 7 of J1 on All copper layers'}, {'x': '59.182', 'y': '94.148', 'message': 'Pad 5 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '96.688', 'message': 'Pad 8 of J1 on All copper layers'}, {'x': '59.182', 'y': '96.688', 'message': 'Pad 7 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '96.688', 'message': 'Pad 8 of J1 on All copper layers'}, {'x': '68.732', 'y': '98.518', 'message': 'Pad 1 of C2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '84.542', 'y': '86.868', 'message': 'Pad 2 of C1 on All copper layers'}, {'x': '68.732', 'y': '98.518', 'message': 'Pad 1 of C2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '82.042', 'y': '86.868', 'message': 'Pad 1 of C1 on All copper layers'}, {'x': '67.497', 'y': '84.968', 'message': 'Pad 1 of R1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '71.232', 'y': '98.518', 'message': 'Pad 2 of C2 on All copper layers'}, {'x': '67.497', 'y': '89.018', 'message': 'Pad 1 of R2 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '59.182', 'y': '99.228', 'message': 'Pad 9 of J1 on All copper layers'}, {'x': '61.722', 'y': '99.228', 'message': 'Pad 10 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '91.608', 'message': 'Pad 4 of J1 on All copper layers'}, {'x': '59.182', 'y': '91.608', 'message': 'Pad 3 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '77.657', 'y': '84.968', 'message': 'Pad 2 of R1 on All copper layers'}, {'x': '61.722', 'y': '91.608', 'message': 'Pad 4 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '61.722', 'y': '89.068', 'message': 'Pad 2 of J1 on All copper layers'}, {'x': '59.182', 'y': '89.068', 'message': 'Pad 1 of J1 on All copper layers'}]}, {'code': '2', 'sheet': '/', 'message': 'Unconnected items', 'con': [{'x': '77.657', 'y': '89.018', 'message': 'Pad 2 of R2 on All copper layers'}, {'x': '61.722', 'y': '89.068', 'message': 'Pad 2 of J1 on All copper layers'}]}]}
        print(parse_kibot.kibot_parser('test/files/main-drc-unconnected.txt'))
        self.assertEqual( parse_kibot.kibot_parser('test/files/main-drc-unconnected.txt'), response)


if __name__ == '__main__':
    print(Path(ospath.abspath('')).resolve())
    unittest.main() 
