import unittest

from sys import path as syspath
from os import path as ospath

syspath.append(ospath.join(ospath.expanduser("..")))

import kicad

class TestParseFiles(unittest.TestCase):

    def test_schema(self):
        self.assertEqual( kicad.get_kicad_files('/foo/bar.pro')[0], '/foo/bar.sch')

    def test_pcb(self):
        self.assertEqual( kicad.get_kicad_files('/foo/bar.pro')[1], '/foo/bar.kicad_pcb')

if __name__ == '__main__':
    unittest.main() 
